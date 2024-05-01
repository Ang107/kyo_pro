import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n, m, k, s, t, x = MII()
x -= 1
s -= 1
t -= 1
ed = [[] for _ in range(n)]
for i in range(m):
    u, v = MII()
    ed[u - 1].append(v - 1)
    ed[v - 1].append(u - 1)

dp = [[[0] * 2 for _ in range(n)] for _ in range(k + 1)]
dp[0][s][0] = 1

for i in range(1, k + 1):
    for j in range(n):
        for l in ed[j]:
            if j == x:
                dp[i][j][0] += dp[i - 1][l][1]
                dp[i][j][1] += dp[i - 1][l][0]
            else:
                dp[i][j][0] += dp[i - 1][l][0]
                dp[i][j][1] += dp[i - 1][l][1]
            dp[i][j][0] %= mod
            dp[i][j][1] %= mod
print(dp[k][t][0])
