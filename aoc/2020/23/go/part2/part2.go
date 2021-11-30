package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func build_cups(preamble string, length int) (cups []int, err error) {
	// Return an array where the value at each index is the cup value next in the chain
	charArray := strings.Split(preamble, "")
	cups = make([]int, length+1)
	first, err := strconv.Atoi(charArray[0])
	if err != nil {
		return nil, err
	}
	prev := first
	var next int
	for i := 1; i < length; i++ {
		if i < len(charArray) {
			next, err = strconv.Atoi(charArray[i])
			if err != nil {
				return nil, err
			}
		} else {
			next = i + 1
		}
		cups[prev] = next
		prev = next
		if i == length-1 {
			cups[prev] = first
		}
	}
	return cups, nil
}

func do_moves(cups []int, moves int, current_cup int) []int {
	for i := 0; i < moves; i++ {
		cup_1 := cups[current_cup]
		cup_2 := cups[cup_1]
		cup_3 := cups[cup_2]
		destination_cup := current_cup
		for {
			destination_cup -= 1
			if destination_cup == 0 {
				destination_cup = len(cups) - 1
			}
			if destination_cup != cup_1 && destination_cup != cup_2 && destination_cup != cup_3 {
				break
			}
			if destination_cup == current_cup {
				panic("Infinite loop")
			}
		}
		cups[current_cup] = cups[cup_3]
		cups[cup_3] = cups[destination_cup]
		cups[destination_cup] = cup_1
		current_cup = cups[current_cup]
	}
	return cups
}

func main() {
	start := time.Now()
	preamble := "523764819"
	first_cup := 5
	cups, err := build_cups(preamble, 1000000)
	// for i := 0; i < len(cups); i++ {
	// 	fmt.Println(cups[i])
	// }
	if err != nil {
		return
	}
	fmt.Println("======")
	moved_cups := do_moves(cups, 10000000, first_cup)
	// for i := 0; i < len(moved_cups); i++ {
	// 	fmt.Println(moved_cups[i])
	// }
	next_1 := moved_cups[1]
	next_2 := moved_cups[next_1]
	fmt.Println("Two cups after 1 are", next_1, "and", next_2)
	fmt.Println(next_1 * next_2)
	elapsed := time.Since(start)
	fmt.Println("Time taken:", elapsed)
}
