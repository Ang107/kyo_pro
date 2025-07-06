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

dp = [[-1] * len(g[i]) for i in range(n)]


def dfs():
    visited = [False] * n
    deq = deque([~0, 0])
    while deq:
        v = deq.pop()
        visited[v] = True
        if v < 0:
            res = [1, 0]
            for next in g[v]:
                if visited[next] == True:
                    res[0] += dp[0][v][0]
                    res[1] += dp[0][v][1] + dp[0][v][0]

        else:
            for next in g[v]:
                if visited[next] == False:
                    deq.append(~next)
                    deq.append(next)
        visited[v] = False
