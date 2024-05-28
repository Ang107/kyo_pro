ans = []
while 1:
    n, m = map(int, input().split())
    if n == 0:
        break
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tmp = []
    for i in a:
        for j in b:
            tmp.append(str(i * j))
    rslt = [0] * 10
    for i in tmp:
        for j in range(10):
            rslt[j] += i.count(str(j))
    ans.append(rslt)
for i in ans:
    print(*i)
