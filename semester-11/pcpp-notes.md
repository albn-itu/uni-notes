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

## Performance measurements (Week 9)

- The process of measuring performance.
- Measurements are key in many sciences and engineering disciplines.
- There are two primary motivations for performance measurements:
    1. To establish what parts of the code are performance bottlenecks, to guide optimization efforts.
    2. To evaluate the impact of optimizations and changes to the code.
- To show how to do performance measurements, and how we avoid pitfalls, we go through the versions of the benchmark functionality in benchmark
    - Mark0: A simple timer on each side of the code to be benchmarked.
        - Essentially useless, as:
            - Really slow
            - May measure JIT compilation
            - Does not account for garbage collection
            - Does not account for dead code elimination
            - Timer resulution may be too low
    - Mark1: Runs the code to be benchmarked multiple times in a loop, and measures the total time taken.
        - Better, but still does not account for garbage collection and other
        - It measures the loop overhead as well.
        - Increasing count of iterations makes the results implausible as it uses the same data over and over again, which may lead to caching effects.
    - Mark2: Actually uses the result from the benchmarks to prevent dead code elimination.
        - Still does not account for garbage collection and other issues.
    - Mark3: Creates a timer for each loop iteration, to minimize the impact of garbage collection and other issues.
        - It doesn't show the average time taken anymore.
        - It's good for showing the distribution of times taken and variations in performance.
    - Mark4: Computes standard deviations on the measurements to show variations in performance.
        - Still does not account for garbage collection and other issues.
        - Should tend to a normal distribution (68 of observations within 1 standard deviation, 95 within 2, 99.7 within 3)
        - This prints the mean and standard deviation of the measurements.
    - Mark5: Adds automatic iteration count adjustments.
        - Starts at 1 iteration, and doubles the number of iterations until the total time taken is at least 0.25 seconds. Is limited to 1 billion iterations.
        - Shows the convergence of mean and standard deviations.
    - Mark6: Generalize to any function using an interface.
        - Only supports the interface defined in the benchmark.
        - Still does not account for garbage collection and other issues.
        - Simple functions are heavily influence by inlining, scheduling etc.
    - Mark7: Move mean and standard deviation calculations out of the loop and only calculate them once at the end.
        - Assumes JIT optimization stabilize eventually.
    - Mark8: Adds problem size params.
        - Adds n and minimum time as parameters to the benchmark function. (n is the amount of times we run the count loop inside the benchmark function)
        - Still has a problem with caching, as it uses the same data over and over again.
    - Mark8.1: Adds setup functions used to initialize data or code that should not be included in the benchmark.
        - Use only for things that take a long time to setup, otherwise it may skew the results.
- When doing performance measurements, there might be times where we have stuff happening that we do not want to benchmark. Fx. Thread creation
    - When measuing threads we are actually measuring:
        1. Creating a thread object
        2. Calculating the hash code of the thread object, to return
        3. Starting the thread
    - A strategy to deal with this is to measure the overhead of the unwanted stuff separately, and then subtract it from the total time taken.
    - We can even split it up so we measure the time taken for each part separately, and then combine them to get the total time taken for the desired operation.
    - Thread work can easily take 72000 ns, while the work itself only takes 650 ns.

### Hints and warnings about performance measurements (Week 9)

- Control your environment:
    - Minimize interference:
        - Shut down external programs
        - Web browsers, Skype, Microsoft Office, OpenOffice
        - Mail clients, virus checkers, iTunes
        - Virtual machines (Virtual PC, Parallels, VMware)
        - Web servers, database servers
        - Windows Update particularly problematic
    - Code preparation:
        - Remove/disable all logging and debugging messages
        - Can consume 90%+ execution time
        - Completely distorts measurements
    - Execution environment:
        - Never measure from IDE (Eclipse, Visual Studio)
        - Use command line
        - IDEs may inject debugging code or consume CPU
    - Power management:
        - Turn off power savings in OS and BIOS
        - Prevent CPU speed reduction mid-benchmark
        - Laptops may slow on battery vs. mains power
        - Desktops may slow with no user activity
    - Compilation:
        - Compile with optimization flags (e.g., `csc /o MyProg.cs`)
        - Without optimization: extraneous no-op instructions
