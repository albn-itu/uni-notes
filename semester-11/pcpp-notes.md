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
    - A good solution must be deadlock free and avoid starvation

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

## Synchronization (Week 1 and 4)

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

### Semaphores (Week 4)

- A semaphore is a synchronization primitive that allows some amount of threads to access the same cricital section.
- The consist of:
    - An integer value called the capacity, or permits in Java. It is the initial number of available accesses.
    - Two operations:
        - `acquire()`: Decreases the number of available permits by 1. If no permits are available, the thread is blocked until a permit becomes available.
        - `release()`: Increases the number of available permits by 1. If there are threads waiting for a permit, one of them is signalled to wake up and acquire the permit.
- Semaphores can be used to implement resource pools, where a limited number of resources are available for use by multiple threads

### Barriers (Week 4)

- A barrier is a synchronization primitive that blocks at a certain point until a set number of threads reach that point.
- They consist of:
    - An integer value called the parties, which is the number of threads that must reach the barrier before any of them can proceed.
    - A method called `await()`, which is called by each thread when it reaches the barrier. The thread is blocked until the specified number of threads have called `await()`.
- Java provides the `CyclicBarrier` class to implement barriers. It resets after the threads have been released, allowing it to be reused.

### Things to avoid (Week 1)

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

## Memory models (Week 3)

- A memory model defines the behavior of memory operations in a concurrent environment.
- We do this because reasoning at the hardware level is not adequate:
    - Hardware may be different across systems
    - Different hardwares have different sets of instructions
    - Different architectures treat memory consistency differently
- The combination of compilers and runtime environments introduce further complexity:
    - Compilers may reorder instructions for optimization
    - Runtime environments may introduce additional layers of abstraction
    - Code rewriting may occur, fx branch elimination and loop unrolling
- Memory models ensure non-paradoxical behavior in concurrent programs:
    - This can be done by being sequnetially consistent, meaning that the intra-thread order of operations is preserved and that operations appear to occur at the same time across threads. (See section on sequential consistency)
- The Java Memory Model (JMM) defines the behavior of memory operations in Java programs.
- It defines the rules for how threads interact through memory and how changes made by one thread become visible to other threads.
- Definitions in the java memory model:
    - Actions: 
        - An action is a pair t(o) where t is a thread and o is an operation performed by that thread.
        - There are 3 types of actions:
            - Variable access: Read/write accesses on program variables
            - Synctionization actions: Lock/unlock operations, volatile variable accesses, thread start/join operations
            - Other actions: e.g., I/O operations
        - We use the notation `m(o)` to denote actions on the main thread and `t<number>(o)` to denote actions on other threads.
    - Executions:
        - A sequence of actions
    - Program order:
        - The intra-thread order of execution of the actions performed by a thread.
        - Given two actions a1 and a2 performed by the same thread t, then a1 occurs before a2 in the program only if a would be performed before a2 when t is executed sequentially.
    - Happens-before order:
        - Given two actions a and b in an execution we say that a happens-before b (denoted a -> b) if:
            - Program Order Rule: Each action in a thread happens-before every action in that thread that comes later in the program order.
            - Monitor Lock Rule: An unlock on a monitor lock happens-before every subsequent lock on that same monitor lock. (Locks and unlocks on explicit `Lock` objects have the same memory semantics as intrinsic locks)
            - Volatile Variable Rule: A write to a volatile field happens-before every subsequent read of that same field. (Note: Reads and writes of atomic variables have the same memory semantics as volatile variables)
            - Thread Start Rule: A call to `Thread.start()` on a thread happens-before every action in the started thread.
            - Thread Termination Rule: Any action in a thread happens-before any other thread detects that thread has terminated (either by successful return from `Thread.join()` or by `Thread.isAlive()` returning false).
            - Interruption Rule: A thread calling `interrupt()` on another thread happens-before the interrupted thread detects the interrupt (either by having `InterruptedException` thrown, or invoking `isInterrupted()` or `interrupted()`).
            - Finalizer Rule: The end of a constructor for an object happens-before the start of the finalizer for that object.
            - Transitivity: If A happens-before B, and B happens-before C, then A happens-before C.
        - Happens-before is a partial order among the actions in an execution.
    - Synchronization order:
        - A total order among the synchronization actions of an execution.
        - Must satisfy two properties:
            - Must be consistent with mutual exclusion
            - Must be consistent with happens-before
        - Due to the non-deterministic nature of thread scheduling, there may be multiple valid synchronization orders for a given execution
        - Every execution has at least one valid synchronization order
    - Well-formed executions:
        - An execution is well-formed if it is consistent with:
            - Program order
            - Synchronization order
            - Happens-before order
        - Java is guaranteed to produce only well-formed executions.
