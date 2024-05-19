ans_l = []
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    b = [[None] * w for _ in range(h)]
    for _ in range(w + h - 1):
        i, j, x = map(int, input().split())
        i -= 1
        j -= 1
        b[j][i] = x

    t = [None] * w
    l = [None] * h
    t[0] = 0

    kakutei_t = [0]
    kakutei_l = []
    while kakutei_t or kakutei_l:
        if kakutei_t:
            j = kakutei_t.pop()
            for i in range(h):
                if b[i][j] != None and l[i] == None:
                    l[i] = b[i][j] - t[j]
                    kakutei_l.append(i)
        if kakutei_l:
            i = kakutei_l.pop()
            for j in range(w):
                if b[i][j] != None and t[j] == None:
                    t[j] = b[i][j] - l[i]
                    kakutei_t.append(j)
    flag = True

    for i in range(h):
        for j in range(w):
            if b[i][j] == None:
                if l[i] != None and t[j] != None:
                    pass
                else:
                    flag = False

    if flag:
        ans_l.append("YES")
    else:
        ans_l.append("NO")


for i in ans_l:
    print(i)
