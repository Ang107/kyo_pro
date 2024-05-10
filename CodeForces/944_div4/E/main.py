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
test = []
for _ in range(t):
    n, k, q = MII()
    a = [0] + LMII()
    b = [0] + LMII()
    r = []

    for _ in range(q):
        d = II()
        idx = bisect_right(a, d) - 1
        if idx == k:
            test.append(b[-1])
            r.append(b[-1])
        else:
            # v = (a[idx + 1] - a[idx]) / (b[idx + 1] - b[idx])
            # test.append(b[idx] + (d - a[idx]) / v)
            r.append(
                int(
                    b[idx]
                    + (d - a[idx]) * (b[idx + 1] - b[idx]) // (a[idx + 1] - a[idx])
                )
            )
    ans.append(r)
for i in ans:
    print(*i)
# print(test)
