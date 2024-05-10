import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


t = II()
ans = []


def isOK(mid, x, r):
    return x + mid**2 < r


def meguru(ng, ok, x, r):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid, x, r):
            ok = mid
        else:
            ng = mid
    return ok


def f(r):
    a = 0
    for x in range(0, r):
        tmp = meguru(r, 0, x**2, r**2) + 1
        a += tmp
        # a += r - x
        # for y in range(r - x, r + 1):
        #     # print(x, y, x**2 + y**2 < r**2)
        #     if x**2 + y**2 < r**2:
        #         a += 1
        #     else:
        #         break
    a *= 4
    a -= 4 * (r - 1)
    a -= 3
    return a


for _ in range(t):
    r = II()

    ans.append(f(r + 1) - f(r))
for i in ans:
    print(i)
