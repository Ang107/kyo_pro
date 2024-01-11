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
	s := make([][]string, n)
	for i := 0; i < n; i++ {
		tmp := getS()
		s[i] = make([]string, n)
		for j, k := range tmp {
			s[i][j] = string(k)
		}
	}
	ans := 2
	var num int
	var tmp int
	tmp = -1
	p_flag := false
	m_flag := false
	// for _, i := range s {
	// 	out(i)
	// }
	for i := 0; i < n; i++ {
		tmp = -1
		for j := 0; j < n; j++ {

			if tmp == -1 {
				tmp = 1
				num = toInt(s[i][j])
				p_flag, m_flag = true, true
			} else {
				if num+1 == toInt(s[i][j]) && p_flag {
					m_flag = false
					tmp += 1
					num += 1
				} else if num-1 == toInt(s[i][j]) && m_flag {
					p_flag = false
					tmp += 1
					num -= 1
				} else {
					ans = max(ans, tmp)
					if tmp > 1 {
						j -= 1
					}
					tmp = 1
					num = toInt(s[i][j])
					p_flag, m_flag = true, true

				}
			}
			ans = max(ans, tmp)
		}
	}

	for i := 0; i < n; i++ {
		tmp = -1
		for j := 0; j < n; j++ {
			if tmp == -1 {
				tmp = 1
				num = toInt(s[j][i])
				p_flag, m_flag = true, true
			} else {
				if num+1 == toInt(s[j][i]) && p_flag {
					m_flag = false
					tmp += 1
					num += 1
				} else if num-1 == toInt(s[j][i]) && m_flag {
					p_flag = false
					tmp += 1
					num -= 1
				} else {
					ans = max(ans, tmp)
					if tmp > 1 {
						j -= 1
					}
					tmp = 1
					num = toInt(s[j][i])
					p_flag, m_flag = true, true
				}
			}
			ans = max(ans, tmp)
		}
	}
	for i := 0; i < n; i++ {
		x := i
		y := 0
		tmp = -1
		for x < n && y < n {
			if tmp == -1 {
				tmp = 1
				num = toInt(s[x][y])
				p_flag, m_flag = true, true
			} else {
				if num+1 == toInt(s[x][y]) && p_flag {
					m_flag = false
					tmp += 1
					num += 1
				} else if num-1 == toInt(s[x][y]) && m_flag {
					p_flag = false
					tmp += 1
					num -= 1
				} else {
					ans = max(ans, tmp)
					if tmp > 1 {
						x--
						y--
					}
					tmp = 1
					num = toInt(s[x][y])
					p_flag, m_flag = true, true
				}
			}
			x++
			y++
			ans = max(ans, tmp)
		}
	}
	for i := 0; i < n; i++ {
		x := i
		y := n - 1
		tmp = -1
		for x < n && y < n {
			if tmp == -1 {
				tmp = 1
				num = toInt(s[x][y])
				p_flag, m_flag = true, true
			} else {
				if num+1 == toInt(s[x][y]) && p_flag {
					m_flag = false
					tmp += 1
					num += 1
				} else if num-1 == toInt(s[x][y]) && m_flag {
					p_flag = false
					tmp += 1
					num -= 1
				} else {
					ans = max(ans, tmp)
					if tmp > 1 {
						x--
						y--
					}
					tmp = 1
					num = toInt(s[x][y])
					p_flag, m_flag = true, true
				}
			}
			x++
			y++
			ans = max(ans, tmp)
		}
	}

	for i := 0; i < n; i++ {
		x := i
		y := 0
		tmp = -1
		for 0 <= x && 0 <= y {
			if tmp == -1 {
				tmp = 1
				num = toInt(s[x][y])
				p_flag, m_flag = true, true
			} else {
				if num+1 == toInt(s[x][y]) && p_flag {
					m_flag = false
					tmp += 1
					num += 1
				} else if num-1 == toInt(s[x][y]) && m_flag {
					p_flag = false
					tmp += 1
					num -= 1
				} else {
					ans = max(ans, tmp)
					if tmp > 1 {
						x++
						y++
					}
					tmp = 1
					num = toInt(s[x][y])
					p_flag, m_flag = true, true
				}
			}
			x--
			y--
			ans = max(ans, tmp)
		}
	}
	for i := 0; i < n; i++ {
		x := i
		y := n - 1
		tmp = -1
		for 0 <= x && 0 <= y {
			if tmp == -1 {
				tmp = 1
				num = toInt(s[x][y])
				p_flag, m_flag = true, true
			} else {
				if num+1 == toInt(s[x][y]) && p_flag {
					m_flag = false
					tmp += 1
					num += 1
				} else if num-1 == toInt(s[x][y]) && m_flag {
					p_flag = false
					tmp += 1
					num -= 1
				} else {
					ans = max(ans, tmp)
					if tmp > 1 {
						x++
						y++
					}
					tmp = 1
					num = toInt(s[x][y])
					p_flag, m_flag = true, true
				}
			}
			x--
			y--
			ans = max(ans, tmp)
		}
	}
	out(ans)
	// use getI(), getS(), getInts(), getF()
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
