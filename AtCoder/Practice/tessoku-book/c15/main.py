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
k = II()
lr = [tuple(map(int, input().split())) for _ in range(n)]
lr_c = lr.copy()
lr.sort(key=lambda x: x[0])
t_l = [0] * 86402

i = 0
for t in range(86400):
    while i < n and lr[i][0] == t:

        t_l[lr[i][1]] = max(t_l[lr[i][1]], t_l[max(0, lr[i][0] - k)] + 1)
        i += 1
        # print(t_l[lr[i][1]])
    t_l[t + 1] = max(t_l[t + 1], t_l[t])

lr.sort(key=lambda x: x[1])

t_r = [0] * 86402
i = n - 1
for t in reversed(range(1, 86401)):
    while i >= 0 and lr[i][1] == t:
        t_r[lr[i][0]] = max(t_r[lr[i][0]], t_r[min(86401, t + k)] + 1)
        i -= 1
    t_r[t - 1] = max(t_r[t - 1], t_r[t])
# print(t_l[:10])
# print(t_r[:10])
ans = 0
for l, r in lr_c:
    ans = 1 + t_l[max(0, l - k)] + t_r[min(r + k, 86401)]
    print(ans)
