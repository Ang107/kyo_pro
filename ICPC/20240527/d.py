ans = []
while 1:
    s = input()
    if s == "#":
        break
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1

    bord = []
    for i in s.split("/"):
        tmp = []
        for j in i:
            if j == "b":
                tmp.append("b")
            else:
                tmp.extend(["."] * int(j))
        bord.append(tmp)
    bord[a][b] = "."
    bord[c][d] = "b"
    for i in range(len(bord)):
        bord[i] = "".join(bord[i])
    rslt = []
    for i in bord:
        tmp = []
        for j in i.split("b"):
            if len(j) > 0:
                tmp.append(str(len(j)))
            tmp.append("b")
        tmp.pop()
        tmp.append("/")
        rslt.extend(tmp)

    rslt.pop()
    ans.append("".join(rslt))
for i in ans:
    print(i)
