package main

import (
	"context"
	"net"
	"sync"
	"time"

	api "github.com/disys-mock-exam/api"
	"github.com/disys-mock-exam/util"
	"google.golang.org/grpc"
)

type Node struct {
	util.Server

	value int64
}

func newNode() *Node {
	node := &Node{
		Server: *util.NewServer(),
		value:  0,
	}

	return node
}

func main() {
	server := newNode()

	server.Logger.IPrintf("Starting server at: %v\n", ":50051")

	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		server.Logger.EPrintf("Failed to listen: %v", err)
	}

	s := grpc.NewServer()
	api.RegisterIncrementServiceServer(s, server)

	go server.heartBeat()

	if err := s.Serve(lis); err != nil {
		server.Logger.EPrintf("Failed to serve: %v", err)
	}
}

func (s *Node) Increment(ctx context.Context, request *api.IncrementRequest) (*api.IncrementResponse, error) {
	s.Logger.IPrintf("Received increment request\n")

	s.Mutex.Lock()
	defer s.Mutex.Unlock()

	if s.State == util.StateElectee {
		// No leader has been elected, so don't increase the value
		// The requirement says that we always have to return a value, so we return the current value
		return &api.IncrementResponse{
			Value: s.value,
		}, nil
	}

	if s.State == util.StateLeader {
		return s.leaderIncrement(ctx, request)
	} else {
		return s.followerIncrement(ctx, request)
	}
}

// Assumes mutex lock
func (s *Node) leaderIncrement(ctx context.Context, request *api.IncrementRequest) (*api.IncrementResponse, error) {
	s.Logger.IPrintf("Forwarding increment\n")

	var wg sync.WaitGroup

	for processId, server := range s.Servers {
		// Avoid sending to yourself, or service nodes such as the loadbalancer
		if processId == s.ProcessId || processId < 0 {
			continue
		}

		// Add to the wait group
		wg.Add(1)

		go func(server string) {
			s.Logger.IPrintf("Sending increment to %s\n", server)
			defer wg.Done()

			client, conn, err := s.ConnectToNode(server)
			if err != nil {
				return
			}
			defer conn.Close()

			ctx, cancel := context.WithTimeout(context.Background(), time.Duration(3*time.Second))
			defer cancel()

			_, err = client.Increment(ctx, request)
			if err != nil {
				s.Logger.EPrintf("Failed to increment: %v", err)
				return
			}

			s.Logger.IPrintf("Done sending increment to %s\n", server)
		}(server)
	}

	wg.Wait()

	s.increaseValue()

	return &api.IncrementResponse{
		Value: s.value,
	}, nil
}

// Assumes mutex lock
func (s *Node) followerIncrement(ctx context.Context, request *api.IncrementRequest) (*api.IncrementResponse, error) {
	s.increaseValue()

	return &api.IncrementResponse{
		Value: s.value,
	}, nil
}

// Assumes mutex lock
func (s *Node) increaseValue() {
	s.Logger.IPrintf("Incrementing value, current value: %d\n", s.value)

	s.value++

	s.Logger.IPrintf("Incremented value, new value: %d\n", s.value)
}

func (s *Node) GetCurrentValue(ctx context.Context, request *api.CurrentValueRequest) (*api.CurrentValueResponse, error) {
	s.Logger.IPrintf("Received get current value request\n")

	s.Mutex.RLock()
	defer s.Mutex.RUnlock()

	s.Logger.IPrintf("Current value: %d\n", s.value)

	return &api.CurrentValueResponse{
		Value: s.value,
	}, nil
}

func (s *Node) heartBeat() {
	for {
		if (s.State == util.StateLeader) || (s.State == util.StateElectee) {
			time.Sleep(time.Duration(10 * time.Second))
		}

		s.Logger.IPrintf("Sending heart beat\n")

		err := s.pingLeader()
		if err != nil {
			s.Logger.EPrintf("Failed to ping leader: %v", err)
			s.beginElection()
		}

		s.Logger.IPrintf("Heart beat confirmed\n")

		time.Sleep(time.Duration(10 * time.Second))
	}
}

func (s *Node) pingLeader() error {
	s.Logger.IPrintf("Pinging leader\n")

	client, conn, err := s.ConnectToNode(s.Servers[s.LeaderId])
	if err != nil {
		return err
	}
	defer conn.Close()

	ctx, cancel := context.WithTimeout(context.Background(), time.Duration(5*time.Second))
	defer cancel()

	_, err = client.Ping(ctx, &api.PingRequest{})
	if err != nil {
		s.Logger.EPrintf("Failed to ping leader: %v", err)
		return err
	}

	s.Logger.IPrintf("Leader pinged\n")

	return nil
}

func (s *Node) Ping(ctx context.Context, request *api.PingRequest) (*api.PingResponse, error) {
	s.Logger.IPrintf("Received ping\n")
	return &api.PingResponse{}, nil
}

// === ELECTION STUFF ===
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
