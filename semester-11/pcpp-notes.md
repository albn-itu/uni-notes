[[toc]]

# PCPP Notes

## Concurrency (Week 1)

- Doing more than one computation at a time
- Hardware matters
    - Not all CPUs have multiple cores
    - Hyper-threading
    - Cache levels
    - The GPU is massively parallel
- The general CPU is MIMD (Multiple Instruction, Multiple Data)
- Motivations for concurrency include:
    - Performance by fully exploiting Hardware
    - Hidden stuff such as one app not blocking another, and the multiple thousands of processes running on a computer
    - Dealing with multiple events happening at once (e.g., user input, network messages, etc)
- It is important to distinguish between the concept of concurrency and the language/hardware details used to implement it
    - Abstractions are stuff like streams and cordination
    - While concrete implementations are locks, monitors, semaphotes, messages, java threads, callbacks etc.

### Common concurrency problems (Week 1)

- The Pets in the Yard problem
    - Multiple pets (threads) want to play in the yard (critical section)
    - Only one pet can be in the yard at a time (mutual exclusion)
    - Pets should eventually get to play in the yard (no starvation)
    - Pets should not get stuck waiting forever (no deadlock)
- The Producer-Consumer problem
    - A producer thread produces data and puts it in a buffer
    - A consumer thread takes data from the buffer and processes it
    - The buffer has a limited size
    - The producer must wait if the buffer is full
    - The consumer must wait if the buffer is empty

#### Readers-Writers problem (Week 2)

- Consider a shared data structure where threads may read and write
- Many readers can read as long as no writers are writing
- Only one writer can write at a time, and no readers can read while a writer is writing
- This cannot be solved with simple locks, as they do not distinguish between readers and writers, leading to potential starvation of writers if there are many readers.
- Can be solved using monitors:
    - First define the state of the montior:
        - `readers`: number of active readers
        - `writer`: boolean indicating if a writer is active
        - `lock`: a lock to protect the monitor state
        - `condition`: a condition variable to signal waiting threads
    - Then define the methods for readers and writers:
        - `readLock()`: acquire the lock, wait if a writer is active, increment the number of readers, release the lock
        - `readUnlock()`: acquire the lock, decrement the number of readers, signal waiting threads if there are no more readers, release the lock
        - `writeLock()`: acquire the lock, wait if there are active readers or a writer, set the writer flag to true, release the lock
        - `writeUnlock()`: acquire the lock, set the writer flag to false, signal waiting threads, release the lock
- This ensures that readers and writers are properly synchronized
- But it's unfair to writers, as they may starve if there are many readers
    - A solution is to set the writer flag when a writer is waiting, preventing new readers from entering until the writer has finished

## Threads in java (Week 1)

- A thread is a stream of program statements (instructions) that are exectuted sequentially
- Several threads can be executed concurrently
- Each thread works at its own pace and ahas its own local memory
- Threads can communicate via shared memory
- Threads on the same core are sequential, but can interleave. (This is still concurrency, as we are still doing 2 tasks at once.)
- Threads on different cores can run in parallel.
- Defined in Java by extending the `Thread` class or implementing the `Runnable` interface. The `run` method contains the code to be executed by the thread.
- Stuff defined on the class is shared memory, stuff defined in the `run` method is local memory.
- The `start` method is used to start the thread, which calls the `run` method in a new thread of execution.
- The `join` method is used to wait for a thread to finish execution.
- You can also define a new thread using a lambda expression, e.g.:
```java
  Thread t = new Thread(() -> {
      // code to be executed by the thread
  });
  t.start();
```
- A thread can be in one of several states: new, ready, running, blocked, or terminated.
    - New: The thread has been created but not yet started.
    - Ready: The thread is ready to run but is waiting for the CPU to be available.
    - Running: The thread is currently executing.
    - Blocked: The thread is waiting for a resource (e.g., I/O operation, lock) to become available.
    - Terminated: The thread has finished execution.
    - Threads switch between Ready, Running, and Blocked states during their lifecycle.
- Threads are by default non-deterministic, meaning the order of execution is not guaranteed.
    - This is due to the scheduler, which decides which thread to run at any given time.
    - Parallelization code should be written with this in mind.
