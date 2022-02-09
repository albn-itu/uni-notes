# Mock-exam 2021
Started: 16:39 - 18:58 ~ 2h and 19m
## Multiple choice
1. A race condition is (correct)
   1. [ ] a Go lang language library for writing concurrent applications that share resources
   2. [x] when two or more threads simulatenously access a resource leading to unwanted behaviour. 
   3. [ ] using a lock on a resource that leads to a deadlock
2. The UDP protocol (correct)
   1. [x] can be used for  streaming videos
   2. [ ] guarantees that messages are delivered in the order they were sent
   3. [ ] guarantees that messages are never lost 
3. The Raft consensus algorithm (correct)
   1. [x] ensures that at most one leader can be elected in a given term
   2. [ ] ensures that a leader can always overwrite or delete entries in its log
   3. [ ] is such that every replica can only be in one of the following states: Follower or Leader
4. Passive replication is such that (correct)
   1. [ ] all replicas run the same code and process all requests concurrently
   2. [ ] there is a client-server architecture and the server may never crash
   3. [x] a single primary replica handles all requests and uses the other replicas as backup
5. Assume we have N nodes in an asynchronous system, and we know that 22% might have Byzantine faults. What is correct (Correct)
   1. [ ] The Byzantine generals problem can be solved for any N
   2. [ ] The Byzantine generals problem can be solved for N <3
   3. [x] The Byzantine generals problem cannot be solved for any N.
6. What properties do we require from a Distributed Mutual Exclusion algorithm (half correct)
   1. [x] safety and liveliness 
   2. [x] that resource assess to Critical Section happens after a token is acquired
   3. [ ] that each node can enter the Critical Section exactly once
7. Given two events a, b in a distributed system (correct)
   1. [ ] We can always determine if 'a' happens before 'b', or 'b' happens before 'a'
   2. [x] if 'a' happens before 'b', then 'a' might have caused 'b'
   3. [ ] the physical clock is always consitent with causuality
8. On figure 1 below, we can say the following (correct)
   1. [ ] (1, A) is the vector clock value
   2. [ ] (3,A)happens before  (4,B)
   3. [x] (1,A) happens before (5,C)
9. What kind of RPC semantics ensures message delivery (half correct)
   1. [ ] First-in-first-out semantic
   2. [x] At least-once-semantic
   3. [x] At-most-once-semantic
10. What is a correct statement about RESTful webservices (correct)
   1. [x] POST does not have to be idempotent
   2. [ ] They need to have an Open API /Swagger definition
   3. [ ] They use only the verbs of the HTTP protocol: GET, PUT, PUBLISH, DELETEv

## Implementation
Placed in the `src` folder, written in go with Docker images to help run it. Run with
```
docker-compose up
```

## Implementation discussion
### What system model are you assuming in your implementation. Write a full desciption.
Assuming an asynchronous network with the possibility of a crash, pr requirements, i use the bully leader system with multiple nodes, where the leader forwards requests, have them acknowledged and then responds to the original request.

#### Frontend
Basically just a proxy to the leader, this node is a part of the cluster, meaning that it will also recieve leader announcements like the rest of the system, allowing a client to only talk to the frontend, not having to know about the rest of the cluster.

#### Node
Has 3 states, follower, leader, electee. 

- Follower
  - Just executes the leaders requests, while continuosly pinging it, if a response is not given from the heartbeat, it enters electee state.
- Leader
  - Recieves requests from the frontend and executes them on each node before executing on itself
- Electee
  - 1. Sends election request to every node with higher process id than itself
    - 2. If no response from any of the higher nodes
    - 3. Send leader announcement to every node in the cluster
  - 2. If an election request is recieved, respond to it
  - 3. Probagate to higher nodes

#### Issues
- The is no consensus algorithm which means that if a node is corrupted it could return the wrong value if elected leader in the future, such an algorithm could be implemented for extra security.
- If the frontend crashes and doesn't recover then the client has no ability to contact the system even though the system may still work. 

### What is the minmal number of nodes in your system to fullfill the requirements? Why?
2+frontend, 1 node can fail in this state and the system will still continue to function. But if that happens it will stop upholding the requirement, so philosopically and infinite amount of nodes are required.

### Explain how your system recovers from crash failure.
If a node in follower state crashes, not much happens, it just doesn't recieve any updates. If a leader node crashes and election is started to find the next leader. If there are no nodes left and the system recieves a request, the frontend will shutdown.

### Explain how you achieve the Monotonicity requirement.
Since we ensure that every node responds before moving on to the next request we ensure that every node is up to date, and since the action only consits of incrementing with one, and nothing else, the following requests must therefore be above the first one.

### Explain how you achieve the Liveliness requirement.
If the system is in an election state, or is otherwise unreachable the frontend will return the last returned value.
