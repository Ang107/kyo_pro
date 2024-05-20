ans = []
while True:
    n = int(input())
    if n == 0:
        break
    l = list(map(int, input().split()))
    l.sort()
    a = 1
    r = 0
    for i in range(1, n):
        if l[i] - l[i - 1] == 1:
            a += 1
        else:
            a = 1
        r = max(r, a)
    ans.append(r)
for i in ans:
    print(i)