- Be aware of how the platform affects measurements:
    - JVM implementations:
        - Different JVMs (Oracle, IBM) have different performance
        - Statements about "the speed of Java" need large grains of salt
    - Garbage collectors:
        - Java/.NET have several different GCs
        - Very different performance characteristics
    - CPU variations:
        - Different brands (Intel, AMD) have different characteristics
        - Different microarchitectures (Netburst, Core, Nehalem)
        - Different versions (desktop, mobile)
        - Same instruction set (x86) doesn't mean same performance
        - Different microarchitectures marketed under same name (Pentium)
        - Same microarchitecture under different names (Pentium, i3, i5, i7)
        - Note processor model number
        - Rest of system matters: RAM speed, memory bus latency/bandwidth, cache sizes
    - Asynchronous operations:
        - Threads, I/O, GPU calls
        - Ensure actually complete before calling `timer.check()`
        - Use `thread.join()` or similar
- Reflect on your results:
    - Unreasonably fast:
        - May have overlooked something
        - Example: Array never actually allocated in RAM
          - Memory pages just entered in MMU table
          - Assumed to contain zeroes
          - Writing first forces actual allocation
    - Unreasonably slow:
        - Example: Scala Application trait code in constructor
          - JVM didn't optimize
          - Moving to ordinary function: 12× faster

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
    - Scales better
    - Offer liveness guarantees
    - Avoid deadlocks
    - Less scheduling overhead

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

## Scalability (Week 10)

- Some ways to scale is to know how to properly use concurrency to increase performance.
    - Use tasks over threads for better resource management.
        - A Thread creates a lot of overhead as it physically starts a new OS thread.
        - A Task is a unit of work that can be executed by a thread pool, which manages a pool of threads and reuses them for multiple tasks.
    - Thread pools are a good way to manage threads and avoid the overhead of creating and destroying threads.
        - We can then schedule a bunch of tasks to be executed by the thread pool, which will efficiently switch work out as necessary
            - This is great as the tasks may not be be the same size, fx. in prime counting the smaller numbers are faster to compute than larger numbers.
        - There are 2 types of tasks:
            - Runnable: Does not return a value and cannot throw checked exceptions.
            - Callable: Returns a value and can throw checked exceptions.
        - For small enought tasks, then the overhead of scheduling the task may be larger than the task itself, in these cases just run it sequentially on the main thread.
    - There are many kinds of thread pools:
        - ForkJoinPool: A thread pool that uses work-stealing to efficiently execute tasks that can be recursively split into smaller tasks.
        - FixedThreadPool: A thread pool with a fixed number of threads.
        - WorkStealingPool: A thread pool that uses work-stealing to efficiently execute tasks.
    - You can shutdown pools, this does not interrupt running tasks, but prevents new tasks from being submitted.
        - `shutdown()`: Initiates an orderly shutdown in which previously submitted tasks are executed, but no new tasks will be accepted.
        - `awaitTermination(timeout, unit)`: Blocks until all tasks have completed execution after a shutdown request, or the timeout occurs, or the current thread is interrupted, whichever happens first.

### Amdahl's law (Week 10)

- Amdahl's law states that the speedup of a program using multiple processors is limited by the sequential fraction of the program.
- The speedup S is given by the formula:
    - S = 1 / (F + (1 - F) / P)
    - Where F is the fraction of the program that is sequential, and N is the number of threads.
- This means that even if we have an infinite number of processors, the speedup is limited by the sequential fraction of the program.
- Example:
    - If 10% of the program is sequential (F = 0.1), then the maximum speedup is:
        - S = 1 / (0.1 + (1 - 0.1) / P) = 1 / (0.1 + 0.9 / P)
        - As P approaches infinity, the speedup approaches 10.
- This shows that to achieve significant speedup, we must minimize the sequential fraction of the program.
- Amdahl's law assumes a fixed problem size, meaning that the amount of work to be done does not change as we increase the number of processors.

### Loss of scalability (Week 10)

- Starvation loss: Minimize the the time threads are idle waiting for work.
    - Can be caused by load imbalance, where some threads have more work than others.
    - Can be caused by contention, where multiple threads are trying to access the same resource.
- Separation loss: Find a good threshold to distribute work evenly:
- Saturation loss: Minimize the time threads are blocked waiting for resources.
    - Can be caused by locks, where multiple threads are trying to acquire the same lock.
- Braking loss: Stop all tasks as soon as the problem is solved.
    - Can be caused by tasks that are not aware of the global state of the program.
    - Example: In a search problem, if one thread finds the solution, all other threads should stop searching.

