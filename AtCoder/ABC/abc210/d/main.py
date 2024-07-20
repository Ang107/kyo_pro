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


h, w, c = MII()
a = [LMII() for _ in range(h)]


def f(a):
    dp = [[inf] * w for _ in range(h)]
    for i in reversed(range(h)):
        for j in reversed(range(w)):
            if i == j == 0:
                continue
            dp[i][j] = c * (i + j) + a[i][j]
            if i + 1 in range(h):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + c)
            if j - 1 in range(w):
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + c)
    rslt = inf
    print(dp)
    for i in range(h):
        for j in range(w):
            if i == j == 0:
                continue
            rslt = min(rslt, a[i][j] + dp[h - 1][w - 1] - c * (i + j))
    return rslt


a_rev = [i[::-1] for i in a]
ans = min(f(a), f(a_rev))
print(ans)
