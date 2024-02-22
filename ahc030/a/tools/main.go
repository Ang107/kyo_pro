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
	// out("# start")
	FirstInput()
	solve()
	// use getI(), getS(), getInts(), getF()
}

var N int
var M int
var E float64
var D_zahyou [][][]int
var D_len_zahyou []int
var D_visited [][]bool
var D_maxmin [][]int
var kakutei []bool
var limit int
var D_size_sum int
var N_2 int
var D_size []int
var Tarn int

func FirstInput() {
	N, M, E = getI(), getI(), getF()
	N_2 = N * N

	kakutei = make([]bool, N_2)
	D_size_sum = 0
	limit = 3000000 / N_2
	D_zahyou = make([][][]int, 0, M)
	D_len_zahyou = make([]int, 0, M)
	D_visited = make([][]bool, 0, M)
	D_maxmin = make([][]int, 0, M)
	for i := 0; i < M; i++ {
		num := getI()
		tmp := getInts(num * 2)
		x_max, y_max := 0, 0
		zahyou := make([][]int, 0, num)
		for j := 1; j < num*2; j += 2 {
			x_max = max(x_max, tmp[j-1])
			y_max = max(y_max, tmp[j])
			zahyou = append(zahyou, []int{tmp[j-1], tmp[j]})
		}
		D_zahyou = append(D_zahyou, zahyou)
		D_len_zahyou = append(D_len_zahyou, len(zahyou))
		D_visited = append(D_visited, make([]bool, N_2))
		D_maxmin = append(D_maxmin, []int{x_max, y_max})
		D_size_sum += len(zahyou)
	}
	sort.Slice(D_zahyou, func(i, j int) bool {
		return D_len_zahyou[i] > D_len_zahyou[j]
	})
	sort.Slice(D_len_zahyou, func(i, j int) bool {
		return D_len_zahyou[i] > D_len_zahyou[j]
	})
	sort.Slice(D_visited, func(i, j int) bool {
		return D_len_zahyou[i] > D_len_zahyou[j]
	})
	sort.Slice(D_maxmin, func(i, j int) bool {
		return D_len_zahyou[i] > D_len_zahyou[j]
	})
	D_size = make([]int, M)
	copy(D_size, D_len_zahyou)

	// fmt.Println("#", D_len_zahyou, D_maxmin, D_len_zahyou)

	for i := M - 2; i >= 0; i-- {
		D_size[i] += D_size[i+1]
	}

	// fmt.Println("#", D_size)
}

func OutputInput(l [][]int) int {
	tmp := make([]int, 0, D_size_sum)
	for _, pair := range l {
		tmp = append(tmp, pair[0])
		tmp = append(tmp, pair[1])
	}
	fmt.Printf("q %d", len(l))
	for _, val := range tmp {
		fmt.Printf(" %d", val)
	}
	fmt.Println()

	n := getI()
	return n
}

func Exit(B []int) {
	ans := make([][2]int, 0, D_size_sum)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if B[i*N+j] >= 1 {
				ans = append(ans, [2]int{i, j})
			}
		}
	}

	LastOutput(ans)
	os.Exit(0)
}

func LastOutput(l [][2]int) bool {
	tmp := make([]int, 0, D_size_sum*2+10)
	for _, pair := range l {
		tmp = append(tmp, pair[0])
		tmp = append(tmp, pair[1])
	}
	fmt.Printf("a %d", len(l))
	for _, val := range tmp {
		fmt.Printf(" %d", val)
	}
	fmt.Println()
	n := getI()
	if n == 0 {
		return false
	} else {
		return true
	}
}

