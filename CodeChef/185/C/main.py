from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

t = II()

memo = [[[0] * 30 for _ in range(30)] for _ in range(30)]


# @cache
def f(turn, l):
    i, j, k = l
    # print(i, j, k)
    if memo[i][j][k] != 0:
        return memo[i][j][k]
    if l == [0, 0, 0]:
        if turn % 2 == 0:
            return 1
        else:
            return -1
    if turn % 2 == 1:
        res = 1
        for i in range(3):
            if l[i] == 0:
                continue
            if i == 0:
                l[i] -= 1
                res = min(res, f(turn + 1, l))
                l[i] += 1
            else:
                l[i] -= 1
                l[i - 1] += 1
                res = min(res, f(turn + 1, l))
                l[i] += 1
                l[i - 1] -= 1

    else:
        res = -1
        for i in range(3):
            if l[i] == 0:
                continue
            if i == 0:
                l[i] -= 1
                res = max(res, f(turn + 1, l))
                l[i] += 1
            elif i == 1:
                l[i] -= 1
                l[i - 1] += 1
                res = max(res, f(turn + 1, l))
                l[i] += 1
                l[i - 1] -= 1
            else:
                l[i] -= 1
                l[i - 2] += 1
                res = max(res, f(turn + 1, l))
                l[i] += 1
                l[i - 2] -= 1
    i, j, k = l
    memo[i][j][k] = res
    return res


for i in range(10):
    for j in range(10):
        for k in range(10):
            print(i, j, k, f(0, [i, j, k]))
# for _ in range(t):

#     ans = 0
#     n = II()

#     a = LMII()
#     sum_ = sum(a)

#     cnt = [0, 0, 0, 0]
#     ans = 0
#     for i in a:
#         cnt[i] += 1


#     if cnt[3] % 2 == 1:
#         if (cnt[1] + cnt[2]) % 2 == 0:
#             pass
#         else:

#     else:

#     # win = [False] * 4
#     # for i in range(1, 4):
#     #     cnt[i] -= 1
#     #     if can_win():
#     #         ans += cnt[i] + 1
#     #     cnt[i] += 1
