# High Performance Game Programming Exam Notes

## Week 1: What is Data Oriented Design?

> S: DOD benefits

### Terminology

- DOD: Data Oriented Design
- ECS: Entity Component System
- OOP: Object Oriented Programming
- DOTS: Data Oriented Technology Stack
- Packages: Additional functionality for Unity projects
- AOS: Array of Structs
- SOA: Structure of Arrays
- Blittable types: Types that have a fixed memory layout and can be copied directly in memory. They have the same representation in managed and unmanaged memory. Examples include primitive types (int, float, etc.) and structs that only contain blittable types. One dimensional arrays of blittable types are also blittable.

### ECS

- Is an architectual design pattern.
- Focuses on a clear seperation of data and behavior.
- Is a very composobale way of designing software.
- Unity adds it through the Unity Entities package.
- Stands for Entity Component System:
    - Entity: A unique identifier for an object in the game world.
    - Component: A small data structure holding the data an entity indexes. Only uses blittable types.
    - System: A unit of logic that transforms the data in components. It uses queries to find the relevant entities and components to operate on.
- The advantages are very similar to DOD as ECS is a way to implement DOD:
    - Seperation of data (compoennts) and behavior (systems).
    - Less dependencies between systems, which allows for more flexibliity and reusability.
    - Data and code does not have to be tightly coupled.
    - New logic can be added by creating new systems that operate on existing components.
- Well suited for large simulations and complex games with many entities.

### Data Oriented Design

- Layout data for efficient caching and memory usage.
- Allows for efficient SIMD processing.
- Usually implemented with the ECS architecture.
- It's all about the data, how it's stored, accessed and processed.
- Focusing on understanding the data is a key part of DOD. Undestand the hot paths and how data flows through the system.

#### Pros and cons

- Pros:
    - As DOD is far more efficient with memory and CPU usage it allows for:
        - Longer battery life
        - Smaller file sizes
        - More complex games
        - More modular code
    - Modularity
    - Reusability
- Cons:
    - Harder to learn and understand.
    - More upfront design work required.
    - Harder to debug.
    - Can't rely on traditional OOP design patterns.
    - Can be hard to collaborate on large teams without strict guidelines.

#### Quick history

- Formally defined in 2009 by Noel Llopis. Been around for much longer.
- Popularized for game development with the PS3 and its multi-core architecture.
- Primarily used for large scale games or complex simulations.
- Becoming more and more mainstream as hardware improves and game complexity increases. And the demand for better performance increases.

### Data Driven Design

- Focuses on designing systems that are driven by data.
- Uses external data sources to define behavior and configuration. 
- For example an RPG game where stats and abilities are defined in data files rather than hardcoded.

### Data Driven Programming

- Focuses on writing code that is flexible and adaptable to changes in data.
- Updates when data changes rather than requiring code changes.
- For example the Unity UI.

### OOP

- Designed around objects that encapsulate both data and behavior.
- Pros:
    - Code structure is closer to how humans think about the world.
    - Easy to implement
- Cons:
    - Poor performance due to cache misses and memory fragmentation.
    - Hard to scale for complex systems.
    - Inflexible and hard to change.
    - Reusability is hard to achieve
    - Dependency management is hard.

### DOTS

- A suite of technologies for building high performance games in Unity.
- Includes:
    - ECS
    - Job system
    - Burst compiler
    - Collections package
    - Mathematics Packages
    - Unity NetCode
    - Unity Physics
    - Unity Entities Graphics
- Designed to work together to provide a high performance, scalable and modular framework for game development.

### CPU and Memory

- A CPU is a processing unit. Put simply it just executes instructions.
- Memory is where data is stored for the CPU to access.
- CPUs are getting much faster than memory every year.
- This creates a bottleneck as the CPU has to wait for data to be fetched from memory.
- Therefore it's important to design systems that minimize memory access and maximize cache usage.
- Its also important to design systems that can take advantage of multiple cores and threads, as single core performance is no longer increasing at the same rate as multi-core performance.

## Week 2: Hardware and DOD

> S: Memory patterns used in DOD (Array of Structs vs Structure of Arrays)
> S: Memory layout in Unity ECS (Chunks)
> S: Cache structure and benefits of cache
> S: Threads and cores in modern CPU architecture
> S: Temporal and spatial locality of data
> S: Von Neumann architecture and Von Neumann bottleneck
> Q: What are the differences between Array of Structs (AOS) and SOA (Structure of Arrays) and how do they relate to how memory can be structured in a DOD way?
> Q: How does the cache work in most modern CPU architectures? What are cache hits and misses? 

### Computer Architecture

- A computer is made up of several components:
    - CPU: Central Processing Unit
    - Memory: RAM
    - Storage: SSD/HDD
    - I/O: Input/Output devices
