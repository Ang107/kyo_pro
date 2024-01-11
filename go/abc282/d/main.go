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
var Map map[int][]int
var Map_color map[int]map[int]bool

func main() {
	defer wr.Flush()
	sc.Split(bufio.ScanWords)
	sc.Buffer([]byte{}, math.MaxInt32)
	n, m := getI(), getI()
	Map = make(map[int][]int)
	visited = make(map[int]bool)

	for i := 0; i < m; i++ {
		u, v := getI(), getI()
		Map[u] = append(Map[u], v)
		Map[v] = append(Map[v], u)
	}

	ans := n*(n-1)/2 - m
	// v_num := make([]int, 0, n)
	Flag := true
	for i := 1; i <= n; i++ {
		if !visited[i] {
			Map_color = make(map[int]map[int]bool)
			Map_color[0] = make(map[int]bool)
			Map_color[1] = make(map[int]bool)
			flag = true
			nibu(i, 0)
			Flag = Flag && flag
			// out(i, flag)
			if flag {
				ans -= get_ans(Map_color)
				// v_num = append(v_num, get_num(Map_color))
			}
		}
	}
	// for i := 0; i < len(v_num); i++ {
	// 	for j := i + 1; j < len(v_num); j++ {
	// 		ans += v_num[i] * v_num[j]
	// 	}
	// }
	if Flag {
		out(ans)
	} else {
		out(0)
	}
	// use getI(), getS(), getInts(), getF()
}

var visited map[int]bool
var flag bool

func get_num(Map_color map[int]map[int]bool) int {
	return len(Map_color[0]) + len(Map_color[1])
}

func get_ans(Map_color map[int]map[int]bool) int {
	tmp := len(Map_color[0])
	tmp = tmp * (tmp - 1) / 2
	tmp1 := len(Map_color[1])
	tmp1 = tmp1 * (tmp1 - 1) / 2
	return tmp + tmp1
}
func nibu(x int, color int) {
	visited[x] = true
	// out(Map_color)
	// out(visited)
	// getI()
	if !Map_color[(color+1)%2][x] {
		Map_color[color][x] = true
	} else {
		// out(false)
		flag = false
	}
	for _, i := range Map[x] {
		if Map_color[color][i] {
			flag = false
		}
		if !visited[i] {
			nibu(i, (color+1)%2)
		}
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
