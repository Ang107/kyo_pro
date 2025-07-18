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


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


n = II()
a = LMII()

plmd = []
for i in range(1, n + 1):
    if i == n:
        plmd.append(a)
    else:
        plmd.append([None] * i)
for i in range(n - 2, -1, -1):
    for j in range(len(plmd[i])):
        x, y = plmd[i + 1][j], plmd[i + 1][j + 1]
        # 太郎さんの手
        if i % 2 == 0:
            plmd[i][j] = max(x, y)
        elif i % 2 == 1:
            plmd[i][j] = min(x, y)

pprint(plmd[0][0])
