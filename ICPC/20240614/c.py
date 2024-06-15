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

def solve(m,n_min,n_max,p):
    max_gap = -1
    idx = 0
    for i in range(n_min, n_max + 1):
        saitei = p[i-1]
        saikou = p[i]
        gap = saitei - saikou
        if max_gap <= gap:
            max_gap = gap
            idx = i
    return idx
    pass

ans = []

while 1:
    m,n_min,n_max = MII()
    if m == n_min == n_max == 0:
        break
    p = [II() for _ in range(m)]
    ans.append(solve(m, n_min, n_max, p))
    pass

for i in ans:
    print(i)