---
title: Context-free grammars
tags: [ concept ]
date: 2022-09-15
---

# Context-free grammars
## Definitions
### Yields
A string $u$ yields a string $v$ if we can apply a grammar rule to $u$ and get $v$

We write $u => v$

### Derives
A string $u$ derives a string $v$ if there is a sequence $U_1,U_2,...,U_k$ with $k>=1$, where $u=u_1, v=u_k$ and $u_1=>u_2=>...=>U_k$.

The sequence is called a derivation

We write $u=>v$

### Leftmost and righmost derivation
A leftmost derivation of a string is a deivation in which, at each step, the leftmost variable is replaced with a string.

A rightmost derivation of a string is a derivation in which, at each step, the rightmost variable is replaced with a string.

#### Example
Using the grammar $S -> SS | aSb | bSa | e$

Find the left and righmost derivations of abab.

Leftmost would be $S->SS->aSbS->abSabS->ababS->abab$

Rightmost would be $S->SS->SaSb->SabSab->Sabab->abab$

### Ambiguity
Some grammars provide more than one way to derive a string.

One can for example create abab multiple ways with $S->SS|aSB|bSa|e$

#### Ambiguous grammar
A grammar is ambiguous if its language contains a string that has more than one leftmost derivation under that grammar.

#### Inherently ambiguous language
A language is inherently ambiguous if every grammar for that language is ambiguous
