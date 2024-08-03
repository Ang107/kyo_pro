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


n = II()
st = [input().split() for _ in range(n)]
ans = []
for correct in range(10000):
    correct = f"{correct:04}"
    f = True
    for s, t in st:
        if t == "1":
            if s == correct:
                pass
            else:
                f = False
        elif t == "2":
            if len([i for i, j in zip(correct, s) if i != j]) == 1:
                pass
            else:
                f = False
        elif t == "3":
            if len([i for i, j in zip(correct, s) if i != j]) >= 2:
                pass
            else:
                f = False
    if f:
        ans.append(correct)
# print(ans)
if len(ans) == 1:
    print(ans[0])
else:
    print("Can't Solve")
