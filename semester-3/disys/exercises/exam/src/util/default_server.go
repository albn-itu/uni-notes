package util

import (
	"context"
	"errors"
	"flag"
	"strconv"
	"strings"
	"sync"
	"time"

	api "github.com/disys-exam/api"
	"google.golang.org/grpc"
)

type State string

const (
	StateLeader   State = "LEADER"
	StateFollower State = "FOLLOWER"
	StateElectee  State = "ELECTEE"
)

type Server struct {
	api.UnimplementedDHTServer

	Mutex         sync.RWMutex
	KeyValueStore map[int64]int64

	ProcessId int64
	LeaderId  int64
	State     State

	Servers map[int64]string

	HeartbeatMutex sync.RWMutex
	HeartbeatTime  time.Time

	Logger *Log
}

func NewServer() *Server {
	servers := flag.String("servers", "", "Comma separated list of server IPs in the format id;ip")
	processId := flag.Int64("processId", -2147483648, "Process id")

	flag.Parse()

	serversList := strings.Split(*servers, ",")
	serverMap := make(map[int64]string)
	var highestServer int64 = -1

	for _, server := range serversList {
		serverParts := strings.Split(server, ";")
		s, err := strconv.ParseInt(serverParts[0], 10, 64)
		if err != nil {
			panic(err)
		}

		if s > highestServer {
			highestServer = s
		}

		serverMap[s] = serverParts[1]
	}

	var state State
	if *processId == highestServer {
		state = StateLeader
	} else {
		state = StateFollower
	}

	return &Server{
		Mutex:         sync.RWMutex{},
		KeyValueStore: make(map[int64]int64),

		ProcessId: *processId,
		LeaderId:  highestServer,
		State:     state,

		Servers: serverMap,

		HeartbeatMutex: sync.RWMutex{},
		HeartbeatTime:  time.Now(),

		Logger: New(),
	}
}

// =============================================================================
// Election
// =============================================================================
func (s *Server) ClaimLeader(ctx context.Context, request *api.LeaderAnnouncement) (*api.LeaderAnnouncementAck, error) {
	s.Logger.IPrintf("Received leader announcement from %d\n", request.ProcessId)

	s.Mutex.Lock()
	defer s.Mutex.Unlock()

	s.LeaderId = request.ProcessId
	s.State = StateFollower

	s.Logger.IPrintf("Leader is now %d, ip: %v\n", s.LeaderId, s.Servers[s.LeaderId])

	return &api.LeaderAnnouncementAck{}, nil
}

func (s *Server) ConnectToNode(server string) (api.DHTClient, *grpc.ClientConn, error) {
	s.Logger.IPrintf("Connecting to %s\n", server)

	conn, err := grpc.Dial(server, grpc.WithInsecure(), grpc.WithTimeout(time.Second))
	if err != nil {
		s.Logger.EPrintf("Failed to connect to %v: %v\n", server, err)
		return nil, nil, err
	}

	return api.NewDHTClient(conn), conn, nil
}

func (s *Server) BeginElection() (bool, error) {
	if s.State == StateElectee {
		return false, errors.New("Already in election")
	}

	s.Logger.IPrintf("Starting election\n")

	s.State = StateElectee
	s.LeaderId = -1

	gotResponse := false

	for processId, server := range s.Servers {
		// Avoid sending to self or below you
		if processId == s.ProcessId || processId < s.ProcessId {
			continue
		}

		s.Logger.IPrintf("Sending election request to %d\n", processId)

		client, conn, err := s.ConnectToNode(server)
		if err != nil {
			s.Logger.EPrintf("Failed to connect to server: %v\n", err)
			continue
		}
		defer conn.Close()

		_, err = client.Election(context.Background(), &api.ElectionRequest{ProcessId: s.ProcessId})
		if err != nil {
			s.Logger.EPrintf("Failed to send election request: %v\n", err)
			continue
		}

		gotResponse = true
		break
	}

	return gotResponse, nil
}
