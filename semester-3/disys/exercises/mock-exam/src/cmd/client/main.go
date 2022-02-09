package main

import (
	"context"
	"flag"
	"math/rand"
	"time"

	"github.com/disys-mock-exam/api"
	"github.com/disys-mock-exam/util"
	"google.golang.org/grpc"
)

type Client struct {
	serverAddr string
	logger     *util.Log
	client     api.IncrementServiceClient
	context    context.Context
}

func main() {
	serverAddr := flag.String("serverAddr", "localhost:5001", "Address of the server")
	flag.Parse()

	client := &Client{
		serverAddr: *serverAddr,
		logger:     util.New(),
	}

	client.logger.IPrintf("Connecting to server at: %v\n", client.serverAddr)
	conn, err := grpc.Dial(client.serverAddr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		client.logger.EPrintf("Could not connect: %v\n", err)
	}
	defer conn.Close()

	c := api.NewIncrementServiceClient(conn)
	ctx, cancel := context.WithCancel(context.Background())

	client.client = c
	client.context = ctx
	defer cancel()

	autoIncrement(client)
}

func autoIncrement(c *Client) {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))

	for {
		if r.Intn(10) <= 5 {
			c.logger.IPrintf("Incrementing\n")
			result, err := c.client.Increment(c.context, &api.IncrementRequest{})
			if err != nil {
				c.logger.EPrintf("Could not increment: %v\n", err)
				break
			}

			c.logger.IPrintf("New value: %v\n", result.Value)
		} else {
			c.logger.IPrintf("Retrieving current value")
			result, err := c.client.GetCurrentValue(c.context, &api.CurrentValueRequest{})
			if err != nil {
				c.logger.EPrintf("Could not get current value: %v\n", err)
				break
			}

			c.logger.IPrintf("Current value: %v\n", result.Value)
		}

		time.Sleep(time.Duration(r.Intn(10)) * time.Second)
	}
}
