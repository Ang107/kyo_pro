def solve(n, a):
    if n <= 3:
        return a
    if i % 2 == 0:
        for i in range(n // 2):
            a[i][i], a[i - (-n // 2)][i - (-n // 2)] = (
                a[i - (-n // 2)][i - (-n // 2)],
                a[i][i],
            )

            j = 1
            while i + j in range(n) and i - j in range(n):
                a[i + j][i - j], a[-1 - (i + j)][-1 - (i - j)] = (
                    a[-1 - (i + j)][-1 - (i - j)],
                    a[i + j][i - j],
                )

                a[i - j][i + j], a[-1 - (i - j)][-1 - (i + j)] = (
                    a[-1 - (i - j)][-1 - (i + j)],
                    a[i - j][i + j],
                )

                j += 1
    else:
        
    return a
    pass


ans = []
while 1:
    n = int(input())
    if n == 0:
        break
    a = [list(map(int, input().split())) for _ in range(n)]
    ans.append(solve(n, a))

for i in ans:
    for j in i:
        print(*j)
