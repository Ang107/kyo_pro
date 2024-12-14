n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = m
dp = [-1] * (1 << n)
dp[0] = 0
for i in range(n):
    dp[1 << i] = a[i]
for mask in range(1, 1 << n):
    b = mask & (-mask)
    dp[mask] = dp[b] + dp[mask - b]
    ans = min(ans, abs(dp[mask] - m))
print(ans)
