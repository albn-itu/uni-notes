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

	time.Sleep(1000 * time.Millisecond)

	// Should be 55000
	fmt.Println(number)
}
