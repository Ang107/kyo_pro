package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)
var Map map[int][]int

func main() {
	defer wr.Flush()
	sc.Split(bufio.ScanWords)
	sc.Buffer([]byte{}, math.MaxInt32)
	m := getI()
	Map = make(map[int][]int)
	for i := 0; i < m; i++ {
		u, v := getI(), getI()
		Map[u] = append(Map[u], v)
		Map[v] = append(Map[v], u)
	}
	p := getInts(8)
	p_int := 0
	for j, i := range p {
		p_int += i * int(math.Pow(10, float64(7-j)))
	}
	kara := 45 - sum(p...)
	out(kara, p_int)
	bfs(kara, p_int)

	// use getI(), getS(), getInts(), getF()
}
func bfs(s int, defa int) int {
	deq := make([][4]int, 0, 10000)
	deq = append(deq, [4]int{s, -1, defa, 0})
	for len(deq) != 0 {
		x := deq[0]
		deq = deq[1:]

		if x[2] == 12345678 {
			return x[3]
		}

		for _, i := range Map[x[0]] {
			if i != x[1] {
				tmp1 := strings.Index(toStr(x[2]), toStr(x[0]))
				tmp2 := strings.Index(toStr(x[2]), toStr(i))
				out(tmp1, tmp2)
				out(i, x[0], change(x[2], tmp1, tmp2), x[3]+1)
				deq = append(deq, [4]int{i, x[0], change(x[2], tmp1, tmp2), x[3] + 1})
			}
		}
	}
	return -1
}

func change(num int, p int, q int) int {
	ans := toStr(num)
	ansSlice := []rune(ans)
	ansSlice[p], ansSlice[q] = ansSlice[q], ansSlice[p]
	ans = string(ansSlice)
	return toInt(ans)
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
