import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
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

n = II()
c = [input() for _ in range(n)]
# マスi,jに到達するまでに使用した色変換の回数の最小値
dp = [[inf] * n for _ in range(n)]
dp[0][0] = 0

heap = [(0, 0, 0)]
while heap:
    w, x, y = heappop(heap)
    if dp[x][y] < w:
        continue
    for i, j in around4:
        if x + i in range(n) and y + j in range(n):
            if c[x + i][y + j] == "R":
                if dp[x][y] < dp[x + i][y + j]:
                    dp[x + i][y + j] = dp[x][y]
                    heappush(heap, (dp[x + i][y + j], x + i, y + j))
            else:
                if dp[x][y] + 1 < dp[x + i][y + j]:
                    dp[x + i][y + j] = dp[x][y] + 1
                    heappush(heap, (dp[x + i][y + j], x + i, y + j))
ans = 0
ans += dp[n - 1][n - 1]

# マスi,jに到達するまでに使用した色変換の回数の最小値
dp = [[inf] * n for _ in range(n)]
dp[0][n - 1] = 0

heap = [(0, 0, n - 1)]
while heap:
    w, x, y = heappop(heap)
    if dp[x][y] < w:
        continue
    for i, j in around4:
        if x + i in range(n) and y + j in range(n):
            if c[x + i][y + j] == "B":
                if dp[x][y] < dp[x + i][y + j]:
                    dp[x + i][y + j] = dp[x][y]
                    heappush(heap, (dp[x + i][y + j], x + i, y + j))
            else:
                if dp[x][y] + 1 < dp[x + i][y + j]:
                    dp[x + i][y + j] = dp[x][y] + 1
                    heappush(heap, (dp[x + i][y + j], x + i, y + j))
ans += dp[n - 1][0]

pritn(ans)
