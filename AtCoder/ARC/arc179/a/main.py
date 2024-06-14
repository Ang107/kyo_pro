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

sys.setrecursionlimit(10**7)
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


def solve(n, k, a):
    if k >= 1:
        return sorted(a)
    else:
        if sum(a) < k:
            return []
        else:
            return sorted(a, reverse=True)


def isOK(k, a):
    tmp = [0] + list(accumulate(a))
    flag = False
    for i in tmp:
        if flag and i < k:
            return False
        if i >= k:
            flag = True
    return True


def solve1(n, k, a):
    rslt = False
    ans = []
    for i in permutations(a):
        if isOK(k, i):
            ans = i
            break

    return ans


import random

# n = 10
# k = -6
# a = [10, -15, 79, 76, 68, -74, 19, -53, -56, -57]
# print(sum(a))
# print(solve(n, k, a))
# print(solve1(n, k, a))
# while True:
#     n = 10
#     k = random.choice(range(-10, 10))
#     a = [random.choice(range(-100, 100)) for _ in range(n)]
#     ans = solve(n, k, a)
#     # print(ans)
#     ans1 = solve1(n, k, a)
#     # print(ans1)
#     print(bool(ans), solve1(n, k, a))
#     if bool(ans) != solve1(n, k, a):
#         print(n, k, a, ans)
#         break

n, k = MII()
a = LMII()
ans = solve(n, k, a)
if ans:
    PY()
    pritn(*ans)
else:
    PN()