## Streams (Week 11)

- Streams are a high-level abstraction for processing sequences of elements.
- They allow for functional-style operations on collections of elements, such as map, filter, reduce, etc.
- Streams can be sequential or parallel.
- Parallel streams allow for concurrent processing of elements in the stream, which can lead to significant performance improvements for large datasets.
- Streams are lazy, meaning that operations on the stream are not executed until a terminal operation is invoked.
    - This is great for memory efficiency, as intermediate results are not stored in memory.
- Streams can be created from various sources, such as collections, arrays, I/O channels, etc.
- Streams can be processed using a pipeline of operations, which can be source, intermediate or terminal.
    - Sources are the starting point of the stream, such as a collection or an array.
        - All java collections have a `stream()` method that returns a sequential stream 
    - Intermediate operations transform the stream into a different stream using operations such as map, filter, etc.
        - They are lazy and do not produce a result until a terminal operation is invoked.
        - Example: `map`, `filter`, `sorted`, `distinct`, `skip`, `limit`, etc.
    - Terminal operations produce a result or a side-effect from the stream, such as collect, count, forEach, etc.
- Example:
    - Take a stream of words
    - The function F discards all words with just one character
    - The function G converts all words to uppercase
    - The function H counts the number of words in the stream
    - This is equivalent to: `H(G(F(words)))`
- Streams may or may not be ordered.
- Parallelization of streams is really easy.
    - Disjoint streams are assigned to different threads for processing.
    - The framework handles the splitting and merging of streams.
    - Streams (if written correctly) are akin to functional programming, and are therefore entirely thread-safe.

### A note on RxJava (Week 11)

- RxJava is a library for composing asynchronous and event-based programs using observable sequences for the Java VM.
- Closely related to streams, but with a focus on asynchronous programming.
- Input elements are obsvervables, which can emit items over time.
- Observers receive notifications from observables when items are emitted.
- Observables can be transformed using operators, similar to stream operations.
- Observables can be subscribed to, which allows for processing of emitted items.
- Unlike streams, an observable (a source) can be subscribed to by multiple observers.
- Backpressure is when a producer emits items faster than a consumer can consume them.
    - RxJava provides mechanisms to handle backpressure, such as buffering, dropping, or sampling items.

## Message passing (Week 12 and 13)

- Message passing is a concurrency model where threads communicate by sending and receiving messages.
- It is an alternative to shared memory concurrency, where threads communicate by reading and writing shared variables
- Message passing is everywhere in distributed systems, where processes communicate over a network.
- Messages are usually recieved in some kind of "mailbox" or "message queue". For the internet each port can be seen as a mailbox.
- Message passing can be assymetric or symmetric.
    - In asymmetric message passing, one thread is the sender and the other is the receiver.
        - On the internet clients and servers are asymmetric, where clients send requests and servers send responses. The server cannot initiate communication, unless the client is also a server (webhooks are a good example of this).
    - In symmetric message passing, both threads can send and receive messages.
- Messages can have many formats. On the internet they are simply string that can then be parsed.

### Actor model (Week 12)

- The actor model is a concurrency model where actors are the fundamental units of computation.
- Actors can only send messages to other actors, and cannot share state.
- An actor is an abstraction of a thread.
- An actor can only execute one of 4 actions:
    - Send a message to another actor.
    - Recieve a message from another actor.
    - Create a new actor.
    - Change its own state (computing)
- Every actor has a unique identifer (address) that other actors can use to send messages to it.
- Actors can only recieve and send finitely many messages. Recieved messages are placed in the mailbox for later processing.
- Sending is non blocking, while receiving is blocking (if no messages are available).
- Do not make assumptions about the order of message delivery.
- The actor model encourages spawning many actors that perform small tasks and communicate via message passing.
    - This is great for building distributed systems, as actors can be distributed across multiple machines.
    - There is of course a limit to how small tasks can be, as the overhead of message passing can be significant. And how many actors can be spawned and still make a difference.

#### Erlang/OTP (Week 12)

- Erlang uses the actor model for concurrency.
- Each Erlang process is an actor.
- Good for building distributed systems.
- Patterns:
    - Define an `init` function to initialize the actor's state.
    - Define a `loop` function to handle incoming messages.
    - Use pattern matching to handle different message types.
    - Use `spawn` to create new actors.
    - Consume messages not recognized by the actor to avoid mailbox overflow.
