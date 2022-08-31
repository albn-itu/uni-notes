---
title: temporary
tags: [ tmp ]
---

# Lecture 1 - Computer systems
| Reading | C-Programming | Assignment |
| ------- | ------------- | ---------- |
| 2h      | 6h            |            |

## Quick fire terminology
- Executable object programs are a series of instructions. Its file is sometimes referred to as executable object files. On windows these usually end in .exe
- Assembly language is a mostly human readable, but very simple language. Which is essentially just a series of instructions.
  - The instructions match machine operations pretty closely and mostly boils down to.
    - Load, copy byte or a word from memory into a register
    - Store, copy byte or a word from a register into memory
    - Operate, copy contents from 2 register, perform an operation and store the result in a register.
    - Jump, Ectract a word from the instruction itself and copy that word into the program counter, thereby overwriting the program counter.
    - When writing to a register or memory, the data already in that spot is overwritten.
- Why understand compilers?
  - To be able to optimize our code to what the compiler creates.
  - To understand what the linker does, and why it causes so many fucking errors.
  - Avoiding security issues. Understand what the compiler does so we know what code comes out, so we know how our code creates security issues.
- Caches are a series of increasingly smaller storage devices which are orders of magnitude faster to read from than memory. Frequently accessed data can be stored here to avoid being bottlenecked by storage devices and memory.
  - The register file is first, and is right next to the processor. Its FAST
  - Then comes the L1 cache which is nearly as fast
  - The L2 cache is next, and might be up to 5 times slower than L1, but still much faster than memory, its also way smaller though. Bigger than L1 tho.
  - Newer systems may have an L3 cache too which is slower than L2, but bigger.
  - Main memory is next, its alot bigger but also molassis slow in comparison.
  - Lastly is physical storage as an HDD or SDD. These may as well be a truck stuck in tar in comparison. But its insanely large too, even compared to memory.
  - In some cases there is also secondary storage, such as webservers or distributed file sytstems, which may be even larger but are slowed down significantly as they still have to do this entire process remotely and then transfer the result over the network to our system.
  - One thing to keep in mind is that physical storage is the only storage that will survive if power is lost. The cache and memory will disappear if power is lost.
- Operating system, is a piece of software that provides APIs to access hardware, such as the cache and the memory. It usually handles the entire storage stack, so we as developers usually dont get to manipulate the cache directly. Most of the time we dont need to either so thats nice. 
- Drivers, are software that wraps the specific details of hardware to provide an API that the operating system can then use to interact with the hardware. These apis are usually wrapped again with some extra logic to provide the API that developers use. Combining these systems means that when building software for an operating system it should work regardless of hardware.
- Process, is an illusion of a running program. Multiple processes can run at the same time on the same system, the operating system then interleaves the instructions when sending them to the CPU. This provides the illusion that the program is executed instruction by instruction, while in practice there may have been thousands of instructions from a different program executing in between ours.
- Context, the environment that a process runs in. Fx one process may create some memory addresses while a different may create some others. We shall not mix these, therefore they are wrapped in a context that is linked to the process. These are written to memory or even disk when processing a different process instructions. This is called context switching and can be quite cumbersome, therefore its important to limit context switching.
  - It actually maps pretty well to real life, where context switching can be a cumbersome process, that completely bottlenecks our productivity. Which is why meetings should be limited, and not split actual work being done.
- Threads, are an execution unit. A process can have many threads using the same data and code. One should be very careful with threads as they may cause race conditions.
- Virtual memory, an illusion to the process that it has exclusive use of the main memory. The view that a process has of the memory is called the Virtual Adress Space. The VAS at the top level contains the OS code and data, while the bottom most level is the user process code and data.
  - Program code and data. Code begins at the same fixed address for all processes. Then followed by the data, starting with global data. Areas are determined by the binary executable.
  - Heap. Expanding area of memory. It changes size based on the run time variable that are created by the software.
  - Shared libraries. An area of memory where shared, unchanging, code such as the C standard library is saved. Can this be used by multiple processes?
  - Stack. Used to implement function calls. Expands and shrinks depending on how many functions are running. Each function call expands the stack.
  - Kernel virtual memory. Top level of the address space. Applications cannot read or write to this area. They must invoke the kernel to do such operations
- Amdahls Law, states that speeding up a part of a system, only has an effect on the system proportional to its significance and how much it was sped up.
- Concurrency, is parallel execution. Here are some models:
  - Thread level. A processor can have many cores, a so called multicore processor. A multicore processor has multiple executing cores, each with its own L1 and L2 cache, they then share L3 cache. 
    - Hyperthreading. Extremely complicated system that involves having multiple copies of program counters and register files, but only one copy of other hardware, such as the arithemtic unit. This allows the CPU to process multiple threads on a cycle by cycle basis, instead of taking 20.000 cycles to switch threads.
  - Instruction level. Most modern processors can handle multiple instructions pr cycle. Most can handle 2-4 pr cycle, some up to 100. Early processors sometimes to 3-10 cycles to execute a single instruction. This enhancement is due to a bunch of clever tricks.
  - Single-Instruction, Multiple-Data (SIMD), special hardware that allows one instruction to cause multiple operations to happen in parallel. Such as adding 8 pairs of single-precision floating-point numbers in parallel. Mostly used for image, sound and video data processing.
- Superscalar, a processor that can execute more than one instruction pr cycle.
- Abstractions, a way to make life easier for others.
