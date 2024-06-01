ans = []
while 1:
    w,h,n,d,b = map(int,input().split())
    if w == 0:
        break
    xy = [list(map(int,input().split())) for _ in range(n)]
    xy = [(i-1,j-1) for i,j in xy]
    l = [xy[b-1]]
    b = [["."] * h for _ in range(w)]
    rslt = 0
    for x,y in xy:
        b[x][y] = "#"
    # print(b)
    while l:
        # print(l)
        x,y = l.pop()
        for i in range(-d,d+1,1):
            # print(i)
            if x+i in range(w) and y in range(h) and b[x+i][y] == "#":
                l.append((x+i,y))
                b[x+i][y] = "."
                rslt += 1

        for i in range(-d,d+1,1):
            if x in range(w) and y+i in range(h) and b[x][y+i] == "#":
                l.append((x,y+i))
                b[x][y+i] = "."
                rslt += 1
    ans.append(rslt)
    # print(b)
for i in ans:
    print(i)
