---
title: Perfect Secrecy
tags: [ encryption ]
date: 2022-09-14
---

See also: [[Symmetric Encryption]]

# Perfect Secrecy
Idea: Use the properties of XOR to encrypt and decrypt

Vernam cipher or One-time pad

## Problem
The key needs to be as large as the message. So to stream the Batman (2022) movie, which is 2h and 56 m long (~3h) would take a 9 gb key. Absolutely not possible. Also the key would have to be transferred at the same time. Making it a 18gb transfer to stream it.

Also the key can only be used once because two encrypted messages with the same key can be xor'd together, which will reveal at least 1 bit of the message.

