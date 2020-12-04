package main

import (
	"fmt"
	"io"
	"os"
)

func findSumPair(numbers []int, target int) (result1, result2 int, err error) {
	for i := 0; i < len(numbers); i++ {
		for j := 0; j < len(numbers); j++ {
			if numbers[i]+numbers[j] == target {
				return numbers[i], numbers[j], nil
			}
		}
	}
	return 0, 0, fmt.Errorf("No sum pair found for target %d", target)
}

func fixExpenseReport(numbers []int, target int) (result int, err error) {
	result1, result2, err := findSumPair(numbers, target)
	if err != nil {
		return 0, err
	}
	return result1 * result2, nil
}

func loadIntsFile(filename string) (nums []int, err error) {
	// https://www.socketloop.com/tutorials/golang-read-integer-from-file-into-array
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
		return nil, fmt.Errorf("Failed to open file")
	}
	var perline int
	for {
		_, err := fmt.Fscanf(file, "%d\n", &perline)
		if err != nil {
			if err == io.EOF {
				break
			}
			fmt.Println(err)
			return nil, fmt.Errorf("File read error")
		}
		nums = append(nums, perline)
	}
	return nums, nil
}

func main() {
	numbers, err := loadIntsFile("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(fixExpenseReport(numbers, 2020))
}
