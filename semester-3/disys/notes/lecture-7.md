

# Lecture 8 - Consensus

## Redundancy

The act of having multiple systems to do the same task, this secures agains failures.



## The consensus problem

- Each process $P_i$ proposes a value from a set D
- Eac process $P_i$ evenetually sets decision value $d_i$
- The protocol must satisfy
  - Termination: each $p_i$ sets its $d_i$
  - Agreement: Each correct $p_i$ chooses the same $d_i$
  - Integrity: If correct processes all proposed the same value, this value is the $d_i$
- Failures: 



## Consensus algorithms

- Dolev-Strong
- Paxos
- Raft
- ZYB



## Byzantine Generals

- Only one process, the commander, proposes a value
- Agreement: Correct processes must agree on some value
- Integrity: If the commander is correct, they always agree on his value



- A byzantine fault is a corrupt node
  - Created by hacking or equivalent
- In the event of a byzantine failure, if there is only 2 nodes there is no way to reach consensur

## FLP result





## CAP Theorem



