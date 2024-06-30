ans = []
while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    ans.append(n * m)
for i in ans:
    print(i)