- Correctness of the Java Memory Model:
    - Conflicting actions:
        - A pair of actions that could lead to concurrency issues.
        - "Given actions a, b in an execution, we say that actions a, b are conflicting iff they are accesses on the same (non-volatile) variable and at least one of them is a write access"
        - By definition, volatile variable accesses are never conflicting actions.
        - This is essentially the definition of a data races, we can define it as:
            - Given actions a, b in an execution, there exists a data race between a and b iff:
                - a and b are conflicting actions
                - a and b are not ordered by happens-before (i.e., neither a -> b nor b -> a)
    - Correctly synchronized programs:
        - A program is correctly synchronized if there are no data races
        - The JMM guarantees that all executions of a correctly synchronized program are sequentially consistent.
    - Visibility:
        - If action a happens-before action b, then the effects of a are visible to b.
        - This means that if a writes to a variable and b reads that variable, then b will see the value written by a (or a later value).
        - This is crucial for ensuring that threads can communicate correctly through shared memory. And to ensure predictable behavior in concurrent programs.

### Reasoning using the JMM (Week 3)

1. Identify actions and categorize them as variable accesses, synchronization actions, or other actions.
2. Define action pairs from the program order rule $HB_{po}$.
3. Define actions pairs from synchronization actions $HB_{sync}$.
4. Define possible synchronization orders.
5. Determine differences in happens-before pairs in the different synchronization orders.
6. For each of the differences, define the happens-before order set associated to the executions corresponding to each synchronization order.

- Use the happens-before order to:
    - Find data races
    - Show absence of data races and correct synchronization
    - Predict the value of variables in the executions of the program.

## Program correctness (Week 4)

- A program is correct if and only if it satifies its specification.
- A specification defines the expected behavior of a program.
- Reasoning about correctness is difficult, as it quickly gets out of hand with many threads and interleavings.
- It is easier to separately analyze parts of the code and then combine them in safe ways. In OOP we can focus on analysing the correctness of classes/objects.

### Thread-safe classes and programs (Week 4)

- A class is thread-safe if and only if no concurrent execution of method calls or field accesses result in data races on the fields of the class.
- We can extend this definition to programs: A program is thread-safe if and only if it is data race free.
- To analyze whether a class is thread safe we must ensure that for any concurrent execution of method calls or field access (where at least one write is involved) that actions are ordered by happens-before.
- The elements to identify/consider are:
    - Class state
    - Escaping
    - Publication
    - Immutability
    - Mutual exclusion

#### Class state (Week 4)

- Uncontrolled concurrent access to shared mutable state is the main cause of date races.
- The state of a class includes the fields defined in the class
- The goal is to ensure that concurrent accesses to the class state are properly synchronized.
- To help achieve this, follow the following guidelines:
    - Methods should only manipulate the class state. Avoid accessing global state, state of other classes, or the state of the parent classes.
    - Methods should avoid using references to objects as parameters, as we cannot ensure the happens-before relation on a referenced object. Instead use copies.
- Keep in mind that these are guidelines, not strict rules. Breaking them does not necessarily make a class not thread-safe, but it makes it harder to reason about its correctness.

#### Escape and publication (Week 2 and 4)

- Exposing (or publication) refers to the process of making an object accessible outside its current or intended scope
- It is important to not expose class fields, otherwise threads may use them without proper synchronization.
- Escape refers to the situation where an object is exposed when it shouldn't be.
    - Thus, we can't enforce the happens-before relation on such fields.
    - For primitive fields, we can simply make them private. In which case they cannot escape.
    - For reference fields, we must ensure that the referenced object does not escape.
