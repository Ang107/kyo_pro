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


# import numpy as np

a = LMII()
b = LMII()
c = LMII()
d = LMII()
l = [a, b, c, d]


def solve(a, b, c):
    A = a[0] - b[0], a[1] - b[1]
    B = c[0] - b[0], c[1] - b[1]
    if A[0] * B[1] - A[1] * B[0] < 0:
        return True
    else:
        return False


tmp = True
for i in range(4):
    # print(solve(l[i - 1], l[i], l[(i + 1) % 4]))
    tmp &= solve(l[i - 1], l[i], l[(i + 1) % 4])
if tmp:
    PY()
else:
    PN()
