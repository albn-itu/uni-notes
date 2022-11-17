---
title: Message Authentication Codes
tags: [ encryption ]
date: 2022-09-14
---

See also: [[Block Cipher]]

# Message Authentication Codes (MAC)
Goal: Integrity and authenticity, this does not provide confidentiality though.

Takes a message and a key to generate a MAC tag. This allows a reciever to compute the MAC tag and check if they are the same. This verifies the sent message is the same as the recieved one.

The genius thing here is that you need the message and the key to generate the tag. This blocks the attacker from computing the tag, even if he can change the message.

## HMAC
Take the message. Run a mac algorithm on it, and append the tag to the message. Send the whole thing, then compute the mac tag on the message (without the tag) and compare to the remaining message.


