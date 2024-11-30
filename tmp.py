n, m = map(int, input().split())
a = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    mask = 0
    for i in range(n):
        mask |= tmp[i] << i
    a.append(mask)
# dp[i][j]: i番目までのクーポンで集合jの品物を無料で貰えるときの使うクーポンの枚数の最小値
dp = [[1 << 60] * (1 << n) for _ in range(m + 1)]
dp[0][0] = 0
for i in range(m):
    for j in range(1 << n):
        # 使わない
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        # 使う
        dp[i + 1][j | a[i]] = min(dp[i + 1][j | a[i]], dp[i][j] + 1)
if dp[m][(1 << n) - 1] == 1 << 60:
    ans = -1
else:
    ans = dp[m][(1 << n) - 1]
print(ans)