- A CPU is controlled by an instruction set architecture (ISA) which defines the instructions that the CPU can execute.
- A computer is actually a series of complex abstractions, bottom up:
    - Transistors (The silicon itselft)
    - Logic Gates (AND, OR, NOT, etc)
    - Functional Units (ALU, FPU, etc)
    - Execution Units (Pipelines, etc)
    - Microarchitecture (The overall design of the CPU, and how it implements the ISA)(e.g. x86, ARM, RISC-V)
    - ISA (The instruction set the CPU can execute)
    - Operating System (The software that manages the hardware and provides an interface for applications)
    - Programming Languages (The languages we use to write software)
    - Applications (The software we use)
- Most programmers operate at the higher levels at the programming language level. The programming language is eventually compiled down to machine code that the CPU can execute.
- However, we need to understand the lower levels to write high performance code.

### Von Neumann Architecture

- A proposal for a computer architecture where the CPU and memory are separate components.
- The proposal consists of:
    - Memory: Stores both data and instructions.
    - Arithemtic Logic Unit (ALU): Performs arithmetic and logical operations.
    - Control Unit: Fetches instructions from memory and decodes them.
    - The CPU: Consists of the ALU and Control Unit.
    - (Modern) Busses: Connects the CPU and memory to carry signals, data and addresses.
- The Von Neumann bottleneck is the limitation on throughput caused by the separation of CPU and memory. We simply cannot move data fast enough between the two.
- In this architecture we do sequential fetching of instructions and data from memory, every time it should be used. This often takes much longer than the CPU needs to execute the instruction.

### Harvard architecture

- A computer architecture where the CPU has separate memory for instructions and data.
- This allows for simultaneous fetching of instructions and data, which can improve performance.
- Modern CPUs often use a modified Harvard architecture, where the CPU has separate caches for instructions and data.

### CPU

- The CPU is the brain of the computer. It executes instructions and performs calculations.
- Turns input data into output data.
- Most new CPUs have multiple cores, which allows for parallel processing of instructions.
- Each core typically has its own ALU, control unit and registers.
- CPUS function on a cycle basis. On each cycle the CPU fetches data or instructions from memory via an address bus, decodes the instruction, executes it and writes the result back to a register or memory via a data bus.
- A clock speed refers to how many cycles the CPU can perform per second. Measured in Hertz (Hz).
- Modern CPUs also have features like pipelining, out-of-order execution and branch prediction to improve performance, so the clock speed is not the only factor that determines performance:
    - Pipelining: Every part of the cycle can be in flight at the same time. Increasing throughput
    - Superscalar: Can execute multiple instructions per cycle. Usually achieved with pipelining.
    - Out-of-order execution: Can execute a different instruction if the current one is waiting on data. Increasing  utilization, by avoiding stalls.
    - Branch prediction: Predicts the outcome of a branch so the pipeline stays busy. Bad predictions must throw work away, causing stalls.
    - Prefecthing: Predicts what data will be needed soon and fetches it into cache ahead of time, based on access paterns. Works well with SOA.
    - SIMD: Single Instruction Multiple Data. A way for the CPU to execute the same instruction on multiple data points at the same time. Great for DOD as the related data is stored contiguously in memory.

### Memory

- Memory is where data is stored for the CPU to access.
- Memory is measured in 3 main ways:
    - Size: How much data can be stored. Measured in bytes (B), kilobytes (KB), megabytes (MB), gigabytes (GB), terabytes (TB).
    - Bandwidth: How much data can flow from memory to the CPU per second. Measured in bytes per second (B/s), kilobytes per second (KB/s), megabytes per second (MB/s), gigabytes per second (GB/s).
    - Latency: How long it takes for data to be fetched from memory. Measured in nanoseconds (ns), microseconds (µs), milliseconds (ms).
- Memory can be classified into several types. Speed here refers to latency:
    - Registers: The fastest type of memory, located inside the CPU. Used to store data that is being actively used by the CPU.
    - Cache: A small amount of fast memory located close to the CPU. Used to store frequently accessed data.
    - RAM: The main memory of the computer. Used to store data that is not actively being used by the CPU.
    - Storage: The slowest type of memory, used to store data that is not actively being used by the CPU. Examples include SSDs and HDDs.

#### Cache

- A small amount of fast memory located close to the CPU.
- Used to store frequently accessed data.
- Modern CPUs usually have multiple levels of cache:
    - Registers: Located inside the CPU, the fastest type of memory. (Immeasurably fast)
    - L1 Cache: The smallest and fastest cache, located inside the CPU core. (1-2 ns)
    - L2 Cache: Larger and slower than L1, but still much faster than RAM, each core has it's own. (3-4 ns)
    - L3 Cache: The largest and slowest cache, shared between all CPU cores. (10-15 ns)
    - RAM: The main memory of the computer, much slower than the built in cache, but can work as such. (50-60 ns)
