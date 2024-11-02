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
# s = [list(input()) for _ in range(8)]
# for i in range(8):
#     for j in range(8):
#         if s[i][j] == "#":
#             for p in range(8):
#                 if s[p][j] != "#":
#                     s[p][j] = "x"
#             for q in range(8):
#                 if s[i][q] != "#":
#                     s[i][q] = "x"
# ans = 0
# for i in range(8):
#     for j in range(8):
#         if s[i][j] == ".":
#             ans += 1
# # for i in s:
# #     print(i)
# print(ans)

# ss = []
# for _ in range(8):
#     s = input()
#     ss.append(list(s))

ss = [i * 2 for i in range(8)]
print(ss)
# _ = 1
# print(_)
# cnt = 0
# for i in range(8):
#     for j in range(8):
#         if ss[i][j] == ".":
#             ok = True
#             # 上下に # のマスが存在するか確認
#             for k in range(8):
#                 if ss[k][j] == "#":
#                     ok = False
#             # 左右に # のマスが存在するか確認
#             for k in range(8):
#                 if ss[i][k] == "#":
#                     ok = False
#             if ok:
#                 cnt += 1
# print(cnt)

# for i in range(8):
#     for j in range(8):
#         if ss[i][j] == "#":
#             for k in range(8):
#                 if ss[k][j] == ".":
#                     ss[k][j] = "x"
#             for k in range(8):
#                 if ss[i][k] == ".":
#                     ss[i][k] = "x"
# for i in range(8):
#     print(ss[i])
# cnt = 0
# for i in range(8):
#     for j in range(8):
#         if ss[i][j] == ".":
#             cnt += 1
# print(cnt)
