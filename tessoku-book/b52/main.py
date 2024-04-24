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


n, x = MII()
a = list(input())
# a[x - 1] = "@"
# l, r = x - 2, x
# while l in range(n) and a[l] == ".":
#     a[l] = "@"
#     l -= 1
# while r in range(n) and a[r] == ".":
#     a[r] = "@"
#     r += 1

# print("".join(a))
deq = deque([x - 1])
while deq:
    pos = deq.popleft()
    a[pos] = "@"
    if pos - 1 in range(n) and a[pos - 1] == ".":
        a[pos - 1] = "@"
        deq.append(pos - 1)
    if pos + 1 in range(n) and a[pos + 1] == ".":
        a[pos + 1] = "@"
        deq.append(pos + 1)

print("".join(a))
