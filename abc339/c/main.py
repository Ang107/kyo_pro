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


n = II()
a = LMII()


def isOK(mid):
    for i in a:
        mid += i
        # print(mid)
        if mid < 0:
            return False

    return True


def meguru(ng, ok):
    while abs(ok - ng) > 1:

        mid = (ok + ng) // 2
        # print(ng, ok, mid)
        # print(isOK(mid))
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru(-1, 10**18) + sum(a))

# prf = accumulate(a)
# # print(max(0, -min(prf)) + sum(a))
# l = -1
# r = 10**16

# while r - l > 1:
#     mid = (r + l) // 2
#     tmp = mid
#     ok = True
#     for i in a:
#         tmp += i
#         if tmp < 0:
#             ok = False

#     if ok:
#         r = mid
#     else:
#         l = mid


# print(r + sum(a))