- Benefits:
    - Improved performance on multi-core systems.
    - Better resource utilization.
    - Asynchronous programming is simplified to a synchronous style.
    - Thread-per-client model for servers makes it easier to handle multiple clients.
    - More responsive user interfaces, as each element can run in its own thread.
- Downsides:
    - Increased complexity in program design and debugging.
    - Potential for race conditions and unsafe access to shared resources.
    - Risks of deadlocks, livelocks, and starvation.
    - Performance overhead due to context switching and synchronization.

### Interleavings (Week 1)

> Use the syntax: <thread>(<step>) to denote a step executed by a thread.

- An interleaving is a possible sequence of execution of the instructions from multiple threads.
- For example, if we have two threads T1 and T2, each with the steps:
    - T1: A1, A2
    - T2: B1, B2
- Possible interleavings include:
    - T1(A1), T1(A2), T2(B1), T2(B2)
    - T2(B1), T2(B2), T1(A1), T1(A2)
    - T1(A1), T2(B1), T1(A2), T2(B2)
    - T2(B1), T1(A1), T2(B2), T1(A2)

### Thread safety (Week 1)

- Definition: A class is thread-safe if it behaves correctly when accessed from multiple threads, regardless of scheduling or interleaving, with no additional synchronization required from calling code.
- Classes are thread safe if they:
    - Use synchronization to protect shared mutable state.
    - Are immutable (state cannot change after construction).
    - Are stateless (do not maintain any state).

## Race conditions and data races (Week 1)

- A race condition occurs when the result of the execution depends on the order of the interleaving of threads.
- A data race occurs when two more threads access the same shared memory location concurrently, and at least one of the accesses is a write.
- Not all race conditions are data races, and not all data races result in race conditions.

## Synchronization (Week 1)

### Critical Sections (Week 1)

