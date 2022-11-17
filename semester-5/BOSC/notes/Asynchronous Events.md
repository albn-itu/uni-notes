---
title: Asynchronous Events
tags: [ term, data ]
date: 2022-10-04
---

# Asynchronous Events
Caused by events exertnal to the processor. These are indicated by setting the processors interrupt pin. Handler returns to "next" instruction. Aka the instruction to return to after doing the current one.

## Asynchronous Events: Exceptions
An exception is a transfer of control to the OS in response to some event.

## Interrupt vector
The first 32 slots are reserved. 33-127 is OS-defined, 128 is system calls and 129-255 is also OS-defined.

## Synchronous Events
Events caused by the result of an instruction executing.

- Traps
  Intentional
- Faults
  - Unintentional but possibly recoverable. Otherwise goes to abort
- Abort
  - Unintentional and unrecoverable


