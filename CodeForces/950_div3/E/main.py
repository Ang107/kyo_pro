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
    n, m = MII()
    a = [LMII() for _ in range(n)]
    b = [LMII() for _ in range(n)]
    a_idx = [None] * (n * m + 1)
    b_idx = [None] * (n * m + 1)
    # 値からidx
    for i in range(n):
        for j in range(m):
            a_idx[a[i][j]] = (i, j)

    for i in range(n):
        for j in range(m):
            b_idx[b[i][j]] = (i, j)

    # print(a_idx)
    # print(b_idx)
    ok = True

    # 横に同じ行にあるか
    for i in range(n):
        tmp = set()
        for j in range(m):
            tmp.add(b_idx[a[i][j]][0])
            if len(tmp) > 1:
                ok = False
                break

    # 縦に同じ列にあるか
    for j in range(m):
        tmp = set()
        for i in range(n):
            tmp.add(b_idx[a[i][j]][1])
            if len(tmp) > 1:
                ok = False
                break
    if ok:
        ans.append("Yes")
    else:
        ans.append("No")
    pass
for i in ans:
    print(i)
