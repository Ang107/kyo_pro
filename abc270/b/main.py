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


x, y, z = MII()
# d = {"s": 0, "x": x, "y": y, "z": z}
# tmp = sorted(d.items(), key=lambda x: x[1])
# tmp = [i for i, j in tmp]


if (x > 0 and y > 0 and z > 0) or (x < 0 and y < 0 and z < 0):
    x, y, z = abs(x), abs(y), abs(z)
    if y < z and y < x:
        print(-1)
    else:
        print(abs(x))
else:
    if x < y < 0 < z or z < 0 < y < x:
        print(abs(z) * 2 + abs(x))
    else:
        print(abs(x))
