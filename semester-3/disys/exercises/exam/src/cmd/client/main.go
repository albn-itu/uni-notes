package main

import (
	"context"
	"flag"
	"math/rand"
	"time"

	"github.com/disys-exam/api"
	"github.com/disys-exam/util"
	"google.golang.org/grpc"
)

type Client struct {
	serverAddr string
	logger     *util.Log
	client     api.DHTClient
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

	c := api.NewDHTClient(conn)
	ctx, cancel := context.WithCancel(context.Background())

	client.client = c
	client.context = ctx
	defer cancel()

	autoTest(client)
}

func autoTest(c *Client) {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))

	for {
		if r.Intn(10) <= 5 {
			c.logger.IPrintf("Putting\n")
			result, err := c.client.Put(c.context, &api.PutRequest{
				Key:   int64(r.Intn(100)),
				Value: int64(r.Intn(100)),
			})
			if err != nil {
				c.logger.EPrintf("Could not increment: %v\n", err)
				break
			}

			c.logger.IPrintf("Success: %t\n", result.Success)
		} else {
			c.logger.IPrintf("Retrieving value\n")

			key := int64(r.Intn(100))

			result, err := c.client.Get(c.context, &api.GetRequest{
				Key: key,
			})
			if err != nil {
				c.logger.EPrintf("Could not get value: %v\n", err)
				break
			}

			c.logger.IPrintf("Value of %d: %d\n", key, result.Value)
		}

		time.Sleep(time.Duration(r.Intn(10)) * time.Second)
	}
}