- Safe publication requires that initialization of an object is completed before it is made accessible to other threads. AKA, the initialization happens-before the publication.
    - This can lead to visibility issues if not done correctly.
    - Safe publication can be achieved for:
        - Primitive types:
            - Declare them as volatile
            - Declare them as final (if they are only assigned once during construction)
            - Initialize them as the default value (if the default value is acceptable)
            - Declare them as static (if they are shared across all instances)
            - Use an atomic class
        - Reference types:
            - Declare them as final
            - Initialize them as the default value (if the default value is acceptable)
            - Declare them as static (if they are shared across all instances)
            - Use the AtomicReference class
    - These techniques enforce the happens-before relation between initialization and publication. Because:
        - Volatile writes happen-before subsequent volatile reads
        - Final and static fields are guaranteed to initialize before any thread can access them (unless the constructor leaks them)
        - The default initialization happens-before any thread can access the object
        - Atomic classes provide atomic read/write operations with proper memory visibility guarantees

#### Immutability (Week 4)

- An immutable object is an object whose state cannot be modified after it is constructed.
- Immutable objects are inherently thread-safe, as there are no mutable states
- An immutable class is one whose instances are immutable objects.
- To ensure thread-safety of an immutable class, we must ensure that:
    - No fields can be modified after publication (i.e., no setters and final)
    - Objects are safely published
    - Access to the objects state does not escape (i.e., no references to mutable objects)

#### Mutual exclusion (Week 4)

- Whenever shared mutable state is accessed concurrently, we must ensure mutual exclusion.

#### Putting it all together (Week 4)

- To analyze whether a class is thread-safe, follow these steps:
    1. Identify the class state (fields)
    2. Ensure that fields do not escape
    3. Ensure safe publication
    4. Wherever possible, define fields as immutable
    5. For mutable fields, ensure mutual exclusion on all accesses
- If all these steps are satisfied, then the class is thread-safe.

#### Instance confinement (Week 4)

- Instance confinement is a technique, in which a non-thread-safe object is wrapped in a thread-safe class, such that the non-thread-safe object is only accessed by one thread at a time.
- This is useful when we want to use a non-thread-safe class in a concurrent program.

#### Extending thread-safe classes (Week 4)

- When extending a thread-safe class, we must ensure that the subclass is also thread-safe.
- But it can be very useful, as it then inherits the intrinsic lock of the parent.

## Properties of concurrency (Week 5)

- Safety: Something bad will never happen.
- Liveness: Something good will eventually happen.

## Testing (Week 5)

> Use JUnit 5 for testing examples.

- Testing concurrent programs is difficult due to the non-deterministic nature of thread scheduling and interleavings.
- The goal of testing is to find bad interleavings that lead to incorrect behavior. (counter-example)
- Remember: Testing can show the presence of bugs, but not their absence.
- It is not guaranteed that a test will find the bug all the time due to the non-deterministic nature of concurrency.
- When testing concurrent programs, test it sequentially first to ensure basic functionality.

### Counter-examples (Week 5)

- A counter-example for a safety property is a finite prefix of a (possibly infinite) interleaving that leads to a violation of the property.
    - Example: A finite interleaving of traffic light controller that leads to both lights being green at the same time.
- A counter-example for a liveness property is an infinite interleaving that never leads to the desired outcome.
    - Example: An infinite interleaving where the traffic light controller never changes the light from red to green.

### Types of concurrency tests (Week 5)

- Functional tests:
    - Focusses on testing that a program behaves correctly according to its specification, regardless of the interleaving.
- Performance tests:
    - Focusses on measuring the performance of a program under different interleavings and workloads.

### Testing strategies (Week 5)

- Precisely define the property to be tested.
    - Use assertions to check the property during the test.
    - Example: "after N threads have incremented a counter M times each, the final value of the counter should be N * M"
- If you are testing multiple implementations, ensure that they all satisfy the same specification. Can be achieved using interface definitions.
- Concurrent tests require setup for starting and running multiple threads.
    - Maximize contention by having threads start at the same time, to avoid sequential execution.
        - Achieved by maximizing the number of concurrent threads
        - Use a barrier to synchronize the start of all threads
    - You may have to define thread classes to encapsulate the behavior of each thread.
