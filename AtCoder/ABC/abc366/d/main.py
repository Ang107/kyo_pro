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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
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

a = [[[0] * n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        tmp = LMII()
        a[i][j] = tmp
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            a[i][j][k] += a[i][j][k - 1]
for i in range(n):
    for j in range(1, n):
        for k in range(n):
            a[i][j][k] += a[i][j - 1][k]
for i in range(1, n):
    for j in range(n):
        for k in range(n):
            a[i][j][k] += a[i - 1][j][k]

q = II()
for _ in range(q):
    lx, rx, ly, ry, lz, rz = [i - 1 for i in LMII()]
    ans = a[rx][ry][rz]
    tmp = 0

    if lx != 0:
        ans -= a[lx - 1][ry][rz]

    if ly != 0:
        ans -= a[rx][ly - 1][rz]
    # print(ans)

    if lz != 0:
        ans -= a[rx][ry][lz - 1]

    if lx != 0 and ly != 0:
        ans += a[lx - 1][ly - 1][rz]
    if ly != 0 and lz != 0:
        ans += a[rx][ly - 1][lz - 1]
    if lz != 0 and lx != 0:
        ans += a[lx - 1][ry][lz - 1]
    if lx != 0 and ly != 0 and lz != 0:
        ans -= a[lx - 1][ly - 1][lz - 1]

    print(ans)
