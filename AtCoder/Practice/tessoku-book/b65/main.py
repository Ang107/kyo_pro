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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")


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


n, t = MII()
t -= 1
ab = []
ed = [set() for _ in range(n)]
for _ in range(n - 1):
    a, b = MII()
    a -= 1
    b -= 1
    ed[a].add(b)
    ed[b].add(a)
from functools import cache


@cache
def f(v):
    if len(ed[v]) == 0:
        return 0
    rslt = 0
    for nxt in ed[v]:
        ed[nxt].remove(v)
        rslt = max(rslt, 1 + f(nxt))
    return rslt


f(t)
ans = [f(i) for i in range(n)]
print(*ans)