- Maxmimze the chances of finding bad interleavings by running the test multiple times.
    - Can be done easily using `@RepeatedTest` in JUnit.
- Use argument generation to test a wide range of inputs.
- Yield the CPU to increase the chances of context switches and different interleavings.
    - Can be done using `Thread.yield()` in Java.
- Use sleep to introduce delays and increase the chances of different interleavings.
    - Can be done using `Thread.sleep(milliseconds)` in Java.

### Example test of BoundedBuffer (Week 5)

- We want to test the BoundedBuffer class, which is a thread-safe implementation of a bounded buffer.
    - Producers may put elements into the buffer as long as it is not full. Otherwise they block until space is available.
    - Consumers may take elements from the buffer as long as it is not empty. Otherwise they block until elements are available.
    - It is implemented as a circular array.
    - Synchronization is implemented using monitors (intrinsic locks and condition variables).
        - Condition 1: notFull - signalled when space becomes available
        - Condition 2: notEmpty - signalled when elements become available
- We want to test the following properties:
    - After several threads put and take the same number of elements, the sum of the put elements and the sum of the taken elements should be equal.
        - Formally: After N producer threads have put $x_1,\dots,x_M$ elements, and several consumer threads have taken $y_1,\dots,y_M$ elements, it must hold that $\sum_{i=1}^{M} x_i = \sum_{i=1}^{M} y_i$
    - A consumer may take more than one element if the buffer is not empty.
    - A producer may put more than one element if the buffer is not full.
- The test:
    - Define two atomic integers to keep track of the sum of put and taken elements.
    - Define a barrier to synchronize the start of all threads.
    - Define producers with how many elements to put.
    - Define consumers with how many elements to take.
    - Define producer threads, which wait at the barrier, then put elements into the buffer and update the sum of put elements.
    - Define consumer threads, which wait at the barrier, then take elements from the buffer and update the sum of taken elements.
    - Start all threads and wait for them to finish.
    - Assert that the sum of put elements equals the sum of taken elements.
    - Repeat the test multiple times to increase the chances of finding bad interleavings.
    - Repeat the test with different buffer sizes and number of threads to test different scenarios.

### Testing frameworks (Week 5)

- JUnit: A popular testing framework for Java. Supports annotations for defining tests, setup, and teardown methods. Provides assertions for checking conditions.
- jcstress: A specialized framework for testing concurrent programs in Java. It allows defining tests with multiple threads and provides tools for analyzing the results.
- Coyote: A framework for systematic testing of concurrent programs. It explores different interleavings and checks for violations of specified properties.

### Testing for deadlocks (Week 5)

- A deadlock occurs when two or more threads are blocked forever, waiting for each other to release resources.
- The classic example is waiting for locks in a circular manner. For example in in the dining philosophers problem.
- Testing for deadlocks is difficult and often impossible, as it requires exploring all possible interleavings.
- Deadlock freedom is a liveness property, so we need to look for infinite interleavings that lead to deadlock.
- To test for deadlocks we must be able to characterize the state in which a deadlock occurs.
    - This can be done by defining a timeout for the test. If the test does not complete within the timeout, we assume a deadlock has occurred, but it's not guaranteed.
    - Another approach is to use thread dumps to analyze the state of the threads and identify deadlocks.
- The better way is formal verification

### Formal verification (Week 5)

- Formal verification is the process of mathematically proving the correctness of a program with respect to its specification.
- It treats programs and properties as mathematical objects, and uses logic and proof techniques to reason about them, it can be done:
    - Manually: By writing formal proofs or using proof assistants.
    - Automatically: By using model checkers, SAT solvers, SMT solvers, static verification, symbolic execution, etc.
- Formal verification is great, but with large programs we run into the state explosion problem, where the number of possible states grows exponentially with the number of variables and threads. Making it infeasible to analyze all possible states.
- We can try an use the same model as for thread-safety, where we analyze classes/objects separately and then combine them in safe ways.
- A plus of formal verification is that it can be implemented into static analysis tools that can be run as part of the build process, and thus catch bugs early.

#### Model checking (Week 5)

