ans = []


def solve(n, m, p, x):
    pass


while 1:
    n, m, p = map(int, input().split())
    if n == m == p:
        break
    x = [int(input()) for _ in range(n)]
    sum_ = sum(x)
    tmp = sum_ * (100 - p)
    if x[m - 1] == 0:
        ans.append(0)
    else:
        ans.append(tmp // x[m - 1])
for i in ans:
    print(i)
