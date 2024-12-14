from sys import stdin

# import pypyjit

# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = 1 << 60
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, K = MII()
xy = [LMII() for _ in range(n)]

d = [0] * (1 << n)
for i in range(1 << n):
    res = 0
    tmp = []
    for j in range(n):
        if i >> j & 1:
            tmp.append(j)
    for j in range(len(tmp)):
        for k in range(len(tmp)):
            ux, uy = xy[tmp[j]]
            vx, vy = xy[tmp[k]]
            res = max(res, (ux - vx) ** 2 + (uy - vy) ** 2)
    d[i] = res
# 既に選んだ点の集合がiで、グループ数がjの時の、スコアの最小値
dp = [[inf] * (1 << n) for _ in range(K + 1)]
dp[0][0] = 0

for cnt in range(1, K + 1):
    for s in range(1, 1 << n):
        t = s
        while t != 0:
            dp[cnt][s] = min(dp[cnt][s], max(dp[cnt - 1][s - t], d[t]))
            t = (t - 1) & s
print(dp[K][(1 << n) - 1])
