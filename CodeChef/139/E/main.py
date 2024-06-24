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
    n = II()
    p = LMII()
    max_ = p[0]
    # 必要な値
    diff = []
    # 超えてはいけない値
    lim = [inf]
    for i in p[1:][::-1]:
        # if not lim:
        #     lim.append(i)
        # else:
        lim.append(min(lim[-1], i - 1))
    lim = lim[::-1]
    for i in range(n):
        diff.append(max(0, max_ - p[i]))
        max_ = max(max_, p[i])
    # print(diff)
    # print(lim)
    tmp = [(i, j) for i, j in zip(diff, lim) if i != 0]

    l = [i for i, j in tmp]
    r = [j for i, j in tmp]

    rslt = 0
    if tmp:
        # print((max(l), min(n, min(r))))
        for i in range(max(l), min(n, min(r)) + 1):
            rslt += i
    else:
        for i in range(n + 1):
            rslt += i
    ans.append(rslt)

    pass
for i in ans:
    print(i)
