# High Performance Game Programming Exam Notes

[[toc]]

## Terminology (Week 1)

- DOD: Data Oriented Design
- ECS: Entity Component System
- ECB: Entity Command Buffer
- OOP: Object Oriented Programming
- DOTS: Data Oriented Technology Stack
- Packages: Additional functionality for Unity projects
- AOS: Array of Structs
- SOA: Structure of Arrays
- Blittable types: Types that have a fixed memory layout and can be copied directly in memory. They have the same representation in managed and unmanaged memory. Examples include primitive types (int, float, etc.) and structs that only contain blittable types. One dimensional arrays of blittable types are also blittable.

## ECS (Week 1)

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

## Data Oriented Design (Week 1)

- Layout data for efficient caching and memory usage.
- Allows for efficient SIMD processing.
- Usually implemented with the ECS architecture.
- It's all about the data, how it's stored, accessed and processed.
- Focusing on understanding the data is a key part of DOD. Undestand the hot paths and how data flows through the system.

### Pros and cons

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

### Quick history

- Formally defined in 2009 by Noel Llopis. Been around for much longer.
- Popularized for game development with the PS3 and its multi-core architecture.
- Primarily used for large scale games or complex simulations.
- Becoming more and more mainstream as hardware improves and game complexity increases. And the demand for better performance increases.

## Data Driven Design (Week 1)

- Focuses on designing systems that are driven by data.
- Uses external data sources to define behavior and configuration. 
- For example an RPG game where stats and abilities are defined in data files rather than hardcoded.

## Data Driven Programming (Week 1)

- Focuses on writing code that is flexible and adaptable to changes in data.
- Updates when data changes rather than requiring code changes.
- For example the Unity UI.

## OOP (Week 1)

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

## DOTS (Week 1 and 3)

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

## CPU and Memory (Week 1)

- A CPU is a processing unit. Put simply it just executes instructions.
- Memory is where data is stored for the CPU to access.
- CPUs are getting much faster than memory every year.
- This creates a bottleneck as the CPU has to wait for data to be fetched from memory.
- Therefore it's important to design systems that minimize memory access and maximize cache usage.
- Its also important to design systems that can take advantage of multiple cores and threads, as single core performance is no longer increasing at the same rate as multi-core performance.

## Computer Architecture (Week 2)

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

## Von Neumann Architecture (Week 2)

- A proposal for a computer architecture where the CPU and memory are separate components.
- The proposal consists of:
    - Memory: Stores both data and instructions.
    - Arithemtic Logic Unit (ALU): Performs arithmetic and logical operations.
    - Control Unit: Fetches instructions from memory and decodes them.
    - The CPU: Consists of the ALU and Control Unit.
    - (Modern) Busses: Connects the CPU and memory to carry signals, data and addresses.
- The Von Neumann bottleneck is the limitation on throughput caused by the separation of CPU and memory. We simply cannot move data fast enough between the two.
- In this architecture we do sequential fetching of instructions and data from memory, every time it should be used. This often takes much longer than the CPU needs to execute the instruction.

## Harvard architecture (Week 2)

- A computer architecture where the CPU has separate memory for instructions and data.
- This allows for simultaneous fetching of instructions and data, which can improve performance.
- Modern CPUs often use a modified Harvard architecture, where the CPU has separate caches for instructions and data.

## CPU (Week 2)

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

## Memory (Week 2)

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

### Cache

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

## AOS vs SOA (Week 2)

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

## Locality (Week 2)

- Temporal locality: The principle that a recently referenced item are likely to be referenced in the near future.
- Spatial locality: The principle that items located close to a recently referenced item are likely to be referenced in the near future.

## Threads and cores (Week 2)

