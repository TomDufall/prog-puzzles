package main

import (
	"errors"
	"fmt"
	"io"
	"os"
)

func validatePassword(password []rune, targetRune rune, i, j int) error {
	if i < 0 || j < 0 || i > len(password) || j > len(password) {
		return errors.New("Index out of bounds error")
	}
	iMatch := password[i-1] == targetRune
	jMatch := password[j-1] == targetRune
	if iMatch == jMatch {
		// Must be exactly one match
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
	defer file.Close()
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
