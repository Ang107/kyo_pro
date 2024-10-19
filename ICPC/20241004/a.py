from sys import stdin, setrecursionlimit
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
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

while 1:
    n = II()
    if n == 0:
        break
    a = [LMII() for _ in range(n)]
    a_copy = [i[:] for i in a]
    # 偶数行のスワップ
    for i in range(1, n, 2):
        a[i] = a[i][n // 2 :] + a[i][: n // 2]
    a = list(zip(*a))
    for i in range(n):
        a[i] = list(a[i])
    # 偶数列のスワップ
    for i in range(1, n, 2):
        a[i] = a[i][n // 2 :] + a[i][: n // 2]
    for i in a:
        print(*i)

    # to_index = {}
    # for i in range(n):
    #     for j in range(n):
    #         to_index[a[i][j]] = (i, j)
    # for i in range(n):
    #     for j in range(n):
    #         for p, q in around4:
    #             if i + p in range(n) and j + q in range(n):
    #                 assert (
    #                     abs(
    #                         to_index[a_copy[i][j]][0]
    #                         - to_index[a_copy[i + p][j + q]][0]
    #                     )
    #                     + abs(
    #                         to_index[a_copy[i][j]][1]
    #                         - to_index[a_copy[i + p][j + q]][1]
    #                     )
    #                     >= n // 2
    #                 )