- `recieve` is used to block and wait for messages.
- `stop` can be used to terminate an actor.
- Remember that it is stateless, so you must pass the state around as parameters to functions.
- The mailbox in Erlang is FIFO, so messages are processed in the order they are recieved.
- Erlang maps perfectly to the actor model:
    - Actor: Module
    - Mailbox address: Process identifier (PID)
    - Message: Any Erlang term
    - State: Function parameters
    - Behavior: `loop` function
    - Create actor: `spawn` function
    - Send message: `Pid ! Message` operator
    - Recieve message: `receive` construct
- Subscriptions can be implemented using message passing.
    - An actor can maintain a list of subscribers (PIDs).
    - When an event occurs, the actor sends a message to all subscribers.
    - Subscribers can unsubscribe by sending a message to the actor to remove their PID from the list.

##### Fault tolerance in Erlang/OTP (Week 13)

- Erlang/OTP has built-in support for fault tolerance.
- Actors are encouraged to fail fast and let other actors handle the failure.
- Actor systems shoud be developed with the assumption that actors will fail, and that the system should be able to recover from failures.
- We only focus on process monitoring for how to handle failures.
    - An actor can monitor another actor using the `monitor` function.
    - If the monitored actor fails, the monitoring actor receives a `DOWN` message.
    - The monitoring actor can then take appropriate action, such as restarting the failed actor or logging the failure.
    - Down can either be normal termination or abnormal termination (crash). Abnormal terminations include a reason for the crash.

##### Load balancing with actors (Week 13)

- Load balancing refers to the process of distributing work evenly across multiple actors.
- One load balancing pattern is Scatter-Gather systems:
    - Scatter-Gather is a commond pattern for distributing work across multiple actors.
    - The scatter actor receives a request and distributes it to multiple worker actors.
    - The amount of actors depends on the load and the nature of the work.
    - The actor types are:
        - Scatterer: Receives requests, splits the computation into smaller tasks, and sends them to gatherer actors.
        - Gatherer: Recieves data from scattrers and combines them into a single result. Then it sends the result to a higher level gatherer.
    - Great for tasks on ranges of numbers.
    - In this case the size of the problem determines the load balancing strategy. This is not always the case.
- Another type of adaptive load balancing is elastic load balancing:
    - Actors can be created and destroyed dynamically based on the load.
    - If the load increases, new actors can be created to handle the increased load.
    - If the load decreases, actors can be destroyed to free up resources.
    - This is great for systems with fluctuating loads, as it allows the system to adapt to changing conditions.

#### Actor model and happened-before (Week 12)

- We can use the happened-before relation to reason about message passing.
- An action a happens-before an action b if:
    - a and b are in the same actor, and a comes before b in the actor's execution order.
    - a is the sending of a message, and b is the receiving of that message.

#### Topology (Week 13)

- The topology of an actor system is the way actors are connected to each other.
- A static topology is one where the connections between actors are fixed. And where actors cannot be created or destroyed.
- Dynamic topology is one where actors can be created and destroyed, and where connections between actors can change.
    - This is more common in real-world systems, as actors can be created and destroyed as needed.
    - Great for load balancing where actors can be created to handle increased load, and destroyed when the load decreases.
- A common worker type is one that only does one thing and then terminates. This ensures a finite number of steps.



# Final notes

## 1. Intro to Concurrency & Mutual Exclusion

> Define and motivate concurrency and mutual exclusion. 
> Explain data races, race conditions, and critical sections.
> Show some examples of code from your solutions to the exercises in week 1.

**Concurrency**: Multiple computations at once. Motivation: performance (exploit HW), non-blocking apps, handling simultaneous events.

**Data Race**: Two+ threads access same memory location concurrently, at least one is a write.

**Race Condition**: Result depends on interleaving order.

**Critical Section**: Code that only one thread can execute at a time.

**Mutual Exclusion Requirements**:
1. No two threads in critical section simultaneously
2. No deadlock (threads eventually exit)
3. No starvation (every thread eventually enters)

**Exercise**: `CounterThreads2Covid.java`

## 2. Synchronization

> Explain and motivate how locks, monitors, and semaphores can be used to address the challenges caused by concurrent access to shared memory.
> Show some examples of code from your solutions to the exercises in week 2.

**Locks**: `lock()` acquires (blocks if held), `unlock()` releases. Use try-finally to ensure release.

