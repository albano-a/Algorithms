package main

import "fmt"

func binary_search(arr [10]int, t int) int {
	var L int = 0
	var R int = len(arr) - 1

	for L <= R {
		var m int = (L + R) / 2
		if arr[m] < t {
			L = m + 1
		} else if arr[m] > t {
			R = m - 1
		} else {
			return m
		}
	}
	return -1
}

func main() {
	arr := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	var target int = 7

	index := binary_search(arr, target)
    if index != -1 {
        fmt.Printf("Found %d at index %d\n", target, index)
    } else {
        fmt.Printf("%d not found\n", target)
    }
}
