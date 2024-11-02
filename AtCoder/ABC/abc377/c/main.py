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
# n, m = MII()
# cand = set()
# for _ in range(m):
#     a, b = MII()
#     a -= 1
#     b -= 1
#     cand.add((a, b))
#     cand.add((a + 2, b + 1))
#     cand.add((a + 1, b + 2))
#     cand.add((a - 1, b + 2))
#     cand.add((a - 2, b + 1))
#     cand.add((a - 2, b - 1))
#     cand.add((a - 1, b - 2))
#     cand.add((a + 1, b - 2))
#     cand.add((a + 2, b - 1))
# ans = n**2
# for a, b in cand:
#     if a in range(n) and b in range(n):
#         ans -= 1
# print(ans)

n, m = list(map(int, input().split()))
s = set()
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s.add((a, b))
    s.add((a - 1, b - 2))
    s.add((a - 1, b + 2))
    s.add((a + 1, b - 2))
    s.add((a + 1, b + 2))
    s.add((a - 2, b - 1))
    s.add((a - 2, b + 1))
    s.add((a + 2, b - 1))
    s.add((a + 2, b + 1))

ans = n**2
for x, y in s:
    if 0 <= x < n and 0 <= y < n:
        ans -= 1
print(ans)