func solve() {
	B := make([]int, N_2)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			B[i*N+j] = -100
		}
	}
	Tarn = 0
	count := 0
	next := calcNext(B)
	// fmt.Println("#", next)
	for {
		// 答えの候補の取得
		flag, ansList := getAns(B)
		fmt.Println("#", flag, len(ansList))

		// 絞り込めたなら
		// ansListの数の上限の決め方を吟味する->現在期待値5だが、一回のクエリで絞り込めるならそっちがお得
		if flag && 1 <= len(ansList) && len(ansList) <= 5 {
			for _, i := range ansList {
				tmp := make(map[[2]int]struct{})
				for idx, j := range D_zahyou {
					sx, sy := i[idx][0], i[idx][1]
					for _, xy := range j {
						tmp[[2]int{xy[0] + sx, +xy[1] + sy}] = struct{}{}
					}
				}
				Tarn++

				tmp1 := make([][2]int, 0, len(tmp))
				for key, _ := range tmp {
					tmp1 = append(tmp1, key)
				}
				if LastOutput(tmp1) {
					os.Exit(0)
				}
			}
		} else {
			// 絞り込めなかった場合
			// 次に送るクエリの候補を計算
			if flag {
				count++
				next = calcNextFromAns(ansList, B)
			} else {
				if len(ansList) == 0 {
					next = calcNext(B)
				} else {
					next = calcNextFromAns(ansList, B)
				}
			}
		}

		if len(next) == 0 {
			Exit(B)
		}

		// クエリを送信、Bの更新
		num := 1
		if Tarn > 150 {
			num = 2
		}
		if Tarn > 250 {
			num = 3
		}

		for i := 0; i < num; i++ {
			for {
				if len(next) == 0 {
					break
				}
				x, y := next[0][0], next[0][1]
				next = next[1:]

				if B[x*N+y] == -100 {
					Tarn++
					B[x*N+y] = OutputInput([][]int{{x, y}})
					break
				}
			}
		}
	}
}

func calcNextFromAns(ansList [][][2]int, B []int) [][2]int {
	next := make([]int, N*N)
	for _, ans := range ansList {
		tmp := make(map[[2]int]struct{})
		for idx, xy := range ans {
			// out(xy)
			x, y := xy[0], xy[1]
			for _, ij := range D_zahyou[idx] {
				tmp[[2]int{ij[0] + x, ij[1] + y}] = struct{}{}
			}
		}

		for ij, _ := range tmp {
			i, j := ij[0], ij[1]
			next[i*N+j] += 1
		}
	}

	tmp := make([][3]int, 0, N_2)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if next[i*N+j] > 0 && B[i*N+j] == -100 {
				tmp = append(tmp, [3]int{next[i*N+j], i, j})
			} else if next[i*N+j] == 0 && B[i*N+j] == -100 {
				B[i*N+j] = 0
			}
		}
	}

	sort.Slice(tmp, func(i, j int) bool {
		return abs(tmp[i][0]-len(ansList)/2) > abs(tmp[j][0]-len(ansList)/2)
	})

	tmp1 := make([][2]int, 0, N_2)
	for _, i := range tmp {
		j, k := i[1], i[2]
		tmp1 = append(tmp1, [2]int{j, k})
	}

	return tmp1
}

