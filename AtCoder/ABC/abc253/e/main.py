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


n, m, k = MII()

# i番目の数字がjになるときの通り数
dp = [[0] * (m + 2) for _ in range(n)]
dp[0] = [1] * (m + 2)
dp[0][0] = 0
dp[0][-1] = 0
prf_l = list(accumulate(dp[0]))
prf_r = list(accumulate(dp[0][::-1]))
prf_r = prf_r[::-1]


for i in range(1, n):
    for j in range(1, m + 1):
        l, r = prf_l[max(0, j - k)] % mod, prf_r[min(m + 1, j + k)] % mod
        if k == 0:
            dp[i][j] += prf_l[-1] % mod
        else:
            dp[i][j] += (l + r) % mod

    prf_l = list(accumulate(dp[i]))
    prf_r = list(accumulate(dp[i][::-1]))
    prf_r = prf_r[::-1]

print(sum(dp[n - 1]) % mod)
# pprint(dp)