- Model checking is an automatic technique for verifying finite-state concurrent systems.
- It does so transforming the program into finite-state models that encapsulate all possible interleavings.
- Properties are specified in some type of logic: Linear Temporal Logic (LTL), Computation Tree Logic (CTL), First-Order Logic (FOL), etc.
- The model and the properties are typically expressed in the same langauge, so that it can be automatically checked.
- Has been very successful in hardware verification.
- JavaPathFinder is such a model checker for Java programs.

## Performance testing (Week 5)

- Performance testing is the process of measuring the performance of a program.
- Can sometimes be extended from functionality tests.
- Should reflect real-world usage as much as possible.
- Select appropriate metrics to measure, such as throughput, latency, resource utilization, etc.
- Select appropriate workloads to test, such as number of threads, size of data, etc.
- Can be different kinds:
    - Raw run time: Measure the time taken to complete a task.
    - Responsiveness: The time taken for an individual operation to complete.
        - Sometimes acceptable to have high average responsiveness if the variance is low
    - Throughput: The number of operations completed in a given time period.

### Common pitfalls (Week 5)

- Garbage collection: Can introduce pauses and affect performance measurements.
    - Is usually unpredictable, so try to minimize its impact by running tests multiple times and averaging results.
    - Can be solved by:
        - Ensuring its not running, add: `-verbose:gc`, if you see GC activity, then restart the test. (Nearly impossible in longer tests)
        - Forcing GC to run at predictable points using `System.gc()`. (Not guaranteed to work). This is useful to reflect real-world performance.
- JIT compilation: The Just-In-Time compiler can optimize code at runtime, leading to performance variations.
    - To minimize its impact, run tests multiple times to allow the JIT compiler to optimize the code before measuring performance.
    - Can be verified with `-XX:+PrintCompilation` flag.
    - Can be solved by:
        - Using `-Xint` to run in interpreted mode only. (Not recommended, as it does not reflect real-world performance)
        - Running a warm-up phase before measuring performance, to allow the JIT compiler to optimize the code.
- Unrealistic workloads: Using workloads that do not reflect real-world usage can lead to misleading performance measurements.
    - Ensure that the workloads used in tests are representative of real-world scenarios.
- Unrealistic contention: Using too few or too many threads can lead to unrealistic contention levels.
    - Ensure that the number of threads used in tests reflects real-world usage patterns.
- Unrealistic hardware: Running tests on hardware that does not reflect the target environment can lead to misleading performance measurements.
    - Ensure that the hardware used in tests is representative of the target environment.
    - (See bethesda monitor issue)
- Dead code elimination: The compiler may optimize away code that does not affect the program's observable behavior.
    - Could theoretically optimize the benchmark iteself away. (Seems unlikely in practice)
    - To prevent this, ensure that the results of operations are used in a way that affects the program's observable behavior.
    - For example, store results in a volatile variable or print them to the console.
    - "Writing effective performance tests requires tricking the optimizer into not optimizing away your benchmark as dead code. Requires every computed result be used somehow - in a way that doesn't require synchronization or substantial computation"

## Additional testing methods (Week 5)

- Static analysis: Analyzing the code without executing it, to find potential concurrency issues, bugs, and code smells.
    - Tools: FindBugs, PMD, Checkstyle, SonarQube, etc.
- Dynamic analysis: Analyzing the program during execution, to find concurrency issues, bugs, and performance bottlenecks.
    - Tools: Java VisualVM, YourKit, JProfiler, etc.
- Code review: Reviewing the code manually to find potential concurrency issues, bugs, and code smells.
    - Can be done in pairs or in groups.
    - Can be done using tools like GitHub, GitLab, Bitbucket, etc.

## Non-blocking synchronization (Week 6)

- Non-blocking synchronization is a technique for achieving concurrency without using locks.
- To be non-blocking, a synchronization mechanism must satisfy one of the following progress properties:
    - Wait-free: A method of an object implementation is wait-free if every call to the method is guaranteed to complete in a finite number of steps, regardless of the actions of other threads.
        - My operations are guaranteed to complete in a bounded number of steps.
    - Lock-free: A method of an object implementation is lock-free if executing the method guarantees that some method call wil complete in a finite number of steps, regardless of the actions of other threads.
        - This means that at least one thread makes progress, but not necessarily all threads.
    - Obstruction-free: A method of an object implementation is obstruction-free if, from any point after which it executes in isolation, it is guaranteed to complete in a finite number of steps.
        - This means that a thread makes progress if it executes in isolation, but not necessarily when other threads are executing concurrently. 
