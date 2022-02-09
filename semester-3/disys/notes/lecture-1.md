# Lecture 1

## Course intro

### Format

14 weeks then 3 weeks working on a project

~10 hr/week

10 lectures

3 group based projects

3 group based exercise sets

Weekly exercises (Not mandatory, but just do them lmao)



## DISYS intro

DISYS = Distributed systems

A distributed system is one which components located at networked computers communicate and coordinates their actions only by passing messages. In that sense a distributed system is a network of computers doing work together.

A distributed system is a network of many entities which communicate by messages, to handle the problems that this interaction creates, we create models.

### 8 fallacies of Distributed Computing

- The networks is reliable
- No latency
- Bandwitch is infinite
- The network is secure
- Toplogy doesnt change
- There is one administrator
- Transport cost is zero
- The network is homogeneous

In genereal the biggest failure of distributed computing is brought by using a network to comunicate which brings on a lot more points of failure

### Challenges

- Heterogeneity
  - Network
  - Computer hardware
  - Operating systems
  - Programming languages
  - Software developers
- Openness // TODO: Missing stuff
  - Support of extensions and changes
  - Requires standardised public interfaces
- Security
  - Access control (Authentication, identification)
  - Denial of service attacks
  - Updates, delegations, mobile code
  - Social engineering
- Scalability // TODO: Missing stuff
  - Physical resources (O(n))
  - Performance loss
- Concurrency (Just use Rust)
  - Resource sharing
  - Interference
  - Deadlock
  - Fairness
  - Concurrency control
- Transparency
  - Local/remote access
  - Physical location
  - Concurrency
  - Replication
  - Failure
  - Mobility
  - Performance 
  - Scaling
- Quality of service
  - Reliability
  - Performance
  - Security
- Failure handling
  - Detect failures
  - Mask failures
  - Tolerate/avoid failures (try/catch)
  - Recover from failures
    - A failure protocol
    - Backups

### Models

An abstraction of a software system

#### Architecture model

Network, machines and topology

- Entities and communication
- Client-server architecture
  - Includes clients, which connect to a server.
  - Servers can also be clients and connect to other servers
  - Variations:
    - Proxy and cache 
    - Mobile code
      - Such as HTML from a web server
- Peer-to-peer
  - Clients connecting to each other and sharing information

#### Fundamental models

- Interaction
  - Latency (Time it takes to deliver a message)
  - Bandwith (Transfer amount)
  - Jitter (Delivery time variation)
  - Synchronous
    - Follows a very certain pattern of execution steps
    - Bounds on execution step
    - Guaranteed transmission in bounded time
    - Clock drift bounds
  - Asynchronous
    - Can jump around in the execution steps
    - No bounds on execution step
    - No time bound on transmission
    - Arbitrary clock drift
  - Modelling of events ordering
- Failures
  - Reasoning and detecting of failures

### Security model

- Identification
- Authentication
- Confidentiality
- Integrity
- Threat model:
  - Capabilities of the adversary



## Go

