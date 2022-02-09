

# Lecture 2

## Pointers

- A reference to a place in memory where a variable live

- One could call it the address to the home of the data

- ```go
  var myVar int // Create a variable, instantiated by default to 0
  myVar = 5 // My var is now 5
  
  var myPointer *int // Create a pointer variable, *x denotes "pointer to var of type x". The pointer is not pointing at anything to begin with. Aka the value is nil.
  myPointer = &myVar // myPointer now points to the memory address of myVar. &x denotes "address of x"
  ```



## Slices

[Implementation](https://github.com/golang/go/blob/master/src/runtime/slice.go)

* Basically a dynamic array, think ArrayList in Java

* In reality a slice is a pointer to an array, by creating a view onto an array

* ```go
  primes := [6]int{2,3,5,7,11,13} // Create a new array
  var s []int := primes[1:4] // Make a slice of the array, that looks at the first to fourth array
  // s = [3,5,7]
  ```

* The slice is implemented as a struct with:

  * Length, the length of the data in the slice
  * Capacity, the length of the slice
  * Pointer to the head of an actual static array

* Remember to use make and append for respectively allocating array space and adding elements to an existing slice

* Using append, will add an element to the slice, if the slice is too small, it will allocate a new array, and point the slice to the newly allocated array, same as ArrayList

* In essence, the slice is a view of an underlying array, that can be appended to, and can look at certain parts of an array, creating a subset. ArrayList functions in exactly the same way.



## Functions

- Use functions when possible

- From a Java perspective, they are basically a method without having to be in a class

- Functions can use recursion, aka reference itself

- A function is not a method, Go also has methods that can be linked to a struct

- ```go
  func add(a int, b int) int { // Takes 2 int parameters and returns an int
      return a + b
  }
  
  fmt.Println(add(2,3)) // Use it to add 2 and 3, returns 5
  ```

- ```go
  // Go methods example
  type rect struct { // Define a new struct type
      width, height int
  }
  
  func (r *rect) area() int { // In order: Link to the struct, define function, define return type
      return r.width * r.height
  }
  
  r := rect {width: 10, height: 5} // Define a new struct instance
  
  fmt.Println("Area: ", r.area()) // Prints 50
  
  // Go methods is basically object oriented programming, but with extra steps
  ```



## Threads & Synchronisation

### Threads

- A thread could be seen as a production line, multiple can run in parallel doing the same work, but will have to wait for each other if they share a resource

- Usually a CPU has 2 threads pr core, so two lines it can focus on, so a 4 core, has 8 threads.

- One process can spawn many threads, known as goroutines in go.

- Every thread can access memory and resources

- Goroutines

  - To create a new go routine, use ``go func_to_run_in_thread()``, Which will spin up a new thread, and not wait for it to return, emitting the ``go`` will make the current thread wait for the function to return.

  - ```go
    package main
    
    import (
    	"fmt"
    	"time"
    )
    
    // Function to do on another thread
    func print(x int) {
    	fmt.Println(x)
    }
    
    func main() {
    	numbers := [6]int{1,2,3,4,5,6} // Define an int array to use
    
    	for x := range(numbers) { // Loop over that array
    		go print(x) // Print the number on a new thread
    	}
    
    	time.Sleep(1 * time.Second) // Have the main thread sleep, as if we don't the the main thread exits before the other threads are done
    }
    
    // Out (This will change each time the program is run):
    // 6
    // 1
    // 4
    // 5
    // 2
    // 3
    
    // As each print is on a new thread, it seems random which thread prints in which order, as it's up to the cpu to prioritize which thread get's to execute, known as CPU scheduling
    ```



### Race conditions

- When multiple threads try to access the same variable in the wrong or random order, which causes unpredictable results, known as a data race.

- Race conditons are really hard to debug, as the result would be incorrct, but the entire program might execute without error, and seemingly corrcetly. On top of that, because of CPU scheduling, the race condition might be very hard to reproduce, as it could happen once in millions of executions.

- Reading the same variable may not be a problem, but writing very much is, as 2 threads might write at the same time, resulting in the variable updating to a random of those threads. Imagine reading, adding, then writing. If both threads read at the same time, they get the current value, then both add, and then write. The result would be the result of the last thread that wrote, but would not be the result of 2 additions, big no no. 

- ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  var number int
  
  func add(x int) {
  	for i := 0; i < x; i++ {
  		number = number + 1
  	}
  }
  
  func main() {
  	numbers := [10]int{1,2,3,4,5,6,7,8,9,10}
  
  	for _, x := range(numbers) {
  		go add(x * 1000)
  	}
  
  	time.Sleep(1 * time.Second) // Have the main thread sleep, as if we don't the the main thread exits before the other threads are done
  
  	// Should be 55000
  	fmt.Println(number)
  }
  // We start threads, that do the same, and access the same variable
  // When doing so, one thread realises that its acccessing a variable that is in use, therefore not sure it is in sync, we get a DATA RACE error, result:
  /* $ go run -race datarace.go
  ==================
  WARNING: DATA RACE
  Read at 0x000000605948 by goroutine 8:
    main.add()
        /home/albertrisenielsen/Documents/Uni/disys/examples/datarace.go:12
  +0x47
  
  Previous write at 0x000000605948 by goroutine 7:
    main.add()
        /home/albertrisenielsen/Documents/Uni/disys/examples/datarace.go:12
  +0x64
  
  Goroutine 8 (running) created at:
    main.main()
        /home/albertrisenielsen/Documents/Uni/disys/examples/datarace.go:20
  +0xc7
  
  Goroutine 7 (finished) created at:
    main.main()
        /home/albertrisenielsen/Documents/Uni/disys/examples/datarace.go:20
  +0xc7
  ==================
  27321
  Found 1 data race(s)
  exit status 66
  */
  ```

- Solution:

  - Use locks. This would lock the variable to that thread

  - ```go
    package main
    
    import (
    	"time"
        "sync"
    )
    
    var arbiter sync.Mutex // Create an arbiter for locking the variable, when mutating (reading is fine)
    
    // Race condition example
    var number int
    
    func increase() {
        arbiter.Lock()
        number++
        arbiter.Unlock()
    }
    
    func main() {
        go increase()
        go increase()
        
        
    	time.Sleep(1 * time.Second) // Have the main thread sleep, as if we don't the the main thread exits before the other threads are done
        
        fmt.Println(number)
    }
    ```

- Further reading:

  - [Banger video from Tom Scott on this phenomenon, using Twitter as an example](https://www.youtube.com/watch?v=RY_2gElt3SA)
  - 



