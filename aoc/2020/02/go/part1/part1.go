package main

import (
	"errors"
	"fmt"
	"io"
	"os"
)

func validatePassword(password []rune, targetRune rune, min, max int) error {
	targetRuneUsage := 0
	for _, rune := range password {
		if rune == targetRune {
			targetRuneUsage += 1
		}
		// fmt.Printf("%#U\n", rune)
	}
	// fmt.Printf("%#U used %d times\n", targetRune, targetRuneUsage)
	if targetRuneUsage < min || targetRuneUsage > max {
		return errors.New("validation_error")
	}
	return nil
}

type passwordAndRule struct {
	password   []rune
	targetRune rune
	min        int
	max        int
}

func countValidPasswords(lines []passwordAndRule) int {
	validCount := 0
	for _, line := range lines {
		err := validatePassword(line.password, line.targetRune, line.min, line.max)
		if err == nil {
			validCount += 1
		}
	}
	return validCount
}

func loadFile(filename string) (lines []passwordAndRule, err error) {
	// https://www.socketloop.com/tutorials/golang-read-integer-from-file-into-array
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
		return nil, fmt.Errorf("Failed to open file")
	}
	var min, max int
	var targetRune, password string
	for {
		_, err := fmt.Fscanf(file, "%d-%d %s %s\n", &min, &max, &targetRune, &password)
		if err != nil {
			if err == io.EOF {
				break
			}
			fmt.Println(err)
			return nil, fmt.Errorf("File read error")
		}
		line := passwordAndRule{[]rune(password), []rune(targetRune)[0], min, max}
		lines = append(lines, line)
	}
	return lines, nil
}

func main() {
	lines, err := loadFile("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	validPasswords := countValidPasswords(lines)
	fmt.Println(validPasswords)
}