- A critical section of a program is a section of code that only one thread can execute at a time.
- Useful when protecting against race conditions.
- This forms the mutual exclusion property which states that: "No two threads can be in their critical sections at the same time."
- To solve the mutual exclusion problem, we need to ensure:
    - Mutual Exclusion: No two threads can be in their critical sections at the same time.
    - Absence of deadlock: Threads should eventually exit the critical section, such that other threads can enter.
    - Absence of starvation: Every thread that wants to enter its critical section should eventually be able to do so. (This one isn't always possible.)

### Atomicity (Week 1)

- An operation is atomic if it appears to be indivisible, i.e., it either happens completely or not at all.
- A common example of a non-atomic operation is incrementing a variable:
```java
x = x + 1;
```
- This operation can be broken down into three steps:
    1. Read the value of `x` from memory.
    2. Add 1 to the value.
    3. Write the new value back to memory.
- If two threads execute this operation concurrently, they may read the same initial value of `x`, leading to lost updates and incorrect results.

### Locks (Week 1)

- Mutual exclusion can be implemented using locks.
- A lock is a synchronization primitive that ensures only one thread can hold the lock at a time.
- In Java, locks can be implemented with the `Lock` interface.
    - Calling `lock()` acquires the lock, blocking if necessary.
    - Calling `unlock()` releases the lock. If there are threads waiting for the lock, one of them will be signalled to wake up and acquire it.
- Simply wrap the critical section with `lock()` and `unlock()` calls.
- This ensures mutual exclusion, but does not guarantee absence of deadlock or starvation.
- To *attempt* to avoid deadlock, its a great idea to wrap the code in a try-finally block to ensure the lock is always released:
```java
lock.lock();
try {
    // critical section
} finally {
    lock.unlock();
}
```
- If you don't do this and an exception is thrown in the critical section, the lock will never be released, causing deadlock.

#### Intrinsic Locks (Week 2)

- One can also use the `synchronized` keyword, which protects a block of code or method with a lock associated with the object or class. This is an intrinsic lock.
- Every object in Java has an intrinsic lock associated with it.
    - Technically its a monitor, since it has a condition variable.
- Can also be used on static methods, which uses the class's static intrinsic lock.
- These locks use `wait()`, `notify()`, and `notifyAll()` for condition variables.

### Monitors (Week 2)

- A monitor is a structured way of encapsulating data, methods and synchronization in a single construct.
- A monitor consists of:
    - Internal state (data)
    - Methods (procedures). All methods in a monitor are mutually exclusive (ensured via locks), and can onyl access internal state.
    - Condition variables, which are queues where the monitor can put threads to wait for certain conditions to be true.
        - Condition variables support two operations:
            - `await()`: Releases the monitor lock and puts the thread to sleep until signalled.
            - `signal()`: Wakes up one waiting thread (if any) on the condition variable.
            - `signalAll()`: Wakes up all waiting threads on the condition variable.
        - When threads wake up they acquite the monitor lock immediately before resuming execution.

### Fairness (Week 1 and 2)

- Locks can be fair or unfair.
- In this course, fairness refers to the absence of starvation.
- A fair lock ensures that threads acquire the lock in the order they requested it (FIFO).
- An unfair lock does not guarantee any particular order, which can lead to starvation for some threads.
- Fair locks can have higher overhead due to the need to maintain a queue of waiting threads.
- In Java, the `ReentrantLock` class can be created as fair or unfair by passing a boolean parameter to its constructor.
- Fairness is also important to ensure predicatable behavior in concurrent programs.

### volatile variables (Week 2)

- The `volatile` keyword in Java is used to indicate that a variable's value may be changed by different threads.
- Its a form of weak synchronization.
- When a variable is declared as `volatile`, it ensures that:
    - Reads and writes to the variable are directly done to main memory, not cached in CPU caches
    - Changes made by one thread to a `volatile` variable are immediately visible to other threads.
    - Changes made to the volatile variables flush registers and low level caches to the main memory, and reload them from main memory when read.
    - The variables cannot be reordered.

### Things to avid (Week 1)

- Busy waiting: Continuously checking for a condition to be true, which wastes CPU resources and memory bus traffic. (Github safe sleep is a great example of this)
- Memory contention: When multiple threads try to access the same memory location, leading to performance degradation due to cache invalidation.
- Not synchronizing reads, as it may lead to visibility issues.

## Common hardware and programming language concurrency issues (Week 2)

### The memory hierarchy (Week 2)

- Modern computers have a memory hierarchy to balance speed and cost.
    - Registers: Fastest, smallest, and most expensive memory, located inside the CPU.
    - Cache: Small, fast memory located close to the CPU. Typically has multiple levels (L1, L2, L3) with decreasing speed and increasing size. Only L3 is usually shared between cores, which is the first point in this hierarchy where multiple cores can see the same data.
    - Main memory (RAM): Larger and slower than cache, but faster than secondary storage.
    - Storage (e.g., SSD, HDD): Largest and slowest memory, used for long-term storage.
- Data is moved between these levels to optimize performance.
- Caches are organized into cache lines, which are blocks of contiguous memory (typically 64 bytes).
- When a CPU core accesses a memory location, the entire cache line containing that location is loaded into the cache.

### Visibility (Week 2)

- When data is not synchronized between threads, then it may be in one cores cache but not in another cores cache. And thus may not be visible to other threads.
    - This is a hardware optimiazation, that we have to be mindful of when writing concurrent code.
- Such problems occur when there are no synchronization actions between threads.
- Synchronization actions (like acquiring/releasing locks, volatile reads/writes) ensure visibility of shared data between threads.
- Without proper synchronization, a thread may read stale data from its cache, leading to incorrect behavior.

### Reordering (Week 2)

- In the absence of data dependencies or synchronization actions, both the compiler, virtual machine and the CPU may reorder instructions to optimize performance. 
- As such, write accesses can seem to happen before read accesses, even if the code is written in the opposite order. Or writes may appear to happen in a different order than they were written.
- This can lead to unexpected behavior in concurrent programs if threads rely on a specific order of operations.
- Most progamming languages include these optimizations.
- Synchronization actions cannot prevent the reordering of instructions within a single thread, but they can prevent reordering across threads.

## Publication and escape (Week 2)

- Publication refers to the process of making an object accessible outside its current or intended scope
- Escape refers to the situation where an object is published when it shouldn't be. Can happen when:
    - An object is assigned to a static field
    - Return from a non-private method
    - Pass to a method in another class
    - Add to a public data structure
- Safe publication can be achieved through:
    - Initializing an object in a static initializer
    - Storing a reference to it in a `volatile` field or an `AtomicReference`
    - Storing a reference to it in a final field of a properly constructed object
    - Storing a reference to it in a field that is properly guarded by a lock