- A core is a physical processing unit within a CPU.
- A thread is a virtual processing unit that can be scheduled to run on a core. Threads are used to handle multiple tasks concurrently inside the same core.
- Modern CPUS can have multiple threads per core (e.g. Intel's Hyper-Threading).

## Parallelism vs Concurrency (Week 2)

- Parallelism: Doing multiple things at the same time. Requires multiple cores.
    - Example: Updating multiple game objects simultaneously on different cores.
- Concurrency: Structuring a program as overlapping tasks, even if they share the same core.
    - Multiple tasks can be in progress at the same time, but not necessarily executing simultaneously.
    - Usually interleaved on a single core.
    - Example: Playing music while loading a level in the background.

## Compilers and Auto-vectorization (Week 2)

- A compiler translates high level code (e.g. C#) into low level machine code that the CPU can execute.
- Modern compilers can perform optimizations to improve performance, including auto-vectorization.
- Auto-vectorization: 
    - The process of converting scalar operations (operating on single data points) into vector operations (operating on multiple data points simultaneously) using SIMD instructions.
    - Auto-vectorization looks for patterns such as sequential arrays with no hidden dependencies and no hidden branching.
- Intrinsics:
    - Special functions that map directly to SIMD instructions.
    - Used to manually write vectorized code.
    - These are harder to write and maintain than auto-vectorized code, but is worth it for performance critical code.

## GPU (Week 2)

- A GPU (Graphics Processing Unit) is a specialized graphics processor designed to process thousands upong thousands of operations in parallel.
- Originally designed for rendering graphics, but now also used for computing tasks (GPGPU).
- GPUs have a different architecture than CPUs, with many more cores (hundreds to thousands) that are optimized for parallel processing. They are however not as flexible as CPUs for general purpose computing.
- The weakness of the GPU is:
    - Limited by memory bandwidth between the CPU and GPU.
    - Higher latency for individual operations.
    - Less flexible than CPUs for general purpose computing.
    - Bad at handling branching and irregular tasks.

### SIMT

- SIMT: Single Instruction Multiple Threads.
- How GPUs implement parallelism.
- A single instruction is executed by multiple threads simultaneously. NVidia calls these threads "warps", while AMD calls them "wavefronts", and are typically 32 or 64 threads respectively.
- For efficiency the threads are executed in lockstep, meaning they all execute the same instruction at the same time.
- Essentially a GPU is a massive SIMD machine, where each thread operates on its own data. Its very good at handling large datasets with the same operations but worse at handling irregular tasks.

## Some consoles (Week 2)

- Playstation 1:
    - Limited graphics capabilities.
    - Problems with floating point precision.
- XBOX 360:
    - Slow HDD caused long load times.
    - Became a cinematic tool.
- Switch:
    - Hardware limitations compared to other consoles.
    - Porting games to Switch requires optimization and adaptation to the hardware constraints.
    - Good at stylized graphics rather than photorealism.
- PS3:
    - Complex architecture with the Cell processor.
    - Difficult to develop for, but allowed for high performance if optimized correctly.
    - Required a deep understanding of the hardware to fully utilize its capabilities.

## Jobs (Week 3)

- Unity has historically been single threaded.
- The Job system allows for easy multi-threading in Unity.
- Jobs are small units of work that can be scheduled to run on multiple threads.
- The jobs are queued up and executed by a pool of worker threads.
- Unless explicitly specified jobs are not guaranteed to finish on the same fram as they were queued.
- Jobs are not exclusive to DOTS, they can be used with traditional Monobehaviour based Unity projects as well.

## GameObject (Week 3)

- Traditionally a C# class.
- Always has a Transform component.
- Can be a child of another GameObject.
- Drawbacks:
    - Is a managed object and can therefore not be burst compiled.
    - Are garbage collected
    - Poor memory layout leading to cache misses.
- Can be converted to ECS data by baking them.

## Sub Scenes (Week 3)

- A different scene type that has an authoring container that automatically converts GameObjects to ECS entities at edit/play/build time.

## Entities (Week 3)

- The core building block of ECS.
- Literally just an index and a version number.
- Cannot be parented without special components.
- Can have any number of components attached to them, but not more than one of each type.
- The set of components attached to an entity defines its archetype.

### Archetype

- Entities with the same set of components share the same archetype.
- Entities with the same archetype are stored together in memory in chunks.
- When adding or removing components from an entity, it changes its archetype. This is called a structural change.
- Structural changes are expensive operations as they require moving the entity to a different chunk in memory.

### Entity Manager

- Central API for creating, destroying and managing entities and components.
- Everything done in Entity Manager is a structural change.

## Managed vs Unmanaged Value vs Reference Types (Week 3)

- Managed types:
    - Code that runs under the .NET runtime.
    - Garbage collected.
    - Exception handling, reflection, etc. is handled by the runtime.
    - Examples: Classes, strings, arrays, etc.
- Unmanaged types:
    - Code that runs outside the .NET runtime directly on the operating system level
    - Not garbage collected.
    - No exception handling, reflection, etc.
    - C# is primarily a managed language, but can also be used to write unmanaged code using the `unsafe` keyword or interacting with unmanaged APIs like Unity ECS.
- Blittable types: 
    - Types that have a fixed memory layout and can be copied directly in memory. 
    - They have the same representation in managed and unmanaged memory. Meaning they dont have to be marshalled when passing between managed and unmanaged code.
    - Examples: primitive types (int, float, etc.) and structs that only contain blittable types. One dimensional arrays of blittable types are also blittable.
- Value types:
    - Stored directly in memory.
    - Passed directly by value, meaning a copy is made when passing to a method or assigning to a variable.
    - This also means that changes made to a value type in a method do not affect the original value, and must be copied back if needed.
- Reference types:
    - Stored as a reference (pointer) to the actual data in memory.
    - Passed by reference, meaning only the reference is copied when passing to a method or assigning to a variable.

## Components (Week 3)

- General Purpose Components:
    - The data containers in ECS.
    - Is a struct
    - Must only contain blittable types, such that it stays a blittable type itself.
    - Implements `IComponentData` interface.
- A tag component is a component with no data, used to mark entities for queries. It still changes the archetype of the entity.
- Class components:
    - Used to store managed data in ECS.
    - Is a class
    - Can contain non-blittable types.
    - Implements `IComponentData` interface.
    - Slower and less efficient than general purpose components due to garbage collection and indirection.
    - Can only be used on the main thread, not in jobs.
- Dynamic Buffer components:
    - Used to store variable length arrays of data in ECS.
    - Is a struct
    - Must only contain blittable types, such that it stays a blittable type itself.
    - Implements `IBufferElementData` interface.
    - Stored in chunks like other components, but can grow and shrink dynamically.
    - Accessed via a special API.

### Baking

- Used to serialize editor data into binary data used in ECS at runtime.
- Converts GameObjects and MonoBehaviours into ECS entities and components.
- Can have different usage flags for what data to include in the bake.

## Systems (Week 3)

- The logic units in ECS.
- A data transformation that operates on entities and components.
- Shouldn't hold any state, all state should be stored in components.
- Is a partial struct implementing `ISystem` interface.
- Contains `OnCreate`, `OnDestroy` and `OnUpdate` methods.
- Uses queries to find the relevant entities and components to operate on.
- The order in which systems run can be controlled using attributes and system groups.
    - By default unity creates a `World` and a set of predefined system groups in that world:
        - InitializationSystemGroup
        - SimulationSystemGroup
        - PresentationSystemGroup
    - Systems can be added to these groups or custom groups or custom worlds. You can for example create a separate world for the client and the server in a multiplayer game.
    - You can force a system to run before or after another system using the `[UpdateBefore(typeof(OtherSystem))]` and `[UpdateAfter(typeof(OtherSystem))]` attributes. 
    - Or simply add the system to a specific system group using the `[UpdateInGroup(typeof(SystemGroup))]` attribute.

### Queries

- Idiomatic Foreach:
    - A normal C# foreach loop that iterates over entities and components.
    - Runs on the main thread
    - Uses the `SystemAPI.Query` method.
    - A query essentially searches for a specific archetype of entities based on the components specified in the query.
- Multiple types of query keywords:
    - `WithAll`: Requires all specified components to be present.
    - `WithAny`: Requires at least one of the specified components to be present.
    - `WithNone`: Requires none of the specified components to be present.

## Entity Command Buffer (Week 3)

- A way to queue up structural changes to be executed later.
- Used to avoid structural changes during system updates, which can cause performance issues and bugs.
    - You can also not make structural changes inside jobs, or to an entity that is being iterated over in a query.
- Much like the Entity Manager, all changes made using an ECB are structural changes.

## Collections (Week 3)

- Safe unmanaged versions of common data structures, such as List (NativeList), Array (NativeArray), Dictionary (NativeHashMap), etc.
- Can be used inside jobs and burst compiled code.
- Have safety checks to enforce thread safety and memory safety.
- Must be disposed of manually to avoid memory leaks.
- Must be allocated in unmanaged memory using an allocator:
    - `Allocator.Temp`: Only last for a single frame.
    - `Allocator.TempJob`: Lasts for the duration of the job, but at most 4 frames.
    - `Allocator.Persistent`: Lasts until manually disposed of.
    - `state.WorldUpdateAllocator`: Lasts for the duration of the world update, automatically disposed of at the end of the update.
- The safety system can be disabled if one KNOWS that the work is safe, as the checks might throw errors in some complex scenarios.

## Math (Week 3)

- Unity Mathematics package provides a set of optimized math types and functions for use in DOTS.
- Supports scalar and vector types.
- Designed for high performance and compatibility with the Burst compiler, such that it can be auto-vectorized and use SIMD instructions.
- `math` should therefore be preffered over `MathF` for performance critical code.

## Multithreading (Week 4)

### Thread safety

- Ensuring that shared data is accessed in a way that prevents race conditions and data corruption. And that behaviour is predictable.
- This is done by synchronization mechanisms that ensure that threads write the same data at the same time.
- Race conditions occur when the outcome of a program depends on the timing of events, such as the order in which threads execute. This can lead to unpredictable behaviour and bugs that are hard to reproduce.
- A data race occurs when 2 instructions from different threads access the same memory location, at least one of these accesses is a write and there is no synchronization that is mandating any particular order among these accesses.
- Types of synchronization mechanisms:
    - Locks: Ensures exclusive access to shared data. In most cases only one thread can hold a lock at a time. (There are some exceptions like reader-writer locks)
        - Deadlocks can occur when two or more threads are waiting for each other to release a lock, causing a standstill.
    - Atomic operations: Operations that are guaranteed to be completed without interruption. Examples include incrementing a counter or setting a flag. As these operations execute in one indivisible step, a different thread cant see the data in an intermediate state.
        - The Unity Jobs system uses these.
    - Immutability: Data that cannot be changed after it is created. This eliminates the need for synchronization, as threads can safely read immutable data without worrying about it being modified by another thread.
- The jobs system uses dependencies to ensure thread safety. Ensuring that a job that writes to a component finishes before another job that reads or writes from the same component starts.

### Jobs

- Unity's way of doing multithreading.
- A job is a partial struct that implements the `IJobEntity` interface.
- Jobs use arguments to its `Execute` method to define what components it operates on. 
    - Essentially generating a query behind the scenes.
    - A job only executes on one entity at a time, but multiple instances of the job can run in parallel on different entities.
    - You can also specify some attributes such as `WithNone` to further filter the query.
    - The keywords `ref`, and `in` are used to specify if the component is read-write or read-only respectively.
- Jobs are scheduled to run on worker threads using the `Schedule` or `ScheduleParallel` methods:
    - `Schedule`: Schedules the job to process whole chunks per thread. 
    - `ScheduleParallel`: Splits each chunk into batches of 64 entities and distributes these batches across multiple threads. Each batch becomes its own task. Therefore multiple threads can work on the same chunk at the same time.
         - Needs `ChunkIndexInQuery` when making structural changes.

#### Dependencies

- Jobs can have dependencies on other jobs to ensure thread safety.
- Unity creates a dependency graph of jobs based on the specified dependencies.
- There is also a dependency graph between the systems. This is `state.Dependency` in the system.
    - This can be used when scheduling a job.
- One can define multiple jobs in a system and then make them depend on each other, by applying the dependency from one job to the next. This ensures the first job finishes before the next one starts.
- If jobs operate on completely different components, then ECS runs them in parallel automatically.

### Sync points

- Points where the code has to wait for the completion of all jobs scheduled so far.
- Usually caused by structural changes as these can only be done on the main thread.
- Can be bypassed using ECB to queue up structural changes to be executed later. This actually reduces the number of sync points, caused by changes, to a single one.
- Other sync points include:
    - Accessing component data directly from the Entity Manager.
    - Calling `Complete` on a job handle.

## Performance budgets (Week 4)

- A performance budget is a target for how much time a specific task or system should take to execute.
- In game development this is usually FPS and frame time measured in miliseconds.
- In the budget one has to contain: code, rendering, physics, sound, input, networking, etc.
- Usual performance budgets:
    - 30 FPS = 33.3 ms per frame
    - 60 FPS = 16.6 ms per frame
    - 90 FPS = 11.1 ms per frame (minimum for VR)
    - 120 FPS = 8.3 ms per frame
- Generally measure in ms as this gives a better sense of how much time is available for each task, and as FPS is  not linear.

## Profiling (Week 4)

- The process of analyzing and monitoring the performance and behaviour of a program to identify performance issues.
- Involves measuring various metrics such as CPU usage, memory usage, frame rate, etc.
- Profiling tools are typically instrumentation or sample based:
    - Instrumentation based:
        - Inserts special instructions (marks) into the source code or binary that record performance data when executed. 
        - Provides detailed information about specific functions and code paths, but can introduce overhead and affect performance.
    - Sample based:
        - Periodically samples the program's state at regular intervals to collect performance data.
        - Less intrusive and has lower overhead, but provides less detailed information about specific functions and code
- Unitys profiler is instrumentation based.
- Apart from the profiler unity also provides:
    - Frame Debugger: Allows you to step through the rendering process frame by frame to see how each draw call is executed.
    - Profile Analyzer: A tool for analyzing and visualizing profiling data collected from the Unity Profiler. Can also compare multiple profiling sessions to see how performance has changed over time.
    - Memory Profiler: A tool for analyzing memory usage in Unity projects. Helps identify memory leaks and optimize memory usage.
    - Project Auditor: A static analysis tool that scans your Unity project for potential issues and provides recommendations for improving performance and code quality.

## Frame lifecycle (Week 4)

- On each frame:
    - Input is processed.
    - Game logic is updated (CPU calculates).
    - Physics simulation is updated (CPU calculates).
    - Animation is updated (CPU calculates).
    - Rendering is prepared (CPU sends draw cals via the render thread to the GPU).
    - Rendering is executed (GPU draws to the screen).

## CPU Bound vs GPU Bound (Week 4)

- A game is usually either CPU bound or GPU bound. To advance performance one must identify which one it is and optimize accordingly.
- CPU Bound:
    - The CPU is the bottleneck in the system.
    - The CPU can be the bottleneck in several ways:
        - Game logic: The CPU is spending too much time updating game logic, such as AI, physics, etc. This happens on the Main thread or the Worker threads.
        - Draw calls: The CPU is spending too much time preparing draw calls for the GPU. This happens on the Render thread.
    - These usually cause CPU bottlenecks:
        - Script updates
        - Garbage collection
        - Physics calculations
        - Camera culling and rendering
        - Poor draw call batching
        - UI updateds
        - Animation
    - To optimize:
        - Batch draw calls
        - Reduce script complexity
        - Reduce expensive operations in update loops
        - Offload big calculations to the GPU
        - Use better algorithms or data structures
        - Use more efficient memory access patterns (DOD)
    - Look for:
        - `Gfx.WaitForGfxCommandsFromMainThread`
        - `WaitForJobGroupID`
- GPU Bound:
    - The GPU is the bottleneck in the system.
    - The GPU is spending too much time rendering frames.
    - These usually cause GPU bottlenecks:
        - High screen resolution
        - High texture resolution
        - Complex shaders
        - High polygon count
        - Too many objects being rendered
        - Global illumination and post-processing effects
        - Ambient occlusion
        - Anti-aliasing
    - To optimize:
        - Reduce screen resolution
        - Reduce texture resolution
        - Minimize the number of objects being rendered (culling, LODs, etc)
        - Reduce the amount of data sent to the GPU
        - Eliminate or tune expensive post-processing effects
        - Simplify shaders
    - Look for:
        - `Gfx.WaitForPresentOnGfxThread`

