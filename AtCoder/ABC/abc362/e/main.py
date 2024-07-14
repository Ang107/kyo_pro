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
a = LMII()
ans = [0] * n
ans[0] = n
# ans[1] = n * (n - 1) // 2

# # 長さが2,3,4,..Nの時の等差数列の選び方
# ans += n * (n - 1) // 2

diff = set()
for i in range(n):
    for j in range(i + 1, n):
        diff.add(a[j] - a[i])
trans = {j: i for i, j in enumerate(sorted(diff))}
# i番目がj番目の要素で等差がkの時の個数
# dp = [defaultdict(lambda: 0) for _ in range(n)]

# for i in range(n):
#     # n_dp = [defaultdict(lambda: 0) for _ in range(n + 1)]
#     for j in range(i + 1, n):
#         d = a[j] - a[i]
#         dp[j][d] += 1
# for i in dp:
#     print(i)
m = len(trans)
# print(trans)
# i番目の要素までで、等差がjで、そこまでにとった数がkの時の組の数
dp = [[[0] * (n + 1) for _ in range(m)] for _ in range(n + 1)]
for i in range(n):
    for j in range(i + 1, n):
        d = trans[a[j] - a[i]]
        dp[j][d][2] += 1

for i in range(n):
    # for j in range(m):
    for l in range(n):
        for nxt in range(i + 1, n):
            d = trans[a[nxt] - a[i]]
            dp[nxt][d][l + 1] += dp[i][d][l]
            dp[nxt][d][l + 1] %= mod

for k in range(2, n + 1):
    for i in range(n):
        for j in range(m):
            ans[k - 1] += dp[i + 1][j][k]
            ans[k - 1] %= mod
print(*ans)
