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

h, w = MII()

s = [input() for _ in range(h)]
# black = [[0] * (w + 1) for _ in range(h + 1)]
# white = [[0] * (w + 1) for _ in range(h + 1)]
b_min_x, b_min_y = h - 1, w - 1
b_max_x, b_max_y = 0, 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            b_min_x = min(b_min_x, i)
            b_min_y = min(b_min_y, j)
            b_max_x = max(b_max_x, i)
            b_max_y = max(b_max_y, j)
for i in range(b_min_x, b_max_x + 1):
    for j in range(b_min_y, b_max_y + 1):
        if s[i][j] == ".":
            PN()
            exit()
PY()
#     black[i][j] = 1
# elif s[i][j] == ".":
#     white[i][j] = 1
# for i in range(h):
#     for j in range(w):
#         black[i + 1][j] += black[i][j]
#         white[i + 1][j] += white[i][j]
# for i in range(h):
#     for j in range(w):
#         black[i][j + 1] += black[i][j]
#         white[i][j + 1] += white[i][j]