- Wait-freedom implies lock-freedom, which implies obstruction-freedom.
- Non-blocking synchronization IS NOT busy wait, because threads cannot be blocked forever, even in obstruction-free completion is guaranteed if a thread executes in isolation.

### Progress conditions in general (Week 6)

- From strongest to weakest:
1. Wait-freedom (maximal, independent, nonblocking)
   - Every thread makes progress
   - Works on any platform
2. Lock-freedom (minimal, independent, nonblocking)
   - Some thread makes progress
   - Works on any platform
3. Obstruction-freedom (maximal, dependent, nonblocking)
   - Thread in isolation makes progress
   - Requires contention management
4. Starvation-freedom (maximal, dependent, blocking)
   - Every thread makes progress (if fair scheduling)
   - Can be blocked
5. Deadlock-freedom (minimal, dependent, blocking)
   - Some thread makes progress (if fair scheduling)
   - Can be blocked

## Lock-freedom and lock-free data structures (Week 6)

- Lock-free data structures are concurrent data structures that do not use locks for synchronization.
- They are designed to allow multiple threads to access and modify the data structure concurrently without blocking each other.
- Lock-free data structures provide several advantages over lock-based data structures:

### Hardware support for atomic operations (Week 6)

- Early processors implemented atomic operations entirely to implement mutexes with test-and-set instructions. This is not suitable for implementing lock-free data structures.
- Modern processors, however, provide special instructions for managing concurrent access to shared variables, such as store-condition and compare-and-swap (CAS).

### Compare-and-swap (CAS) (Week 6)

- At the programming language level most languages provide atomic operations through libraries or built-in constructs.
- In java it is `val.compareAndSwap(expected, newValue)`, where `val` is an atomic variable.
- It compares the value of `val` with `expected`. If they are equal, it sets `val` to `newValue`. Otherwise, it does nothing.
    - In both cases it returns the original value of `val`.
- This is translated to `CMPXCHG` instruction or similar by the compiler or runtime.
    - "The CMPXCHG [...] If the values contained in the destination operand and the EAX register are equal, the destination operand is replaced with the value of the other source operand (the value not in the EAX register). [...] For multiple processor systems, CMPXCHG can be combined with the LOCK prefix to perform the compare and exchange operation atomically." 
    - "Intel 64 and IA-32 processors provide a LOCK# signal [...] While this output signal is asserted, requests from other processors or bus agents for control of the bus are blocked [...]"
- CAS is a powerful primitive that can be used to implement lock-free data structures.
- For example, AtomicInteger can be implemented using CAS:
    - To increment the value, we read the current value, compute the new value, and use CAS to update the value. If the CAS fails, we repeat the process until it succeeds.
```java
public int incrementAndGet() {
    int oldValue, newValue;
    do {
        oldValue = value.get();
        newValue = oldValue + 1;
    } while (!value.compareAndSet(oldValue, newValue));
    return newValue;
}
```
- This is called optimistic concurrency, in a nutshell trying to do the operation assuming no other thread is interfering, and if it does, retrying.
- It is non-blocking, with the lock-free property, as at least one thread will make progress.
- In Java atomic classes are provided by the `Atomic*` classes in the `java.util.concurrent.atomic` package.
    - They all follow the same memory semantics as volatile variables.
    - All methods on atomic classes are atomic operations.
- If we would want to set multiple values atomically, we can create an immutable class and use an `AtomicReference` to hold a reference to an instance of that class.
    - To update multiple values, we create a new instance of the immutable class with the new values and use CAS to update the reference.

#### A note on correctness (Week 6)

- Due to the volatile semantics of atomic variables, we can use their visibility semantics to reason about safe-publication.
- However, they are not part of the Java Memory Model, and we can therefore not reason about correctness or thread-safety.
- We can however produce a specification for them, such that we can reason about correctness and thread-safety.
- We can also reason using linearizability, which we will cover in a later section.

#### CAS based locks (Week 6)

