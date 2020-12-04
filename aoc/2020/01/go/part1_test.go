package main

import (
	"fmt"
	"testing"
)

func TestFindSumPair(t *testing.T) {
	var tests = []struct {
		numbers              []int
		target               int
		expectedA, expectedB int
		expectedErr          error
	}{
		{[]int{1721, 979, 366, 299, 675, 1456}, 2020, 1721, 299, nil},
	}
	for num, tt := range tests {
		testname := fmt.Sprintf("%d", num)
		t.Run(testname, func(t *testing.T) {
			actualA, actualB, actualErr := findSumPair(tt.numbers, tt.target)
			if actualA != tt.expectedA || actualB != tt.expectedB || actualErr != tt.expectedErr {
				t.Errorf("actual %d, %d, %s, expected %d, %d, %s", actualA, actualB, actualErr, tt.expectedA, tt.expectedB, tt.expectedErr)
			}
		})
	}
}
