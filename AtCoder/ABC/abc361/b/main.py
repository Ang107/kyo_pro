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

a, b, c, d, e, f = MII()
g, h, i, j, k, l = MII()

x = False
y = False
z = False
for p in range(1001):
    if a <= p < d and g <= p < j:
        x = True
for p in range(1001):
    if b <= p < e and h <= p < k:
        y = True

for p in range(1001):
    if c <= p < f and i <= p < l:
        z = True
if x and y and z:
    PY()
else:
    PN()

# if (d > g and e > h and f > i) or (j > g and l > h and f > i):
#     PY()
# else:
#     PN()
