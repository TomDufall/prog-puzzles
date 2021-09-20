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
	slopes := [][]int{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}
	product := 1
	// Multiply the collisions for each together
	for _, xy := range slopes {
		collisions, err := part1.CountCollisions(obstructions, xy[0], xy[1])
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
		product *= collisions
		fmt.Println(collisions)
	}
	fmt.Println(product)
}
