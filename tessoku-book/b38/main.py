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
s = input()
tmp = []
for i in s:
    if not tmp or i != tmp[-1][0]:
        tmp.append([i, 1])
    else:
        tmp[-1][1] += 1

ans = 0
if tmp[0][0] == "A":
    ans += 1
else:
    ans += tmp[0][1] + 1

# print(tmp)
# print(ans)
for idx in range(len(tmp)):
    i, j = tmp[idx]
    if i == "A":
        if idx + 1 != len(tmp):
            ans += (j + 2) * (j - 1) // 2
            ans += max(tmp[idx + 1][1] + 1, j + 1)
            # print("a")
        else:
            ans += (j + 3) * j // 2
            # print("b")
    elif i == "B":
        ans += (j + 1) * j // 2
        # print("c")
    # print(ans)
print(ans)
