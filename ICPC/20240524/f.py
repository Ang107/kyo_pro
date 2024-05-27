ans = []
while True:
    T, D, L = map(int, input().split())
    if T == 0:
        break
    X = [int(input()) for _ in range(T)]
    rslt = 0
    over_time = -1000000
    for time, i in enumerate(X[:-1]):
        # print(L, i, L <= i)
        if L <= i:
            over_time = time
        if over_time + D > time:
            rslt += 1
    ans.append(rslt)

for i in ans:
    print(i)
