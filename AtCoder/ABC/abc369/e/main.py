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
setrecursionlimit(10**7)
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


n, m = MII()
dis = [[inf] * n for _ in range(n)]
g = []
for i in range(m):
    u, v, t = MII()
    u -= 1
    v -= 1
    dis[u][v] = min(dis[u][v], t)
    dis[v][u] = min(dis[v][u], t)
    g.append((u, v, t))
for i in range(n):
    dis[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
# for i in dis:
#     print(i)
q = II()


for _ in range(q):
    min_cost = inf
    k = II()
    b = LMII()
    b = [i - 1 for i in b]
    # 順列全探索
    for i in permutations(b):
        # 向きを全探索
        for j in range(1 << k):
            cost = 0
            for l in range(k):
                if l == 0:
                    if j >> l & 1:
                        cost += dis[0][g[b[l]][0]]
                    else:
                        cost += dis[0][g[b[l]][1]]

                if l == k - 1:
                    if j >> l & 1:
                        cost += dis[g[b[l]][1]][n - 1]
                    else:
                        cost += dis[g[b[l]][0]][n - 1]
                if l < k - 1:
                    if j >> l & 1:
                        if j >> (l + 1) & 1:
                            cost += dis[g[b[l]][1]][g[b[l + 1]][0]]
                        else:
                            cost += dis[g[b[l]][1]][g[b[l + 1]][1]]
                    else:
                        if j >> (l + 1) & 1:
                            cost += dis[g[b[l]][0]][g[b[l + 1]][0]]
                        else:
                            cost += dis[g[b[l]][0]][g[b[l + 1]][1]]
                cost += g[b[l]][2]
            min_cost = min(cost, min_cost)
    print(min_cost)
