# n, W = map(int, input().split())
# weight = [0] * 110
# value = [0] * 110

# for i in range(n):
#     weight[i], value[i] = map(int, input().split())

# dp = [[0 for _ in range(10010)] for _ in range(110)]

# # DP初期条件: dp[0][w] = 0
# for w in range(W + 1):
#     dp[0][w] = 0

# # DPループ
# for i in range(n):
#     for w in range(W + 1):
#         if w >= weight[i]:
#             dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
#         else:
#             dp[i + 1][w] = dp[i][w]
#         print(dp[i][w])

# print(dp[n][W])
n = int(input())
a = list(map(int,input().split()))
A = int(input())

dp = [[False for _ in range(10010)] for _ in range(110)]

dp[0][0] = True

for i in range(n):
    for j in range(A+1):
    

n, A = map(int, input().split())
a = list(map(int, input().split()))

# DPテーブル
dp = [[False] * (A + 1) for _ in range(n + 1)]

# 初期条件
dp[0][0] = True

for i in range(n):
    for j in range(A + 1):
        dp[i + 1][j] |= dp[i][j]
        if j >= a[i]:
            dp[i + 1][j] |= dp[i][j - a[i]]

if dp[n][A]:
    print("YES")
else:
    print("NO")



