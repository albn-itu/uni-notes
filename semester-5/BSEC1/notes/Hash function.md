---
title: Hash function
tags: [ mechanism, encryption ]
date: 2022-09-14
---

# Hash function
Common building block of security mechanisms.

## Definition
A function $\mathcal{H}$ that takes and arbitrary block of data and returns a fixed-size bit string.

## Cryptographic Hash functions
A cryptographic hash function needs:
- Pre-Image resistance
- Second pre-image resistance
- Collision resistance: 

### Industry standards
Currently used, but being deprecated: SHA2. It's currently being replaced by SHA3. There is currently not attack agains SHA2, but it's being replaced before one is found, just to be extra sure.

## Application
Storing passwords. A hash function is one way, so it allows us to never actually have to know the password, we just have to hash the input and test it against the stored password. Problematically this allows us to see if 2 users have the same passsword.

The problem above is fixed with salting.