func calcNext(B []int) [][2]int {
	canUse := make([]map[int]bool, N*N)
	for i := 0; i < N_2; i++ {
		canUse[i] = make(map[int]bool)
	}
	next := make([]float64, N*N)
	plusSum := 0

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if B[i*N+j] >= 1 {
				plusSum += B[i*N+j]
			}
		}
	}

	count := 0
	for idx, d := range D_zahyou {
		size := D_len_zahyou[idx]
		visited := D_visited[idx]
		xMax, yMax := D_maxmin[idx][0], D_maxmin[idx][1]
		for i := 0; i < N-xMax; i++ {
			for j := 0; j < N-yMax; j++ {
				if visited[i*N+j] {
					continue
				}

				tmp := make([][2]int, 0, N_2)
				tmp1 := make([][2]int, 0, N_2)
				flag := 0

				for _, coord := range d {
					x, y := coord[0], coord[1]
					if i+x >= 0 && i+x < N && j+y >= 0 && j+y < N {
						if B[(i+x)*N+(j+y)] == -100 {
							tmp = append(tmp, [2]int{(i + x), (j + y)})
						} else if B[(i+x)*N+(j+y)] >= 1 {
							tmp1 = append(tmp1, [2]int{(i + x), (j + y)})
							flag++
						} else {
							flag = -1
							break
						}
					} else {
						flag = -1
						break
					}
				}

				if flag >= 0 && D_size[0]-size >= plusSum-flag {
					count++
					for _, coord := range tmp {
						p, q := coord[0], coord[1]
						next[p*N+q]++
						if float64(D_size_sum)/float64(N_2) < 0.35 && float64(Tarn) > float64(D_size_sum)*0.35 {
							next[p*N+q] += math.Pow(1-float64(flag)/float64(size), 0.5) * 10
						}
					}

					for _, coord := range tmp1 {
						p, q := coord[0], coord[1]
						canUse[p*N+q][idx] = true
					}
				} else {
					visited[i*N+j] = true
				}
			}
		}
	}

	tmp := make([][3]int, 0, N_2)

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if len(canUse[i*N+j]) == 1 && !kakutei[i*N+j] {
				var idx int
				for key := range canUse[i*N+j] {
					idx = key
				}
				kakutei[i*N+j] = true
				d, visited, xMax, yMax := D_zahyou[idx], D_visited[idx], D_maxmin[idx][0], D_maxmin[idx][1]

				for x := 0; x < N-xMax; x++ {
					for y := 0; y < N-yMax; y++ {
						if visited[x*N+y] {
							continue
						}
						flag := 0
						for _, pq := range d {
							p, q := pq[0], pq[1]
							if x+p >= 0 && x+p < N && y+q >= 0 && y+q < N {
								if B[(x+p)*N+(y+q)] == -100 || B[(x+p)*N+(y+q)] >= 1 {
									if x+p == i && y+q == j {
										flag = 1
									}
								} else {
									flag = -1
									break
								}
							} else {
								flag = -1
								break
							}
						}
						if flag <= 0 {
							visited[x*N+y] = true
						}
					}
				}
			}

			if next[i*N+j] != 0 && B[i*N+j] == -100 {
				tmp = append(tmp, [3]int{int(next[i*N+j]), i, j})
			} else if next[i*N+j] == 0 && B[i*N+j] == -100 {
				B[i*N+j] = 0
				// fmt.Printf("#c %d %d blue\n", i, j)
			}
			// fmt.Println("#", tmp)
		}
	}

	if float64(D_size_sum)/float64(N_2) < 0.35 && float64(Tarn) > float64(D_size_sum)*0.35 {
		sort.Slice(tmp, func(i, j int) bool {
			return tmp[i][0] > tmp[j][0]
		})
	} else {
		sort.Slice(tmp, func(i, j int) bool {
			return abs(tmp[i][0]-count/2) < abs(tmp[j][0]-count/2)
		})
	}

	result := make([][2]int, 0, N_2)
	for _, t := range tmp {

		i, j := t[1], t[2]
		result = append(result, [2]int{i, j})
	}
	return result
}

func getAns(B []int) (bool, [][][2]int) {
	var deq []struct {
		idx int
		B   []int
		prv [][2]int
	}
	B_n := make([]int, len(B))
	copy(B_n, B)
	deq = append(deq, struct {
		idx int
		B   []int
		prv [][2]int
	}{0, B_n, [][2]int{}})

	ans := make([][][2]int, 0, 300000)

	for len(deq) > 0 {

		front := deq[0]
		deq = deq[1:]
		idx, B, prv := front.idx, front.B, front.prv
		shape := D_zahyou[idx]
		visited := D_visited[idx]
		xMax, yMax := D_maxmin[idx][0], D_maxmin[idx][1]
		Sum := 0
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if B[i*N+j] >= 1 {
					Sum++
				}
			}
		}
		for i := 0; i < N-xMax; i++ {
			for j := 0; j < N-yMax; j++ {
				if visited[i*N+j] {
					continue
				}
				flag := true
				for _, coord := range shape {
					x, y := coord[0], coord[1]
					if i+x >= 0 && i+x < N && j+y >= 0 && j+y < N && (B[(i+x)*N+(j+y)] <= -100 || B[(i+x)*N+(j+y)] >= 1) {
					} else {
						flag = false
						break
					}
				}
				if flag {
					prv_n := make([][2]int, len(prv))
					copy(prv_n, prv)
					prv_n = append(prv_n, [2]int{i, j})
					B_n := make([]int, len(B))
					copy(B_n, B)
					if idx == M-1 {
						for _, coord := range shape {
							x, y := coord[0], coord[1]
							B_n[(i+x)*N+(j+y)]--
						}
						if max(B_n...) <= 0 {
							ans = append(ans, prv_n)
						}
						if len(ans) >= 300000 {
							return false, ans
						}
					} else {
						tmp := 0
						for _, coord := range shape {
							x, y := coord[0], coord[1]
							B_n[(i+x)*N+(j+y)]--
							if B_n[(i+x)*N+(j+y)] >= 0 {
								tmp++
							}
						}
						if max(B_n...) <= M-idx-1 && D_size[idx+1] >= Sum-tmp {
							deq = append(deq, struct {
								idx int
								B   []int
								prv [][2]int
							}{idx + 1, B_n, prv_n})
						}
						if len(deq) >= limit {
							return false, nil
						}
					}
				}
			}
		}
	}
	return true, ans
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
