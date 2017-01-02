package main

import (
"fmt"
"time"
)

func main() {
    	go fmt.Println("Hello from another goroutine")
	fmt.Println("Hello,world!")

	time.Sleep(time.Second)
}
