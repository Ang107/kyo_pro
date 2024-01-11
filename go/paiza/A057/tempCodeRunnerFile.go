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
	ans := 0
	var num int
	var tmp int
	tmp = -1
	p_flag := false
	m_flag := false
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
					tmp = -1
				}
			}
		}
		ans = max(ans, tmp)
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
					tmp = -1
				}
			}
		}
		ans = max(ans, tmp)
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
					tmp = -1
				}
			}
			x++
			y++
		}
		ans = max(ans, tmp)
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
					tmp = -1
				}
			}
			x--
			y--
		}
		ans = max(ans, tmp)
	}
	out(ans)
	// use getI(), getS(), getInts(), getF()
}