ans = []
while 1:
    n,m = map(int,input().split())
    if n == 0:
        break
    sum_ = [0] * n
    for i in range(m):
        p = list(map(int,input().split()))
        for j in range(n):
            sum_[j] += p[j]
    # print(sum_)
    ans.append(max(sum_))
for i in ans:
    print(i)