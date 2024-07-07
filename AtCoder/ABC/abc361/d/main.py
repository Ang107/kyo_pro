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

n = II()
s = list(input()) + [".", "."]
t = list(input()) + [".", "."]
g = tuple(t)
import time

START = time.perf_counter()

dp = {tuple(s)}
visited = set(tuple(s))
c = 0
while time.perf_counter() - START < 1.8:
    n_dp = set()
    c += 1
    for u in dp:
        # print(u, g)
        if u == g:
            print(c - 1)
            exit()

        for i in range(n + 1):
            if u[i] == "." and u[i + 1] == ".":
                p, q = i, i + 1
                break
        for i in range(n + 1):
            if u[i] != "." and u[i + 1] != ".":
                l, r = i, i + 1
                u_n = list(u)
                u_n[l], u_n[r], u_n[p], u_n[q] = u_n[p], u_n[q], u_n[l], u_n[r]
                u_n = tuple(u_n)
                if u_n not in visited:
                    n_dp.add(u_n)
                    visited.add(u_n)
    dp = n_dp
print(-1)
