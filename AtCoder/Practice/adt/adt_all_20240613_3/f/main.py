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

n, m = MII()


def solve(n, m):
    ans = []
    if n == 1:
        for a in range(1, m + 1):
            ans.append((a,))
    elif n == 2:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                ans.append((a, b))
    elif n == 3:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    ans.append((a, b, c))
    elif n == 4:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    for d in range(c + 1, m + 1):
                        ans.append((a, b, c, d))
    elif n == 5:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    for d in range(c + 1, m + 1):
                        for e in range(d + 1, m + 1):
                            ans.append((a, b, c, d, e))
    elif n == 6:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    for d in range(c + 1, m + 1):
                        for e in range(d + 1, m + 1):
                            for f in range(e + 1, m + 1):
                                ans.append((a, b, c, d, e, f))
    elif n == 7:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    for d in range(c + 1, m + 1):
                        for e in range(d + 1, m + 1):
                            for f in range(e + 1, m + 1):
                                for g in range(f + 1, m + 1):
                                    ans.append((a, b, c, d, e, f, g))
    elif n == 8:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    for d in range(c + 1, m + 1):
                        for e in range(d + 1, m + 1):
                            for f in range(e + 1, m + 1):
                                for g in range(f + 1, m + 1):
                                    for h in range(g + 1, m + 1):
                                        ans.append((a, b, c, d, e, f, g, h))

    elif n == 9:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    for d in range(c + 1, m + 1):
                        for e in range(d + 1, m + 1):
                            for f in range(e + 1, m + 1):
                                for g in range(f + 1, m + 1):
                                    for h in range(g + 1, m + 1):
                                        for i in range(h + 1, m + 1):
                                            ans.append((a, b, c, d, e, f, g, h, i))

    elif n == 10:
        for a in range(1, m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    for d in range(c + 1, m + 1):
                        for e in range(d + 1, m + 1):
                            for f in range(e + 1, m + 1):
                                for g in range(f + 1, m + 1):
                                    for h in range(g + 1, m + 1):
                                        for i in range(h + 1, m + 1):
                                            for j in range(i + 1, m + 1):
                                                ans.append(
                                                    (a, b, c, d, e, f, g, h, i, j)
                                                )

    for i in ans:
        print(*i)


solve(n, m)
# for n in range(1, 11):
#     for m in range(n, 11):
#         solve(n, m)
