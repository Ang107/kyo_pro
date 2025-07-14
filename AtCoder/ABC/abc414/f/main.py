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
    n, k = MII()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = MII()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    ng = [[] for _ in range(n)]
    visited = [-1] * n
    dis = [-1] * n
    for i in range(n):
        deq = deque([i])
        visited[i] = i
        dis[i] = 0
        while deq:
            v = deq.popleft()
            for next in g[v]:
                if visited[next] == i:
                    continue
                visited[next] = i
                dis[next] = dis[v] + 1
                if dis[next] == k:
                    ng[i].append(next)
                else:
                    deq.append(next)

    visited = [inf] * n
    deq = deque([0])
    visited[0] = 0
    while deq:
        v = deq.popleft()
        for next in ng[v]:
            if visited[next] != inf:
                continue
            visited[next] = visited[v] + 1
            deq.append(next)

    ans = [-1] * (n - 1)
    for i in range(1, n):
        if visited[i] != inf:
            ans[i - 1] = visited[i]
    print(*ans)
