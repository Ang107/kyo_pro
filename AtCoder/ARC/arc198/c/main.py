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

n = II()
a = LMII()
b = LMII()
ans = []


def f(i, j):
    a[i], a[j] = a[j] - 1, a[i] + 1


if sum(a) != sum(b):
    PN()
    exit()
for i in range(n):
    for j in range(i,n):
        if b[i] <= a[j] + (n-j)-1:
            
# for i in range(n - 1):
#     for _ in range(10**4):
#         for k in range(i, n - 1):
#             ans.append((k + 1, k + 2))
#             f(k, k + 1)
#         if max(a[:-1]) <= 0:
#             break
#         ans.append((i + 1, n))
#         f(i, n - 1)
#         # print(i, a)
#     if max(a[:-1]) <= 0:
#         break
# # print(a)
# for i in range(n):
#     while True:
#         if a[-1] - b[i] <= (n - i) - 1:
#             print(a)

#             diff = a[-1] - b[i]
#             ans.append((i + diff - 1 + 1, n))
#             f(i + diff - 1, n - 1)
#             for j in range(i + diff - 2, i - 1, -1):
#                 ans.append((j + 1, j + 2))
#                 f(j, j + 1)
#             print(a)

#             for j in range(i + 1, n - 1):
#                 for _ in range(10**4):
#                     for k in range(j, n - 1):
#                         ans.append((k + 1, k + 2))
#                         f(k, k + 1)
#                     if max(a[i + 1 : -1]) <= 0:
#                         break
#                     ans.append((j + 1, n))
#                     f(j, n - 1)
#                     # print(i, a)
#                 if max(a[i + 1 : -1]) <= 0:
#                     break
#             print(a)

#             break
#         else:
#             for j in range(n - 2, i - 1, -1):
#                 ans.append((j + 1, j + 2))
#                 f(j, j + 1)
#             ans.append((i + 1, n))
#             f(i, n - 1)
#             # print(a)
