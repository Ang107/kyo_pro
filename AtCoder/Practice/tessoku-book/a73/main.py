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
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x):
    return print(x)


def PY():
    return print("Yes")


def PN():
    return print("No")


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


n, m = MII()
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c, d))
    g[b].append((a, c, d))
# 総距離、-木の総数、頂点
heap = [(0, 0, 0)]
dis = [(inf, inf)] * n
dis[0] = (0, 0)
while heap:
    sum_d, sum_t, v = heappop(heap)
    if (sum_d, sum_t) > dis[v]:
        continue
    for nxt, d, t in g[v]:
        if (sum_d + d, sum_t - t) < dis[nxt]:
            heappush(heap, (sum_d + d, sum_t - t, nxt))
            dis[nxt] = (sum_d + d, sum_t - t)
print(dis[n - 1][0], -dis[n - 1][1])
