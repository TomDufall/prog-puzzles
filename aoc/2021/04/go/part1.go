package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type board struct {
	cells [][]int
}

func make_board(strings_ []string) (board_ board) {
	length := len(strings_) // assume square
	board_.cells = make([][]int, length)
	for i := 0; i < length; i++ {
		board_.cells[i] = make([]int, length)
	}
	for row_i, row_str := range strings_ {
		for col_i, num_str := range strings.Fields(row_str) {
			if num_str == "" {
				log.Fatal()
			}
			num, err := strconv.Atoi(num_str)
			if err != nil {
				log.Fatal(err)
			}
			board_.cells[col_i][row_i] = num
		}
	}
	return
}

func loadFile(filename string) (calls []int, boards []board) {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Scan()
	calls_strs := strings.Split(scanner.Text(), ",")
	scanner.Scan() // Discard blank line
	var num int
	for _, x := range calls_strs {
		num, err = strconv.Atoi(x)
		if err != nil {
			log.Fatal(err)
		}
		calls = append(calls, num)
	}

	var lines [5]string
	i := 0
	for scanner.Scan() {
		lines[i] = scanner.Text()
		i += 1
		if i == 5 {
			boards = append(boards, make_board(lines[:]))
			scanner.Scan() // skip next blank line
			i = 0
		}
	}
	return
}

func main() {
	calls, boards := loadFile("input.txt")
	println(calls, boards)
}
