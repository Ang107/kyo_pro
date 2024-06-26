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

t = II()
ans = []

for _ in range(t):
    n, m, k = MII()
    a = [LMII() for _ in range(n)]
    b = [list(map(int, input())) for _ in range(n)]
    mult = set()
    height = [0, 0]
    for i in range(n):
        for j in range(m):
            height[b[i][j]] += a[i][j]
    diff = abs(height[0] - height[1])
    new_b = [list(accumulate(i)) for i in b]

    def f(x, y):
        rslt = new_b[x + k - 1][y + k - 1]
        if x - 1 >= 0:
            rslt -= new_b[x - 1][y + k - 1]
        if y - 1 >= 0:
            rslt -= new_b[x + k - 1][y - 1]
        if x - 1 >= 0 and y - 1 >= 0:
            rslt += new_b[x - 1][y - 1]
        return rslt

    for j in range(m):
        for i in range(1, n):
            new_b[i][j] += new_b[i - 1][j]

    for i in range(n - k + 1):
        for j in range(m - k + 1):
            # 雪有りのマスの数、無しのマスの数
            rslt = f(i, j)
            snow = [rslt, k * k - rslt]
            # snow = []
            # for p in range(k):
            #     for q in range(k):
            #         snow[b[i + p][j + q]] += 1
            mult.add(abs(snow[0] - snow[1]))
    mult.discard(0)
    if diff == 0:
        ans.append("Yes")
    elif mult and diff % math.gcd(*mult) == 0:
        ans.append("Yes")
    else:
        ans.append("No")
    # print(diff)
    # print(mult)
    pass
for i in ans:
    print(i)
