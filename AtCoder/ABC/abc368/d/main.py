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

n, k = MII()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = MII()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
v = LMII()


def dfs(s):
    visited = [-2] * n
    deq = [s]
    visited[s] = -1
    while deq:
        v = deq.pop()
        for next in g[v]:
            if visited[next] == -2:
                deq.append(next)
                visited[next] = v
    return visited


visited = dfs(v[0] - 1)
# print(visited)
ans = [False] * n


def make_root(t):
    root = []
    while t != -1 and ans[t] == False:
        root.append(t)
        t = visited[t]
    root.reverse()
    return root


for i in v:
    if ans[i - 1] == False:
        root = make_root(i - 1)
        for j in root:
            ans[j] = True
#         print(i, root)
# print(ans)
print(ans.count(True))
