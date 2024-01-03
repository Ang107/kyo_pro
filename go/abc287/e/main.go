package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func main() {
	defer wr.Flush()
	sc.Split(bufio.ScanWords)
	sc.Buffer([]byte{}, math.MaxInt32)
	n := getI()
	S := make([]string, n)
	Map := make(map[string]int)
	for i := 0; i < n; i++ {
		s := getS()
		S[i] = s
	}
	default_S := make([]string, n)
	copy(default_S, S)
	sort.Strings(S)
	// out(S)
	// out(Map)
	for i := 0; i < n; i++ {
		ans := 0
		if i-1 >= 0 {
			// out("-")
			temp := 0
			for j := 0; j < min(len(S[i]), len(S[i-1])); j++ {
				// out(S[i][j], S[i-1][j], S[i][j] == S[i-1][j])
				if S[i][j] == S[i-1][j] {
					temp += 1
				} else {
					break
				}
			}
			ans = max(ans, temp)
		}
		if i+1 < n {
			// out("+")
			temp := 0
			for j := 0; j < min(len(S[i]), len(S[i+1])); j++ {
				// out(S[i][j], S[i+1][j], S[i][j] == S[i+1][j])

				if S[i][j] == S[i+1][j] {
					temp += 1
				} else {
					break
				}
			}
			ans = max(ans, temp)
		}
		Map[S[i]] = ans
		// out(S[i], ans)
	}
	// out(Map)
	for _, i := range default_S {
		out(Map[i])
	}

}

func out(x ...interface{}) {
	fmt.Fprintln(wr, x...)
}

func getI() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func getF() float64 {
	sc.Scan()
	i, e := strconv.ParseFloat(sc.Text(), 64)
	if e != nil {
		panic(e)
	}
	return i
}

func getInts(N int) []int {
	ret := make([]int, N)
	for i := 0; i < N; i++ {
		ret[i] = getI()
	}
	return ret
}

func getS() string {
	sc.Scan()
	return sc.Text()
}

// 型変換
func toStr(num int) string {
	return strconv.Itoa(num)
}

func toInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

// 重複削除
func toSet(arr []int) []int {
	m := make(map[int]struct{})
	for _, v := range arr {
		m[v] = struct{}{}
	}
	var newArr []int
	for k, _ := range m {
		newArr = append(newArr, k)
	}
	return newArr
}

func toMap(slice []int) map[int]bool {
	m := make(map[int]bool)
	for _, s := range slice {
		m[s] = true
	}
	return m
}

func inSlice(slice []int, key int) bool {
	for _, i := range slice {
		if i == key {
			return true
		}
	}
	return false
}

func inMap(Map map[int]bool, key int) bool {
	_, exist := Map[key]
	return exist
}

func sum(a ...int) int {
	temp := 0
	for _, v := range a {
		temp += v
	}
	return temp
}

func max(a ...int) int {
	temp := a[0]
	for _, v := range a {
		if temp < v {
			temp = v
		}
	}
	return temp
}

func min(a ...int) int {
	temp := a[0]
	for _, v := range a {
		if temp > v {
			temp = v
		}
	}
	return temp
}

func chmin(a *int, b int) bool {
	if *a < b {
		return false
	}
	*a = b
	return true
}

func chmax(a *int, b int) bool {
	if *a > b {
		return false
	}
	*a = b
	return true
}

func asub(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}

func lowerBound(a []int, x int) int {
	idx := sort.Search(len(a), func(i int) bool {
		return a[i] >= x
	})
	return idx
}

func upperBound(a []int, x int) int {
	idx := sort.Search(len(a), func(i int) bool {
		return a[i] > x
	})
	return idx
}