**Monitors**: Encapsulate state + methods + synchronization. Methods mutually exclusive via locks.
- Condition variables: `await()` releases lock & waits, `signal()`/`signalAll()` wakes waiting threads

**Semaphores**: Allow N threads into critical section.
- `acquire()`: decrements permits, blocks if 0
- `release()`: increments permits, signals waiting thread

**Barriers**: Block until N threads reach barrier point. `CyclicBarrier` resets after release.

**Exercises**: `ReadWriteMonitor2Conditions.java`

## 3. Visibility & Reordering

> Explain the problems of visibility and reordering in shared memory concurrency.
> Motivate and describe the use of volatile variables and locks to tackle these problems.
> Show some examples of code from your solutions to the exercises in week 2.

**Visibility Problem**: Without synchronization, writes in one thread's cache may not be visible to other threads.

**Reordering**: Compiler/CPU may reorder instructions without data dependencies for optimization.

**Solutions**:
- **volatile**: Reads/writes go directly to main memory, prevents reordering, ensures visibility
- **Locks**: Acquiring/releasing flushes caches, establishes happens-before

**Exercise**: `TestMutableInteger.java`

## 4. Java Memory Model (JMM)

> Motivate the need for the Java memory model.
> Explain the elements of the Java memory model including program order, happens-before order, synchronization order, and data races.
> Define what a correctly synchronized program is according to the Java memory model.
> Show some examples of code from your solutions to the exercises in week 3 and illustrate the use of the Java memory model to reason about their correctness.

**Purpose**: Define memory operation behavior independent of hardware; guarantee correctness for synchronized programs.

**Key Concepts**:
- **Program Order**: Intra-thread execution order
- **Happens-Before (->)**: Partial order guaranteeing visibility
  - Program order rule: a -> b if same thread, a before b
  - Monitor lock rule: unlock -> subsequent lock
  - Volatile rule: write -> subsequent read
  - Thread start rule: start() -> first action in thread
  - Thread join rule: last action in thread -> join() return
  - Transitivity: a -> b ^ b -> c => a -> c

**Data Race**: Conflicting accesses (same variable, >= 1 write) not ordered by happens-before.

**Correctly Synchronized**: No data races. JMM guarantees sequential consistency for such programs.

## 5. Thread-Safe Classes

> Define and explain what makes a class thread-safe.
> Explain the issues that may make classes not thread-safe.
> Show some examples of code from your solutions to the exercises in week 4.

**Definition**: Behaves correctly under concurrent access without external synchronization.

