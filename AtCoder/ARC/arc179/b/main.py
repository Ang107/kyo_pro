import sys


# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

m, n = MII()
x = LMII()
x = [i - 1 for i in x]
tmp = [0] * (m)
for i in range(m):
    tmp[x[i]] |= 1 << i
# i個目までで使用可能な数字の集合がjの時の通り数
dp = [[0] * (1 << m) for _ in range(n + 1)]
dp[0][(1 << m) - 1] = 1
for i in range(n):
    for j in range(1 << m):
        for k in range(m):
            if j >> k & 1:
                dp[i + 1][j - (2**k) | tmp[k]] += dp[i][j]
                dp[i + 1][j - (2**k) | tmp[k]] %= mod
ans = 0
for i in range(1 << m):
    ans += dp[n][i]
    ans %= mod
pritn(ans)
