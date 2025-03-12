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

n, m, s, t = MII()
s -= 1
t -= 1
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = MII()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


def can_clear():
    cnt1 = 0
    cnt2 = 0
    for i in g:
        if len(g) == 1:
            cnt1 += 1
        elif len(g) == 2:
            cnt2 += 1
        else:
            return True
    if cnt1 == 2:
        return False
    else:
        return True


if not can_clear():
    print(-1)
    exit()


def bfs(s, block=-1):
    visited = [-1] * n
    visited[s] = 0
    frm = [-1] * n
    deq = deque()
    deq.append(s)
    while deq:
        v = deq.popleft()
        for next in g[v]:
            if visited[next] == -1 and next != block:
                visited[next] = visited[v] + 1
                frm[next] = v
                deq.append(next)
    return visited


def get_root(frm, s, g):
    route = [g]
    now = g
    while route[-1] != s:
        now = frm[now]
        route.append(now)
    return route[::-1]


av1 = bfs(s)
bv1 = bfs(t)
av2 = bfs(s,)
bv2 = bfs(t)