- CAS can also be used to implement locks.
- The simplest lock is the try lock implemented using an atomic reference:
    - Simply get a reference to the current thread using `Thread.currentThread()`.
    - Use CAS to set the atomic reference to the current thread if it is null.
    - If the CAS succeeds, we have acquired the lock. Otherwise, the lock is held by another thread.
    - In both cases return whether the CAS succeeded.
    - This is a non-blocking lock.

#### Scalability of CAS (Week 6)

- Pros:
    - Faster than acquiring and releasing locks, as there is no context switching or blocking.
    - An unsuccessful CAS does not cause blocking
- Cons:
    - High contention can lead to many retries, which can degrade performance.
    - Can lead to starvation, as some threads may never succeed in acquiring the lock.
    - High memory bus traffic, as CAS operations require exclusive access to the memory bus.

#### The ABA problem (Week 6)

- The ABA problem occurs when a thread reads a value A from a shared variable, then another thread changes the value to B, and then back to A. When the first thread performs a CAS operation, it sees the value A and assumes that nothing has changed, leading to incorrect behavior.
- This can be solved by using version numbers or timestamps along with the value, so that the CAS operation checks both the value and the version number.
- ITs not a problem in Java as it ensures newly created objects have different references. It's mostly a problem in low-level programming with pointers and without garbage collection.

## Linearizability (Week 7)

- Linearizability is a way to reason about the correctness of concurrent objects.
- Specifications of sequential objects are easy to reason about and are typically expressed in terms of preconditions and postconditions of methods.
- Linearizability allows us to reason about concurrent objects using their sequential specifications.
- Informally we would actually just like our concurrent programs to behave as if they were sequential.
- Notation:
```
A: -| q.enq(x) |-------| p.enq(y) |--->
B: -----| q.deq(x) |------| p.deq(y) |->B: -----| q.deq(x) |------| p.deq(y) |-
```
- Time horizontal: `---` (nothing) or `| action |` (method call)
- Left `|` : method invocation
- Right `|` : response received
- Width: duration

### Sequential consistency (Week 7)

- Recall that in sequential programs operations can be reordered as long as the program result is not affected.
    - As an example take this program: `q.enq(x)` -> `q.deq(x)` -> `q.enq(y)` -> `q.deq(y)`
    - `q.enq(x)` -> `q.enq(y)` -> `q.deq(x)` -> `q.deq(y)` is a valid reordering, as the result is the same.
    - `q.enq(x)` -> `q.deq(y)` -> `q.enq(y)` -> `q.deq(x)` is not a valid reordering, as the result is different.
- For concurrent programs we must define conditions that assert that every thread is behaving consitently with the sequential specification.
- For executions of concurrent objects, an execution is sequentially consistent if:
    - Method calls appear to happen one at a tim in sequential order.
    - Method calls should appear to take effect in program order.
- We can reword this to: A concurrent execution is sequentially consistent if there exists a reordering of  operations that produces a sequential execution where:
    - Operations happen one at a time.
    - Program order is preserved for each thread.
    - The executions satisfies the specification of the object.
- This is not compositional so concurrent executions involving sequentially consitent objects are not necessarily sequentially consistent.

### Linearizability definition (Week 7)

- Linearizability extends sequential consitency by requiring that the real time order of executions is preserved.
- Linearizability extends sequential consitency with another condition:
    - Each method call appears to take effect instantaneously at some point between its invocation and its response.
- We do this by defining linearization points for each method call.
    - A linearization point is a point in time between the invocation and response of a method call where the method call takes effect.
    - It essentially defines when the method call takes effect.

### Linearizable concurrent objects (Week 7)

- Lets extend the property of executions to objects.
- A concurrent object is linearizable if all its concurrent executions are linearizable. (This is hard to prove)
- Linearizability IS compositional, so concurrent executions involving linearizable objects are also linearizable.
- This makes it easier to reason about the correctness of concurrent programs using linearizable objects.
- To show that an object implementation is linearizable we:
    1. Identify the linearization points for each method call.
    2. Argue about the sates of the object at each linearization point.
    3. Show that the reordering of method calls based on their linearization points produces a sequential execution that satisfies the specification of the object.
