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


x, a, d, n = MII()
x -= a
ans = []
if d == 0:
    print(abs(x))
elif (d * (n - 1) < x and d > 0) or (d * (n - 1) > x and d < 0):
    print(abs(x - d * (n - 1)))
elif (x < 0 and d > 0) or (x > 0 and d < 0):
    print(abs(x))
else:
    tmp_min, tmp_max = x % d, d - x % d
    if d > 0:
        if x - tmp_min in range(d * (n - 1)):
            ans.append(tmp_min)
        if x + tmp_max in range(d * (n - 1)):
            ans.append(tmp_max)
    if d < 0:
        if x - tmp_min in range(0, d * (n - 1), -1):
            ans.append(tmp_min)
        if x + tmp_max in range(0, d * (n - 1), -1):
            ans.append(tmp_max)

    print(min(ans))
