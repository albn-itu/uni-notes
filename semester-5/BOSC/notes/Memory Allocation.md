---
title: Memory Allocation
tags: [ term, data ]
date: 2022-11-01
---

# Memory Allocation

## Allocator
Allocator maintains a collection of variable sized blocks, known as the heap.

**Explicit**

Application allocates and frees space. Fx. the `malloc` package in C.

**Implicit**

Application allocates, but does not free. That's the job of the garbage collector.

## malloc

- `malloc(size_t size)` - Returns a pointer to a memory block of the given size
- `free(void *p)` - Returns the block pointed at by `p` to available memory
- `calloc` - `malloc` but initializes allocated block to zero.
- `realloc` - Changes size of previously allocated block
- `sbrk` - Used internally by allocators to grow or shrink the heap.
- `aligned_alloc(size_t alignment, size_t size)` - Multiple alignment allocation


