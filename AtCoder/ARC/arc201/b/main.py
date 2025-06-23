from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


t = II()
for _ in range(t):

    @cache
    def f(w, i):

        pass

    n, w = MII()
    xy = [LMII() for _ in range(n)]
    g = [[] for _ in range(60)]
    for x, y in xy:
        g[x].append(y)
    for i in range(60):
        g[i].append(0)
        g[i].sort(reverse=True)
    for i in range(60):
        for j in range(1, len(g[i])):
            g[i][j] += g[i][j - 1]
    sum_w = [0] * 60
    for i in range(60):
        if i == 0:
            sum_w[i] = 2**i * (len(g[i]) - 1)
        else:
            sum_w[i] = sum_w[i - 1] + 2**i * (len(g[i]) - 1)

    dp = defaultdict(int)
    dp[0] = 0
    # print(sum_w)
    # print(g)
    for i in reversed(range(60)):
        ndp = defaultdict(int)

        for k, v in dp.items():
            if i == 0:
                s = min(len(g[i]) - 1, (w - k) // 2**i)
            else:
                s = min(len(g[i]) - 1, (w - k - sum_w[i - 1]) // 2**i)
            s = max(0, s - 1)
            # print(k, v, i, s)
            if s == 0:
                ndp[k] = max(ndp[k], dp[k])
            for j in range(s, len(g[i])):
                if k + (j + 1) * (1 << i) <= w:
                    # print(i, j)
                    ndp[k + (j + 1) * (1 << i)] = max(
                        ndp[k + (j + 1) * (1 << i)], dp[k] + g[i][j]
                    )
                else:
                    break
        dp = ndp
        print(len(dp))
    print(max(dp.values()))