**Thread-safe if**:
- Properly synchronized mutable state
- Immutable (state can't change)
- Stateless

**Analysis Steps**:
1. Identify class state (fields)
2. Prevent field escape
3. Ensure safe publication (volatile/final/static/atomic)
4. Make fields immutable where possible
5. Use mutual exclusion for mutable fields

**Safe Publication**: Use volatile, final, static, or atomic classes to ensure initialization happens-before access.

**Exercise**: `Person.java`

## 6. Testing Concurrent Programs

> Explain the challenges in ensuring the correctness of concurrent programs.
> Describe different testing strategies for concurrent programs, and their advantages and disadvantages.
> Show some examples of code from your solutions to the exercises in week 5.

**Challenges**: Non-determinism, interleavings hard to reproduce.

**Testing cannot prove absence of bugs, only presence.**

**Strategies**:
- Maximize contention (barrier to sync thread start)
- `@RepeatedTest` for multiple runs
- `Thread.yield()` for context switches
- Timeouts to detect deadlocks
- Test sequentially first

**Counter-examples**: 
- Safety: finite prefix leading to violation
- Liveness: infinite execution never reaching goal

**Tools**: JUnit, jcstress, formal verification (model checking)

**Exercise**: `ConcurrentSetTest.java`

## 7. Performance Measurements

> Motivate and explain how to measure the performance of Java code.
> Illustrate some of the pitfalls there are in doing such measurements.
> Show some examples of code from your solutions to the exercises in week 9.

**Pitfalls**:
- GC pauses (use `-verbose:gc`, warmup)
- JIT compilation (warmup phase)
- Dead code elimination (use results somehow)
- Timer resolution too low
- Caching effects

**Best Practices**:
- Run multiple iterations, compute mean & std dev
- Use warmup phase for JIT stabilization
- Measure from command line, not IDE
- Control environment (disable power saving, close other apps)
- Measure overhead separately

**Mark versions**: 0-8 progressively add iterations, std dev, auto-adjustment, setup functions.

**Exercise**: `TestTimeSearch.java`

## 8. Performance & Scalability

> Explain how to increase the performance of Java code exploiting concurrency. 
> Illustrate some of the pitfalls there are in doing this.
> Show some examples of code from your solutions to the exercises in week 10.

**Amdahl's Law**: S = 1 / (F + (1-F)/P)
- F = sequential fraction, P = processors
- Speedup limited by sequential portion

**Use Tasks over Threads**: Thread pools avoid creation overhead.
- Runnable: no return value
- Callable: returns value

**Thread Pools**: ForkJoinPool, FixedThreadPool, WorkStealingPool

**Loss of Scalability**:
- Starvation loss: threads idle waiting
- Contention loss: waiting for same resource
- Saturation loss: blocked waiting for resources

**Exercise**: `TestCountPrimesThreads.java`

## 9. Lock-Free Data Structures

> Define and motivate lock-free data structures. 
> Explain how *compare-and-swap* (CAS) operations can be used to solve concurrency problems. 
> Show some examples of code from your solutions to the exercises in week 6.

**Progress Conditions** (strongest to weakest):
1. **Wait-free**: Every thread completes in bounded steps
2. **Lock-free**: Some thread always makes progress (CAS)
3. **Obstruction-free**: Progress guaranteed in isolation

**Compare-and-Swap (CAS)**: `compareAndSet(expected, new)` - atomically updates if current==expected.

```java
do {
    oldVal = value.get();
    newVal = oldVal + 1;
} while (!value.compareAndSet(oldVal, newVal));
```

**Optimistic concurrency**: Try operation, retry on conflict.

**ABA Problem**: Value changes A→B→A; CAS sees A, thinks unchanged. Solve with version numbers.

**Exercise**: `CasHistogram.java`

## 10. Linearizability

> Explain and motivate linearizability. 
> Explain how linearizability can be applied to reason about the correctness of concurrent objects. 
> Show some examples of code in your solutions to the exercises in week 7 where you used linearizability to reason about correctness.

**Sequential Consistency**: Operations appear one-at-a-time, preserving program order per thread.

**Linearizability** = Sequential consistency + real-time order preserved.

**Linearization Point**: Instant between invocation and response when method "takes effect."

**Proving Linearizability**:
1. Identify linearization points
2. Show reordering by linearization points produces valid sequential execution
3. Verify specification satisfied

**Compositional**: Linearizable objects compose to linearizable systems.

**Exercise**: `LockFreeStack.java`

## 11. Streams

> Explain and motivate the use of streams to parallelize computation. 
> Discuss issues that arise in operations executed by parallel streams. 
> Show some examples of code from your solutions to the exercises in week 11.

**Stream Pipeline**: Source -> Intermediate ops -> Terminal op

**Intermediate** (lazy): `map`, `filter`, `sorted`, `distinct`
**Terminal**: `collect`, `count`, `forEach`

**Parallel Streams**: `parallelStream()` or `.parallel()`
- Framework handles splitting/merging
- Must avoid side effects for correctness
- Functional style = thread-safe

**Issues**: Side effects, ordering requirements, stateful operations.

**Exercise**: `LockFreeStack.java`

## 12-13. Message Passing & Actor Model

> Explain and motivate the actor model of concurrent computation. 
> Discuss advantages and disadvantages of approaches to distribute computation in actor systems. 
> Show some examples of code from your solutions to the exercises in week 12 and 13.

**Message Passing**: Threads communicate via messages, not shared memory. Used in distributed systems.

**Actor Model**: Actors are fundamental units.
- **Actions**: Send message, receive message, create actor, change own state
- **Properties**: Unique address, mailbox (FIFO), non-blocking send, blocking receive

**Erlang Patterns**: 
- `spawn` creates actors
- `Pid ! Message` sends
- `receive` blocks for messages
- Pattern matching for message types

**Happens-Before in Actors**: 
- Within actor: program order
- Across actors: send -> receive

**Fault Tolerance**: `monitor` other actors, receive `DOWN` on failure.

**Load Balancing**: 
- Scatter-Gather: split work to workers, combine results
- Elastic: dynamically create/destroy actors based on load

**Topology**: Static (fixed connections) vs Dynamic (actors created/destroyed).

**Exercises**: `week13exercises`
