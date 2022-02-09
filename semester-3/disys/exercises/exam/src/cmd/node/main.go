package main

import (
	"context"
	"net"
	"os"
	"sync"
	"time"

	api "github.com/disys-exam/api"
	"github.com/disys-exam/util"
	"google.golang.org/grpc"
)

type Node struct {
	util.Server
}

func newNode() *Node {
	node := &Node{
		Server: *util.NewServer(),
	}

	return node
}

func main() {
	server := newNode()

	server.Logger.IPrintf("Starting server at: %v\n", ":50051")

	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		server.Logger.EPrintf("Failed to listen: %v", err)

		os.Exit(1)
	}

	s := grpc.NewServer()
	api.RegisterDHTServer(s, server)

	go server.HeartbeatLoop()

	if err := s.Serve(lis); err != nil {
		server.Logger.EPrintf("Failed to serve: %v", err)

		os.Exit(1)
	}
}

// =============================================================================
// Requests
// =============================================================================
func (s *Node) Get(ctx context.Context, request *api.GetRequest) (*api.GetResponse, error) {
	s.Logger.IPrintf("Received Get request: %v\n", request)

	s.Mutex.RLock()
	defer s.Mutex.RUnlock()

	value, ok := s.KeyValueStore[request.Key]
	if !ok {
		value = 0
	}

	s.Logger.IPrintf("Returning Get response: %v\n", value)
	return &api.GetResponse{Value: value}, nil
}

func (s *Node) Put(ctx context.Context, request *api.PutRequest) (*api.PutResponse, error) {
	s.Logger.IPrintf("Received Put request: %v\n", request)

	s.Mutex.Lock()
	defer s.Mutex.Unlock()

	if s.State == util.StateLeader {
		return s.leaderPut(request)
	} else {
		return s.followerPut(request)
	}
}

// Assumes the mutex is locked
func (s *Node) leaderPut(request *api.PutRequest) (*api.PutResponse, error) {
	s.Logger.IPrintf("Forwarding put request: %v\n", request)

	var wg sync.WaitGroup

	for processId, server := range s.Servers {
		// Skip self and service nodes such as the loadbalancer
		if processId == s.ProcessId || processId < 0 {
			continue
		}

		wg.Add(1)

		go func(server string, processId int64) {
			defer wg.Done()
			s.Logger.IPrintf("Sending put request to %d\n", processId)

			client, conn, err := s.ConnectToNode(server)
			if err != nil {
				return
			}
			defer conn.Close()

			ctx, cancel := context.WithTimeout(context.Background(), time.Duration(3*time.Second))
			defer cancel()

			_, err = client.Put(ctx, request)
			if err != nil {
				s.Logger.EPrintf("Failed to send put request to %d: %v\n", processId, err)
				return
			}

			s.Logger.IPrintf("Sent put request to %d\n", processId)
		}(server, processId)
	}

	wg.Wait()

	s.KeyValueStore[request.Key] = request.Value

	s.Logger.IPrintf("Returning Put response: %v\n", request)
	return &api.PutResponse{
		Success: true,
	}, nil
}

// Assumes the mutex is locked
func (s *Node) followerPut(request *api.PutRequest) (*api.PutResponse, error) {
	s.Logger.IPrintf("Follower put\n")

	if s.KeyValueStore == nil {
		s.Logger.EPrintf("Map is nil\n")
		s.KeyValueStore = make(map[int64]int64)
	}

	s.KeyValueStore[request.Key] = request.Value

	s.Logger.IPrintf("Returning Put response: %v\n", request)
	return &api.PutResponse{
		Success: true,
	}, nil
}

// =============================================================================
// Heartbeat
// =============================================================================
func (n *Node) HeartbeatLoop() {
	for {
		if n.State == util.StateLeader {
			n.leaderHeartbeat()
			time.Sleep(time.Second * 5)
		} else if n.State == util.StateFollower {
			n.followerHeartbeat()
			time.Sleep(time.Second * 10)
		} else {
			time.Sleep(time.Second * 2)
		}
	}
}

