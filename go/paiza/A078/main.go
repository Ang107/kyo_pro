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
var h int
var w int

func main() {
	defer wr.Flush()
	sc.Split(bufio.ScanWords)
	sc.Buffer([]byte{}, math.MaxInt32)
	h = getI()
	w = 5
	S := make([][]rune, h)
	for i := 0; i < h; i++ {
		s := getS()
		S[i] = []rune(s)
	}

	for len(get_zyuuzi(S)) != 0 {
		del := get_zyuuzi(S)
		del_zyuuzi(S, del)
		rakka(S)

	}
	for _, i := range S {
		out(string(i))
	}
	// use getI(), getS(), getInts(), getF()
}

func get_zyuuzi(s [][]rune) [][2]int {
	h := len(s)
	w := 5
	ans := make([][2]int, 0, 100)
	around4 := make([][]int, 4)
	around4[0] = []int{0, -1}
	around4[1] = []int{0, 1}
	around4[2] = []int{-1, 0}
	around4[3] = []int{1, 0}
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			flag := true
			if s[i][j] == '.' {
				continue
			}
			for _, k := range around4 {
				p, q := k[0], k[1]
				if 0 <= i+p && i+p < h && 0 <= j+q && j+q < w {
					if s[i][j] != s[i+p][j+q] {
						flag = false
						break
					}
				}
			}
			if flag {
				ans = append(ans, [2]int{i, j})
			}
		}
	}
	return ans
}
func del_zyuuzi(s [][]rune, del [][2]int) {
	for _, i := range del {
		p, q := i[0], i[1]
		s[p][q] = '.'
		s[p][max(0, q-1)] = '.'
		s[p][min(w-1, q+1)] = '.'
		s[max(0, p-1)][q] = '.'
		s[min(h-1, p+1)][q] = '.'
	}
}
func rakka(s [][]rune) {
	for i := 0; i < 5; i++ {
		for j := len(s) - 1; j > 0; j-- {
			if s[j][i] == '.' {
				l := 1
				for j-l > 0 && s[j-l][i] == '.' {
					l += 1
					// out(i, j-l)
				}
				s[j][i], s[j-l][i] = s[j-l][i], s[j][i]
			}
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
