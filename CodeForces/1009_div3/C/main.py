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
# setrecursionlimit(10**7)
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

import random

t = II()
ans = []
res = 0
for x in range(100):
    # x = random.randrange(2, 10**9)
    tmp = bin(x)[2:]
    if tmp.count("0") == 0 or tmp.count("1") == 1:
        continue
    print("!", x, bin(x))
    for j in range(1, x):
        tmp = [x, j, x ^ j]
        tmp.sort()
        if tmp[0] + tmp[1] > tmp[2]:
            # res = max(res, j)
            # print(x, bin(x))
            # # print(x, j)
            print(j, bin(j))
            # print(bin(x), bin(j))
            # break
print(res)
# for _ in range(t):
#     x = II()
#     # x = random.randrange(2, 10**9)
#     tmp = bin(x)[2:]
#     if tmp.count("0") == 0 or tmp.count("1") == 1:
#         ans.append(-1)
#     else:
#         res = []
#         added = [False] * 2
#         for i in tmp[::-1]:
#             if i == "0":
#                 if added[int(i)] == False:
#                     res.append("1")
#                 else:
#                     res.append("0")
#             else:
#                 if added[int(i)] == False:
#                     res.append("1")
#                 else:
#                     res.append("0")
#             added[int(i)] = True
#         res = int("".join(res[::-1]), 2)
#         tmp = [x, res, x ^ res]
#         tmp.sort()
#         assert tmp[0] + tmp[1] > tmp[2]
#         ans.append(res)
#         # for i in range(1, x):
#         #     a = [x, i, x ^ i]
#         #     a.sort()
#         #     if a[0] + a[1] > a[2]:
#         #         ans.append(i)
#         #         break


# for i in ans:
#     print(i)
