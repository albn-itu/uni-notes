I hereby declare that this submission was created in its entirety by me and only me. I have recycled some code from my mock exam solution, specifically the logger and small parts of the default server implementation. 

Albert Rise Nielsen

=======


# Exam 2021

## Multiple choice
1. Assume that a blockchain network has been attacked, and that at least 40% of the nodes have Byzantine faults. What is correct
   1. The network consistency is compromised since the Byzantine generals problem cannot be solved

2. The *Token Ring* distributed mutual exclusion algorithm on N Nodes
   
   2. has a continuos bandwidth consumption

3. The happened before relation

   3. is transitive

4. In a network 

   1. that is synchronous, messages always arrive with progation delay at most D

5. A design goal for Microservices is 

   2. internal implementation details are hidden

6. We definitely have a deadlock when

   1. a process P1 has a lock on a resource A while waiting to get a lock on another resource B; and, at the same time a process P2 has a lock on resource B while waiting to get a lock on resource A

7. The TCP protocol 

   1. cannot be used for streaming videos

8. In the Raft consensus algorithm 

   3. the leader uses the heartbeat for notifying it is still alive and for sending updates about the log

9. Sequential Consistency does not imply that 

   1. requests from all clients are processed in the same order that they were received


9. An operation is idempotent when

   1. applying it several consecutive times yields the same result

## Implementation
Placed in the `src` folder, written in go with Docker images to help run it. Run with
```
docker-compose up
```

## Implementation discussion
### What system model are you assuming in your implementation. Write a full desciption.
I am assuming a system model with crash failures using an asynchronous network. This means that the nodes should be able to crash and recover their state, as well as function over the network with some sort of consensus / leader.

I have decided to use the bully leader tactic, which means the highest process id is elected leader, in case of the original leader crash. On top of that i have decided to take a note from the RAFT algorithm, which uses heartbeats from the leader to notify liveness to other nodes, RAFT also includes the log in it's heartbeats, both of which my system model does.

Quick explanation of binaries:

- Node
  - Implements the proto file
  - processId > 0
  - Can be leader, follower or electee (These states and their behavior is explained further down)
- Frontend
  - Implements the proto file
  - processId = -2147483648
  - A proxy to the cluster, considered to be a node by other nodes, so it recieves election notices and can start elections but will never be elected due to it's low id, if it does get elected it assumes the entire system has crashed as it would not have recieved a response from anyone above it.
- Client
  - Randomly sends get or put requests to the frontend in random intervals

*NOTE: The crash failure recovery is beyond the scope of this implementation*

**Heartbeats**

![heartbeats](./out/diagram/Heartbeat.png)

The leader is responsible for notifying the other clients of it's liveness, by sending a heartbeat to each of them in intervals of 5 seconds. In each heartbeat it includes the current version of the map which allows out of date nodes to update themselves, this is useful in case of a crash fx. (The crash recovery is not implemented though)

On each node (including the frontend) is a value which stores the local time that the last heartbeat was recieved and a constantly running thread which checks every 10 seconds whether or not it has recieved a heartbeat within the last 10 seconds (It should have recieved 2 on average), if it hasn't recieved one it assumes the leader has crashed and starts the election process.

**Requests**

![requests](./out/diagram/Request.png)

(See diagram above, the following is a textual explanation of the same concept)

When a client sends a put request to the frontend the frontend forwards it to the current leader. Said leader then executes the request on each node in the cluster, when that is done it executes it on itself. Returns the result to the frontend, which in turn returns it to the client.

When a client sends a get request to the frontend the frontend forwards it to the current leader. Said leader then retrieves the value from its critical section and returns it to the frontend which returns it to the client.

**Elections**

![election](./out/diagram/Election.png)

(See diagram above, the following is a textual explanation of the same concept)

As stated previously the election process starts when a node hasn't recieved a heartbeat within the last 10 seconds.

When the process starts the node sends an election request to the nodes with a higher process id than itself, stopping if it recieves a response, as that must mean it cannot be the leader. When a node receives an election request it returns a response and starts it's own election, this happens until a node no longer recieves a response, as that must mean that it has the highest id. When that happens the node in question notifies every other node of it's victory and starts acting as the leader. Every other node set's their internal register of the leader and acts as followers (except the frontend, which just starts using the new leader)

While the election process is running, the nodes will not compute any requests so the put response will have success as false, and any get requests will use the cached version of the data set that the frontend has.

### What is the minimal number of nodes in your system to fullfill the requirements? Why?
Technically 2, plus the frontend.

The leader or follower can crash without having the system stop responding. Since there is no consensus implemented, there is no need for any specific number of nodes, though the larger the better, as if you have 2 nodes and 1 crashes then there will no longer be any backups, meaning that if the last node crashes all the data is lost.

### Explain how your system recovers from crash failure.
In the current implementation the node that crashed is assumed to never recover. Though with the heartbeat system recovery is possible to implement.

If a follower node crashes it will just not recieve any updates, the leader will not stop trying to communicate with it though, so if it is a temporary outage it will eventually get updates again.

If a leader node crashes the follower nodes, or frontend, will start the election process to select a new leader.

### Explain how you achieve the Property 1 requirement.
I use a hashmap to store values and keys, which in itself fullfills that requirement.

Since a crashed node is assumed to never recover, and since the system ensures the nodes are always updated with the newest version of the map (due to the heartbeats) the system will always have repeatable reads, if, and only if, the put request actually succeeded. 

*Note: I just realised that if a leader node recovers, from a network outage, it will assume it's leader position again without communicating that to the rest of the system, this could break this requirement. Since it would send heartbeats to the rest of the system with it's possibly outdated hashmap.*

### Explain how you achieve the Property 2 requirement.
Simply check whether or not the hashmap contains the key, if it doesn't return 0.

### Explain how you achieve the Property 3 requirement.
Every put request is computed on every node before completing on the leader node, and returning the result thereby ensuring consistency. This is further established by sending the current version of the map with every heartbeat.

To further complete this requirement, a mutex is used on every node to ensure that no data races happen.

### Explain how you achieve the Property 4 - Liveness requirement.
The only way that a put request fails is if the system is in the election state, which it will exit eventually, so a put request will eventually succeed, unless every node has crashed, leaving only the frontend which will eventually crash when it realises that there are no live nodes.

So the requirement is filled, assuming that there are 1 or more nodes alive.

### Explain how you achieve the Property 5 - Reliability requirement.
As explained in "What is the minimal number of nodes in your system to fullfill the requirements? Why?", if there are 2 or more nodes + the frontend alive the system can tolerate a crash of 1 node.

