---
title: Compilation system
tags: [ concept, system, compilation, code ]
date: 2022-08-31
---

# Compilation system
The compilation system is a sequence of steps that turn the code from human readable code, into instructions that the machine can understand and execute. Each step of the compilation system for C is described below.

## [[Preprocessor]]
Modifies the code according to a series of instructions. In C this could be including via `#include <stdio>.h`. That instruction is, by the preprocessor, replaced with the contents of `stdio.h`.

In C this program is called `cpp`

## [[Compiler]]
Turns the result of the preprocessor into [[Assembly]].

In C this program is called `cc1`

## [[Assembler]]
Turns the Assembly language instructions into machine-language instructions and outputs a binary file. This binary file is either executable or an object file.

In C this program is called `as`

## [[Linker]]
Merges existing compiled code int the binary file. Such as merging the `printf.o` object file, from the standard library, into the executable.

In C this program is called `ld`