func (n *Node) leaderHeartbeat() {
	n.Logger.IPrintf("Sending heartbeats\n")
	var wg sync.WaitGroup

	for processId, server := range n.Servers {
		if processId == n.ProcessId {
			continue
		}

		wg.Add(1)

		go func(server string, processId int64) {
			defer wg.Done()

			n.Logger.IPrintf("Sending heartbeat to %d\n", processId)

			client, conn, err := n.ConnectToNode(server)
			if err != nil {
				return
			}
			defer conn.Close()

			n.HeartbeatMutex.RLock()
			// 5 second timeout
			ctx, cancel := context.WithTimeout(context.Background(), time.Duration(5*time.Second))
			defer cancel()

			_, err = client.Heartbeat(ctx, &api.HeartbeatRequest{KeyValuePairs: n.KeyValueStore})
			n.HeartbeatMutex.RUnlock()
			if err != nil {
				n.Logger.EPrintf("Failed to send heartbeat to %d: %v\n", processId, err)
				return
			}

			n.Logger.IPrintf("Heartbeat confirmed from %d\n", processId)
		}(server, processId)
	}

	wg.Wait()
}

func (n *Node) followerHeartbeat() {
	n.HeartbeatMutex.RLock()
	defer n.HeartbeatMutex.RUnlock()

	n.Logger.IPrintf("Checking heartbeat, time is: %v, and now: %v\n", n.HeartbeatTime, time.Now())

	if time.Now().After(n.HeartbeatTime.Add(time.Duration(time.Second * 10))) {
		n.beginElection()
	}
}

func (n *Node) Heartbeat(ctx context.Context, request *api.HeartbeatRequest) (*api.HeartbeatResponse, error) {
	n.Logger.IPrintf("Received heartbeat\n")

	n.HeartbeatMutex.Lock()
	n.Mutex.Lock()
	defer n.HeartbeatMutex.Unlock()
	defer n.Mutex.Unlock()

	n.HeartbeatTime = time.Now()

	// Update key value store to keep in sync
	if request.KeyValuePairs != nil {
		n.KeyValueStore = request.KeyValuePairs
	}

	n.Logger.IPrintf("Heartbeat confirmed\n")

	return &api.HeartbeatResponse{}, nil
}

// =============================================================================
// Election
// =============================================================================
func (s *Node) beginElection() {
	if s.State == util.StateElectee {
		return
	}

	s.Mutex.Lock()
	defer s.Mutex.Unlock()

	gotResponse, err := s.BeginElection()

	if err != nil {
		return
	}

	if !gotResponse {
		s.Logger.IPrintf("No one responded, i am the leader, send leader announcement\n")

		s.LeaderId = s.ProcessId
		s.State = util.StateLeader

		s.sendLeaderAnnouncement()
	}
}

func (s *Node) sendLeaderAnnouncement() {
	s.Logger.IPrintf("Sending leader announcement\n")

	var wg sync.WaitGroup

	for processId, server := range s.Servers {
		// Avoid sending to yourself
		if processId == s.ProcessId {
			continue
		}

		wg.Add(1)

		go func(processId int64, server string) {
			defer wg.Done()

			s.Logger.IPrintf("Sending leader announcement to %d\n", processId)

			client, conn, err := s.ConnectToNode(server)
			if err != nil {
				return
			}
			defer conn.Close()

			ctx, cancel := context.WithTimeout(context.Background(), time.Duration(5*time.Second))
			defer cancel()

			_, err = client.ClaimLeader(ctx, &api.LeaderAnnouncement{
				ProcessId: s.ProcessId,
			})
			if err != nil {
				s.Logger.EPrintf("Failed to send leader announcement: %v", err)
				return
			}

			s.Logger.IPrintf("Sent leader announcement to %d\n", processId)
		}(processId, server)
	}

	wg.Wait()

	s.Logger.IPrintf("Leader announced\n")
}

func (s *Node) Election(ctx context.Context, request *api.ElectionRequest) (*api.ElectionResponse, error) {
	s.Logger.IPrintf("Received election request from %d\n", request.ProcessId)

	s.Mutex.Lock()
	defer s.Mutex.Unlock()

	if request.ProcessId < s.ProcessId {
		if s.State == util.StateLeader {
			s.Logger.IPrintf("I am the leader, sending leader announcement\n")

			go s.sendLeaderAnnouncement()

			return &api.ElectionResponse{}, nil
		}

		s.Logger.IPrintf("I am higher than %d, beginning own election\n", request.ProcessId)

		go s.beginElection()

		return &api.ElectionResponse{}, nil
	} else {
		s.State = util.StateElectee
		s.LeaderId = -1
	}

	return &api.ElectionResponse{}, nil
}
