---
title: Mandatory hand-in 2
author: Albert Rise Nielsen (albn@itu.dk)
date: 19-10-2022
---

# Running the game 

My implementation is written in Rust, using [Tonic](https://github.com/hyperium/tonic) for GRPC. To run it 2 Dockerfile's are provided, these are both used in the `docker-compose.yaml` file, which i suggest running through.

To run it:

- First go to the root of the project.
- Run `cd data && bash gen_certs.sh`, to generate certificates
- Build and run the docker compose with `docker compose up --build`

## Output
Using the above you should get something like:

```
...a bunch of build messages
handin-2-bob-1    | [2022-10-19 13:19:59.653355897 +00:00] InitPedersenRequest { h: 1578916582, g: 3485915850, p: 1236607165 }
handin-2-alice-1  | ["Wed, 19 Oct 2022 13:19:59 GMT"][Code: "0"] InitPedersenReply { ack: true }
handin-2-bob-1    | [2022-10-19 13:19:59.653873542 +00:00] SendCommitmentRequest { c: 823808275 }
handin-2-alice-1  | ["Wed, 19 Oct 2022 13:19:59 GMT"][Code: "0"] SendCommitmentReply { m: 3 }
handin-2-bob-1    | [2022-10-19 13:19:59.654185602 +00:00] SendPedersenRequest { r: 15227874476282040476, m: 2 }
handin-2-bob-1    | Dice game finished: 2
handin-2-alice-1  | ["Wed, 19 Oct 2022 13:19:59 GMT"][Code: "0"] SendPedersenReply { ack: true }
handin-2-alice-1  | Dice roll result: 2
handin-2-alice-1 exited with code 0
```

# The protocol
## The goal
The goal of our protocol is to achieve

- Confidentiality: The message should be hidden from the outside world
- Authenticity: We need to know the message comes from the right person
- Integrity: We need to know the message has not been altered.

To achieve the above we use the Coin tossing protocol, with Pedersen commitments, all sent over TLS.

## Coin tossing

The coin tossing scheme allows 2 parties to both pick a random number and send it to each other, while being sure none of the parties have cheated. It does so by using an XOR operation on the resulting 2 numbers, thereby ensuring that if at least one of the numbers were random, then the result will be too.

To ensure that no party has cheated we use commitments.

## Commitments

A commitment is an algorithm applied to a message that destroys the message, but can be calculated from the message. Therefore it can be sent as a substitute for the message, that the recieving party cannot decode until the sending party sends over the original message. 

They allow asynchronous communication where one party can pick a message, send the commitment, recieve the other party's message and then send over the original message, thereby ensuring the other party has not sent their message based on the original message.

I've used Pedersen commitments in this assignment. Pedersen commitments are based on the discrete logarithm problem to ensure that the message is completely impossible, with current technology, to decode.

Commitments provide us with our integrity.

## TLS

TLS provides Confidentiality, authenticity and integrity. Confidentiality is achieved with the use of asymmetric cryptography to share a session specific shared key. The shared key will be used to encrypt further communication. This protects against a Dolev-Yao attacker.

Authenticity is provided using certificates. These contain information about the server, the CA (Certificate Authority, assumed to be trusted) that vouches for the integrity of the certificate, and the servers public key. Authenticity is essentially achieved using a third party, the CA, that can vouch for the credibility of the certificate, and thereby the server.

Lastly TLS provides integrity by calculating a message authentication code (MAC) and appending it to the message, specifically an HMAC is used in TLS 1.2.

In this project i've used mutual TLS (mTLS), which means that both the server and the client have certificates that they exchange. Both signed by the same third party CA (The CA isself-signed in this assignment, to not widen the scope too much). The protocol of mTLS is as follows:

- Client connects to server
- Server presents certificate
- Client verifies certificate against CA
- Client presents certificate
- Server verifies certificate against CA
- Server grants access
- Client and server exchange encrypted information

This results in a completely trusting and verified relationship between the 2 parties.

## How does the game work?
Let's assume 2 parties a client Alice, and a server Bob. 

- **Alice:** Connects to bob
- *The TLS handshake described above takes place*
- **Alice:** Generates Pedersen commitment data, and sends `h`,`g` and `p` to Bob.
- **Bob:** Stores and acknowledges data
- **Alice:** Rolls dice, saves result and calculates commitment
- **Alice:** Sends commitment to Bob
- **Bob:** Stores commitment, rolls dice and responds with dice result to Alice
- **Alice:** Sends `r` and and dice roll to Bob
- **Bob:** Calculates commitment based on Alice's dice roll and verifies that it matches the previously sent commitment 
- **Bob:** Acknowledges commitment
- **Both:** Calculates and prints XOR of the rolls, thereby ending the game.
- **Alice:** Disconnects from Bob

### Pitfalls
The server (Bob) currently has no relation to the status of Alice. So if Alice disconnects and another person connects the other person will be using the state that Alice got to. This could cause issues.

The server does not automatically shut down after the game is done.

Both of these issues could be fixed by implementing my own stream, as discussed in this [Github issue](https://github.com/hyperium/tonic/issues/196), though that seems outside the scope of this assignment. 
