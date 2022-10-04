---
title: Polymorphism
tags: [ types ]
date: 2022-09-29
---

# Polymorphism
A polymorphic type is a type of many forms, which may have many multiple type instances

## Type generalization and scheme
If f has type $(\alpha -> int)$ and $\alpha$ appears nowhere else the type is generalized to the *type scheme* written $\forall \alpha.(\alpha \rightarrow int)$.

## Type specialization
The instantiation of a type.

## Type inference
Functions have static types, but they are not explicit. Types are generalized as much as possible. To the point where they may be able to be any type.

## Restrictions
Only let bound variables and functions can have a polymorphic type

A paramaters type is never polymorphic
```fs
let f g = g 7 + g false
```
The above is invalid as g cannot be both types at once.

A functions is never polymorphic in its own body.


