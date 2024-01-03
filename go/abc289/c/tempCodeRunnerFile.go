func main() {
	defer wr.Flush()
	sc.Split(bufio.ScanWords)
	sc.Buffer([]byte{}, math.MaxInt32)
	n, m := getI(), getI()
	a := make([][]int, m)
	ans := 0
	for i := 0; i < m; i++ {
		c := getI()
		temp := getInts(c)
		a[i] = temp
	}
	for mask := 0; mask < (1 << m); mask++ {
		temp := make(map[int]bool)
		flag := true
		for i := 0; i < n; i++ {
			if (mask>>i)&1 == 1 {
				for _, j := range a[i] {
					temp[j] = true
				}
			}
		}
		for i := 1; i <= n; i++ {
			if inMap(temp, i) {

			} else {
				flag = false
			}
		}
		if flag {
			ans += 1
		}
	}
	out(ans)
	// use getI(), getS(), getInts(), getF()
}