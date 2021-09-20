package main

import (
	"fmt"
	"os"
	"part1"
)

func main() {
	obstructions, err := part1.LoadFile("../../input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	collisions, err := part1.CountCollisions(obstructions, 3, 1)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(collisions)
}
