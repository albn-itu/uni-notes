---
title: Block Cipher
tags: [ encryption, cipher ]
date: 2022-09-14
---

See also: [[Symmetric Encryption]]

# Block Cipher
## Security
A block cipher is secure if has a good pseudorandom permutation function.

## Informal definition of pseudorandom permutation
The output of a secure cipher cannot be distinguished from a random permutation.

## Problems
The key has to be the same lengh of the message. The solution to this is to generate a permutation of the key, to fit the size of the plaintext. 

The key can only be used once since the same key encrypting the same plaintext, will result in the same ciphertext. This is fixed by some random vector that is added to the key. This is called the Initialization vector. 

## Confusion
Make the connection between ciphertext and the key opague.

## Diffusion
Flipping a single bit of the plaintext produces a flipping of half of the bits in the ciphertext
