package main

import (
	"fmt"
	"time"
)

func print(x int) {
	fmt.Println(x)
}

func main() {
	numbers := [6]int{1,2,3,4,5,6}

	for _, x := range(numbers) {
		go print(x)
	}

	time.Sleep(1 * time.Second)
}