- Cache works by storing copies of frequently accessed data from main memory.
- When the CPU tries to access data or an instruction it first checks the cache. If it doesnt find it there, it fetches it from main memory and stores a copy in the cache for future access.
- A cache miss occurs when the CPU tries to access data that is not in the cache. This results in a longer latency as the data has to be fetched from main memory.
- A cache hit occurs when the CPU tries to access data that is in the cache.
- The CPU searches from the smallest and fastest cache to the largest and slowest cache until it finds the data.

- A Cache line is the smallest unit of data that can be stored in the cache. Typically 64 bytes.
- You will always fetch an entire cache line from memory, even if you only need a small part of it. Therefore it's important to design data structures that take advantage of this by storing related data together in memory.

### AOS vs SOA

- AOS: Array of Structures is a data layout patern commonly used in OOP.
    - Each object is stored as a contiguous block of memory.
    - Example: An array of `struct Particle { float x, y, z; float vx, vy, vz; }` would store each particle's position and velocity together.
    - Pros:
        - Easy to understand and use.
        - Good for small datasets or when objects are accessed individually.
    - Cons:
        - Poor cache performance when accessing large datasets, as related data may be scattered in memory.
        - Difficult to parallelize processing of large datasets.
- SOA: Structure of Arrays is a data layout pattern commonly used in DOD.
    - Each attribute of an object is stored in a separate array.
    - Example: An array of `struct ParticlePositions { float[] x; float[] y; float[] z; }` and `struct ParticleVelocities { float[] vx; float[]; vy; float[] vz; }` would store all particle positions and velocities separately.
    - Pros:
        - Better cache performance when accessing large datasets, as related data is stored contiguously in memory.
        - Easier to parallelize processing of large datasets with SIMD.
        - Improves cache hit rates by maximizing locality.
    - Cons:
        - More complex to understand and use.
        - May require more memory due to padding and alignment requirements.

### Locality

- Temporal locality: The principle that a recently referenced item are likely to be referenced in the near future.
- Spatial locality: The principle that items located close to a recently referenced item are likely to be referenced in the near future.

### Threads and cores

- A core is a physical processing unit within a CPU.
- A thread is a virtual processing unit that can be scheduled to run on a core. Threads are used to handle multiple tasks concurrently inside the same core.
- Modern CPUS can have multiple threads per core (e.g. Intel's Hyper-Threading).

### Parallelism vs Concurrency

- Parallelism: Doing multiple things at the same time. Requires multiple cores.
    - Example: Updating multiple game objects simultaneously on different cores.
- Concurrency: Structuring a program as overlapping tasks, even if they share the same core.
    - Multiple tasks can be in progress at the same time, but not necessarily executing simultaneously.
    - Usually interleaved on a single core.
    - Example: Playing music while loading a level in the background.

### Compilers and Auto-vectorization

- A compiler translates high level code (e.g. C#) into low level machine code that the CPU can execute.
- Modern compilers can perform optimizations to improve performance, including auto-vectorization.
- Auto-vectorization: 
    - The process of converting scalar operations (operating on single data points) into vector operations (operating on multiple data points simultaneously) using SIMD instructions.
    - Auto-vectorization looks for patterns such as sequential arrays with no hidden dependencies and no hidden branching.
- Intrinsics:
    - Special functions that map directly to SIMD instructions.
    - Used to manually write vectorized code.
    - These are harder to write and maintain than auto-vectorized code, but is worth it for performance critical code.

### GPU

- A GPU (Graphics Processing Unit) is a specialized graphics processor designed to process thousands upong thousands of operations in parallel.
- Originally designed for rendering graphics, but now also used for computing tasks (GPGPU).
- GPUs have a different architecture than CPUs, with many more cores (hundreds to thousands) that are optimized for parallel processing. They are however not as flexible as CPUs for general purpose computing.
- The weakness of the GPU is:
    - Limited by memory bandwidth between the CPU and GPU.
    - Higher latency for individual operations.
    - Less flexible than CPUs for general purpose computing.
    - Bad at handling branching and irregular tasks.

#### SIMT

- SIMT: Single Instruction Multiple Threads.
- How GPUs implement parallelism.
- A single instruction is executed by multiple threads simultaneously. NVidia calls these threads "warps", while AMD calls them "wavefronts", and are typically 32 or 64 threads respectively.
- For efficiency the threads are executed in lockstep, meaning they all execute the same instruction at the same time.
- Essentially a GPU is a massive SIMD machine, where each thread operates on its own data. Its very good at handling large datasets with the same operations but worse at handling irregular tasks.
