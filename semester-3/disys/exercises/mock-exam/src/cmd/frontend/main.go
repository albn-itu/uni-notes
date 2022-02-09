package main

import (
	"context"
	"errors"
	"net"
	"os"
	"time"

	api "github.com/disys-mock-exam/api"
	"github.com/disys-mock-exam/util"
	"google.golang.org/grpc"
)

type FrontEnd struct {
	util.Server

	lastValue int64 // Sort of a cache
}

func newFrontEnd() *FrontEnd {
	return &FrontEnd{
		Server: *util.NewServer(),

		lastValue: 0,
	}
}

// Main function that listens for connections using grpc
func main() {
	server := newFrontEnd()

	// listen for incoming connections on port 50051
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		server.Logger.EPrintf("failed to listen: %v", err)
	}

	// create a new grpc server
	s := grpc.NewServer()

	// register the server and the generated protobuf code
	api.RegisterIncrementServiceServer(s, server)
	server.Logger.IPrintf("starting server at: %v\n", lis.Addr())

	// start the server
	if err := s.Serve(lis); err != nil {
		server.Logger.EPrintf("failed to serve: %v", err)
	}
}

func (s *FrontEnd) ConnectToLeader() (api.IncrementServiceClient, *grpc.ClientConn, error) {
	if s.State == util.StateElectee {
		return nil, nil, errors.New("Cannot connect to leader while in election")
	}

	client, conn, err := s.ConnectToNode(s.Servers[s.LeaderId])
	if err != nil {
		s.LeaderError("Failed to connect to leader", err)

		return nil, nil, err
	}

	return client, conn, nil
}

func (s *FrontEnd) LeaderError(message string, err error) {
	s.Logger.EPrintf("%s: %v\n", message, err)

	// Since the leader is not working, we need to start an election
	go s.beginElection()
}

func (s *FrontEnd) Increment(ctx context.Context, request *api.IncrementRequest) (*api.IncrementResponse, error) {
	s.Logger.IPrintf("Received increment request\n")

	s.Mutex.Lock()
	defer s.Mutex.Unlock()

	if s.State == util.StateElectee {
		return &api.IncrementResponse{
			Value: s.lastValue,
		}, nil
	}

	client, conn, err := s.ConnectToLeader()
	if err != nil {
		return &api.IncrementResponse{}, nil
	}
	defer conn.Close()

	ctx, cancel := context.WithTimeout(context.Background(), time.Duration(10*time.Second))
	defer cancel()

	response, err := client.Increment(ctx, request)
	if err != nil {
		s.LeaderError("Failed to send increment message", err)

		return &api.IncrementResponse{
			Value: s.lastValue,
		}, nil
	}

	s.Logger.IPrintf("Increment response: %v\n", response)

	s.SetLastValue(response.Value)

	return response, nil
}

func (s *FrontEnd) GetCurrentValue(ctx context.Context, request *api.CurrentValueRequest) (*api.CurrentValueResponse, error) {
	s.Logger.IPrintf("Received current value request\n")

	s.Mutex.Lock()
	defer s.Mutex.Unlock()

	if s.State == util.StateElectee {
		return &api.CurrentValueResponse{
			Value: s.lastValue,
		}, nil
	}

	client, conn, err := s.ConnectToLeader()
	if err != nil {
		return &api.CurrentValueResponse{}, nil
	}
	defer conn.Close()

	ctx, cancel := context.WithTimeout(context.Background(), time.Duration(5*time.Second))
	defer cancel()

	response, err := client.GetCurrentValue(ctx, request)
	if err != nil {
		s.LeaderError("Failed to send current value message", err)

		return &api.CurrentValueResponse{
			Value: s.lastValue,
		}, nil
	}

	s.SetLastValue(response.Value)

	return response, nil
}

// Assumes that the mutex is locked
func (s *FrontEnd) SetLastValue(value int64) {
	s.Logger.IPrintf("Setting last value to %v\n", value)

	s.lastValue = value

	s.Logger.IPrintf("Last value set to %v\n", value)
}

func (s *FrontEnd) beginElection() {
	gotResponse, err := s.BeginElection()

	if err != nil {
		return
	}

	if !gotResponse {
		s.Logger.IPrintf("No one responded, exit\n")

		os.Exit(1)
	}
}
