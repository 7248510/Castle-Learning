package main

import (
	"fmt"

	"exampleDO/addModule"
)

func main() {
	fmt.Println("Called from the main file")
	addModule.PrintHello()
}