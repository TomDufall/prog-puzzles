package part1

import (
	"fmt"
	"io"
	"os"
)

func CountCollisions(obstructions [][]bool, xStep, yStep int) (count int, err error) {
	if yStep <= 0 {
		return 0, fmt.Errorf("yStep must be greater than 0 to terminate")
	}
	count = 0
	x := 0
	for y := 0; y < len(obstructions); y += yStep {
		if obstructions[y][x] == true {
			count += 1
		}
		x = (x + xStep) % len(obstructions[y])
	}
	return count, nil
}

func LoadFile(filename string) (obstructions [][]bool, err error) {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
		return nil, fmt.Errorf("Failed to open file")
	}
	var row string
	i := 0
	for {
		_, err := fmt.Fscanf(file, "%s\n", &row)
		if err != nil {
			if err == io.EOF {
				break
			}
			fmt.Println(err)
			return nil, fmt.Errorf("File read error")
		}
		obstructions = append(obstructions, (make([]bool, len(row))))
		for j, rune := range []rune(row) {
			obstructions[i][j] = rune != '.'
		}
		i += 1
	}
	return obstructions, nil
}
