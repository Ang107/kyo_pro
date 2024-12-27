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

n = II()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = MII()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = inf
for i in range(n):
    min_ = inf
    tmp = []
    for j in g[i]:
        tmp.append(len(g[j]) - 1)
    tmp.sort(reverse=True)
    for j in range(len(tmp)):
        res = n - 1 - (j + 1) - tmp[j] * (j + 1)
        ans = min(ans, res)
    # for j in g[i]:
    #     min_ = min(min_, len(g[j]) - 1)
    # print(i, min_)

    # res = n - 1 - len(g[i]) * (min_ + 1)
    # print(i, min_, len(g[i]), res)
    ans = min(ans, res)
print(ans)
