from sys import stdin, setrecursionlimit
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
# setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


t = II()
anss = []

for _ in range(t):
    n = II()
    a = LMII()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = MII()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    def dfs():
        deq = [0]
        visited = [-1] * n
        visited[0] = 0
        res = [-1] * n
        res[0] = a[0]
        while deq:
            v = deq.pop()
            for next in g[v]:
                if visited[next] != -1:
                    continue
                visited[next] = visited[v] ^ 1
                if visited[v] == 0:
                    res[next] = res[v] - a[next]
                else:
                    res[next] = res[v] + a[next]
                deq.append(next)
        return res, visited

    res, dis = dfs()
    # print(dis)
    for i in range(n):
        if dis[i] == 0:
            pass
        else:
            res[i] *= -1
    g_minmax = [[0, 0] for _ in range(n)]
    k_minmax = [[0, 0] for _ in range(n)]
    g_minmax[0][0] = min(g_minmax[0][0], res[0])
    g_minmax[0][1] = max(g_minmax[0][1], res[0])
    deq = [0]
    visited = [-1] * n
    visited[0] = 0
    ans = [-1] * n
    ans[0] = a[0]
    # print(res)
    while deq:
        v = deq.pop()
        # k_ = k_minmax[:]
        # g_ = g_minmax[:]
        # print(v)
        # print(k_)
        # print(g_)
        for next in g[v]:
            if visited[next] != -1:
                continue
            if dis[next] == 1:
                # print(next, k_minmax, g_minmax)
                ans[next] = max(res[next] - k_minmax[v][0], res[next] + g_minmax[v][1])
                k_minmax[next][0] = min(k_minmax[next][0], k_minmax[v][0], res[next])
                k_minmax[next][1] = max(k_minmax[next][1], k_minmax[v][1], res[next])
                g_minmax[next][0] = min(g_minmax[next][0], g_minmax[v][0])
                g_minmax[next][1] = max(g_minmax[next][1], g_minmax[v][1])
            else:
                # print(next, k_minmax, g_minmax)
                ans[next] = max(res[next] - g_minmax[v][0], res[next] + k_minmax[v][1])
                g_minmax[next][0] = min(g_minmax[next][0], g_minmax[v][0], res[next])
                g_minmax[next][1] = max(g_minmax[next][1], g_minmax[v][1], res[next])
                k_minmax[next][0] = min(k_minmax[next][0], k_minmax[v][0])
                k_minmax[next][1] = max(k_minmax[next][1], k_minmax[v][1])
            visited[next] = True
            deq.append(next)
    anss.append(ans)
    pass
for i in anss:
    print(*i)
