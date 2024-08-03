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


def solve(n, x, y, ab):
    # 甘さがiで食べた枚数がjの時の、しょっぱさの最小値
    dp = [[inf] * (n + 1) for _ in range(x + 2)]
    dp[0][0] = 0
    for a, b in ab:
        ndp = [[inf] * (n + 1) for _ in range(x + 2)]
        for i in range(x + 1):
            for j in range(n + 1):
                # 食べない
                ndp[i][j] = min(ndp[i][j], dp[i][j])
                # 食べる
                if dp[i][j] <= y:
                    ndp[min(x + 1, i + a)][j + 1] = min(
                        ndp[min(x + 1, i + a)][j + 1], dp[i][j] + b
                    )
        dp = ndp
    ans = 0
    for i in range(x + 2):
        for j in range(n + 1):
            if dp[i][j] != inf:
                if dp[i][j] <= y and i <= x:
                    ans = max(ans, j + 1)
                else:
                    ans = max(ans, j)
    return min(n, ans)


def native(n, x, y, ab):
    ans = 0

    for i in range(1 << n):
        cnt = 0
        p, q = 0, 0
        for j in range(n):
            if i >> j & 1:
                cnt += 1
                p += ab[j][0]
                q += ab[j][1]
                if p > x or q > y:
                    break
        ans = max(ans, cnt)
    return ans


import random

if 0:
    while True:
        n = 7
        x = random.randrange(1, 100)
        y = random.randrange(1, 100)
        ab = [(random.randrange(1, 100), random.randrange(1, 100)) for _ in range(n)]
        r1, r2 = solve(n, x, y, ab), native(n, x, y, ab)
        print(r1, r2)
        if r1 != r2:
            print(x, y)
            for i in ab:
                print(i)
            exit()

else:
    n, x, y = MII()
    ab = [LMII() for _ in range(n)]
    print(solve(n, x, y, ab))
    # print(native(n, x, y, ab))
