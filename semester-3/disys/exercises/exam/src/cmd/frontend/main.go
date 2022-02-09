package main

import (
	"context"
	"errors"
	"net"
	"os"
	"time"

	api "github.com/disys-exam/api"
	"github.com/disys-exam/util"
	"google.golang.org/grpc"
)

type FrontEnd struct {
	util.Server
}

func newFrontEnd() *FrontEnd {
	frontEnd := &FrontEnd{
		Server: *util.NewServer(),
	}

	go frontEnd.HeartbeatLoop()

	return frontEnd
}

func main() {
	server := newFrontEnd()

	server.Logger.IPrintf("Starting server at %v\n", ":50051")

	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		server.Logger.EPrintf("Failed to listen: %v\n", err)

		os.Exit(1)
	}

	s := grpc.NewServer()
	api.RegisterDHTServer(s, server)

	go server.HeartbeatLoop()

	if err := s.Serve(lis); err != nil {
		server.Logger.EPrintf("Failed to serve: %v\n", err)

		os.Exit(1)
	}
}

// =============================================================================
// Util
// =============================================================================
func (f *FrontEnd) ConnectToLeader() (api.DHTClient, *grpc.ClientConn, error) {
	if f.State == util.StateElectee {
		return nil, nil, errors.New("Cannot connect to leader while in election")
	}

	client, conn, err := f.ConnectToNode(f.Servers[f.LeaderId])
	if err != nil {
		f.LeaderError("Failed to connect to leader", err)

		return nil, nil, err
	}

	return client, conn, nil
}

func (f *FrontEnd) LeaderError(message string, err error) {
	f.Logger.EPrintf("%v: %v\n", message, err)

	go f.beginElection()
}

func (f *FrontEnd) RetrieveCachedValue(key int64) int64 {
	f.Mutex.RLock()
	defer f.Mutex.RUnlock()

	value, ok := f.KeyValueStore[key]
	if !ok {
		value = 0
	}

	return value
}

func (f *FrontEnd) SetKeyValueStore(keyValueStore map[int64]int64) {
	f.Mutex.Lock()
	defer f.Mutex.Unlock()

	f.KeyValueStore = keyValueStore
}

func (f *FrontEnd) SetKeyValuePair(key int64, value int64) {
	f.Mutex.Lock()
	defer f.Mutex.Unlock()

	f.KeyValueStore[key] = value
}

func (f *FrontEnd) UpdateHeartbeat() {
	f.HeartbeatMutex.Lock()
	defer f.HeartbeatMutex.Unlock()

	f.HeartbeatTime = time.Now()
}

// =============================================================================
// Requests
// =============================================================================
func (f *FrontEnd) Put(ctx context.Context, request *api.PutRequest) (*api.PutResponse, error) {
	f.Logger.IPrintf("Received Put request: %v\n", request)

	if f.State == util.StateElectee {
		return &api.PutResponse{
			Success: false,
		}, nil
	}

	client, conn, err := f.ConnectToLeader()
	if err != nil {
		return &api.PutResponse{
			Success: false,
		}, err
	}
	defer conn.Close()

	ctx, cancel := context.WithTimeout(ctx, time.Second*20)
	defer cancel()

	response, err := client.Put(ctx, request)
	if err != nil {
		f.LeaderError("Failed to put", err)

		return &api.PutResponse{
			Success: false,
		}, err
	}

	if response.Success {
		f.SetKeyValuePair(request.Key, request.Value)
		go f.UpdateHeartbeat()
	}

	f.Logger.IPrintf("Returning Put response\n")
	return response, nil
}

func (f *FrontEnd) Get(ctx context.Context, request *api.GetRequest) (*api.GetResponse, error) {
	f.Logger.IPrintf("Received Get request: %v\n", request)

	if f.State == util.StateElectee {
		return &api.GetResponse{
			Value: f.RetrieveCachedValue(request.Key),
		}, nil
	}

	client, conn, err := f.ConnectToLeader()
	if err != nil {
		return &api.GetResponse{
			Value: f.RetrieveCachedValue(request.Key),
		}, err
	}
	defer conn.Close()

	ctx, cancel := context.WithTimeout(ctx, time.Second*20)
	defer cancel()

	response, err := client.Get(ctx, request)
	if err != nil {
		f.LeaderError("Failed to get", err)

		return &api.GetResponse{
			Value: f.RetrieveCachedValue(request.Key),
		}, err
	}

	f.Logger.IPrintf("Returning Get response\n")
	go f.UpdateHeartbeat()
	return response, nil
}

// =============================================================================
// Heartbeat
// =============================================================================
func (f *FrontEnd) HeartbeatLoop() {
	for {
		if f.State == util.StateElectee {
			time.Sleep(time.Second * 2)
		} else {
			// Create a new scope, for the defer
			func() {
				f.Logger.IPrintf("Checking heartbeat, time is: %v, and now: %v\n", f.HeartbeatTime, time.Now())

				if time.Now().After(f.HeartbeatTime.Add(time.Duration(time.Second * 10))) {
					f.beginElection()
				}

				time.Sleep(time.Second * 10)
			}()
		}
	}
}

func (f *FrontEnd) Heartbeat(ctx context.Context, request *api.HeartbeatRequest) (*api.HeartbeatResponse, error) {
	f.Logger.IPrintf("Received heartbeat\n")

	f.UpdateHeartbeat()

	// Update key value store to keep in sync
	if request.KeyValuePairs != nil {
		f.SetKeyValueStore(request.KeyValuePairs)
	}

	f.Logger.IPrintf("Heartbeat confirmed\n")

	return &api.HeartbeatResponse{}, nil
}

// =============================================================================
// Election
// =============================================================================
func (s *FrontEnd) beginElection() {
	s.Mutex.Lock()
	defer s.Mutex.Unlock()

	gotResponse, err := s.BeginElection()

	if err != nil {
		return
	}

	if !gotResponse {
		s.Logger.IPrintf("No one responded, exit\n")

		os.Exit(1)
	}
}
