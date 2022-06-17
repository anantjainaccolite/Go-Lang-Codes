package main

import (
	"fmt"
)

func cal(arr []int) int {
	if len(arr) == 0 {
		return 0
	}
	max_so_far := arr[0]
	max_end_here := 0
	for i := 0; i < len(arr); i++ {

		max_end_here += arr[i]
		if max_end_here > max_so_far {
			max_so_far = max_end_here
		}
		if max_end_here < 0 {

			max_end_here = 0
		}
	}
	return max_so_far
}

func main() {
	var items = [][]int{{1, 2, 3, 3, 4},
		{-2, -3, -5, -1, -10},
		{1, -1, 2, -2, 3, -3, 4, -4, 5},
		{10, -7, 3, 3, -5, -1},
		{11, -1, 10, -30, 40},
		{500},
		{}}
	for i := 0; i < len(items); i++ {
		res := cal(items[i])
		fmt.Println(" Sum: ", res)
	}

}
