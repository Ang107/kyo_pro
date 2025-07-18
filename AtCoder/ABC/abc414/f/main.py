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
inf = 1 << 60
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
MASK = (1 << 32) - 1


def h(v, frm):
    return v << 32 | frm


def restore(hashed):
    return hashed >> 32, hashed & MASK


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
    # 考える辺
    visited = []
    for i in range(n):
        visited.append([[inf] * k for _ in range(len(g[i]) + 1)])

    deq = deque([(0, 0, 0)])
    # now, frm, mod
    visited[0][-1][0] = 0
    while deq:
        v, mod, frm = deq.popleft()
        now_ = h(v, frm)
        # print(v, mod, frm, visited[now_][mod])
        for i, next in enumerate(g[v]):
            if visited[next][][(mod + 1) % k] != inf:
                continue
            if next == frm:
                continue
            if (mod + 1) % k == 0:
                visited[next_][(mod + 1) % k] = visited[now_][mod] + 1
                visited[h(next, next)][(mod + 1) % k] = visited[now_][mod] + 1
                deq.append((next, (mod + 1) % k, next))
            else:
                visited[next_][(mod + 1) % k] = visited[now_][mod] + 1
                deq.append((next, (mod + 1) % k, v))
    ans = [inf] * (n - 1)
    for i in range(1, n):
        for j in g[i]:
            ans[i - 1] = min(ans[i - 1], visited[h(i, j)][0] // k)
        if ans[i - 1] == inf:
            ans[i - 1] = -1
    print(*ans)
