---
title: Symmetric Encryption
tags: [ concept, encryption, definition ]
date: 2022-09-14
---

# Symmetric Encryption
## Goal
Confidentiality

## Definition
The same key as the one that was used to create a ciphertext by encryping a plaintex shall be used to decrypt the ciphertext back as the plaintext.

## Why
Perfomance is great, especially compared to something like RSA.

## Why not
You have to transfer the key, so an attacker could simply listen in and get that key.

## How to actually use it
Use a much more secure, but slow, encryption scheme like RSA to transfer the key. By doing this we still have to do the slow computation but only once, and we ensure the key is securely transferred. For optimal security a new key should be used every once in a while, and transferred securely again.

## Examples
- Caesar cipher
- AES
- Blowfish
- Skipjack
