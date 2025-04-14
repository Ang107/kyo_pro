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

n1 = II()
g1 = [[] for _ in range(n1)]
for _ in range(n1 - 1):
    u, v = MII()
    u -= 1
    v -= 1
    g1[u].append(v)
    g1[v].append(u)
n2 = II()
g2 = [[] for _ in range(n2)]
for _ in range(n2 - 1):
    u, v = MII()
    u -= 1
    v -= 1
    g2[u].append(v)
    g2[v].append(u)


def dfs(s, g):
    n = len(g)
    deq = deque()
    deq.append(s)
    dis = [-1] * n
    dis[s] = 0
    while deq:
        v = deq.pop()
        for next in g[v]:
            if dis[next] == -1:
                deq.append(next)
                dis[next] = dis[v] + 1
    return dis


d = dfs(0, g1)
max_d = max(d)
u = d.index(max_d)
d1u = dfs(u, g1)
max_d = max(d1u)
v = d1u.index(max_d)
d1v = dfs(v, g1)
d1 = [max(i, j) for i, j in zip(d1u, d1v)]
max_d1 = max(d1)
d1.sort()

d = dfs(0, g2)
max_d = max(d)
u = d.index(max_d)
d2u = dfs(u, g2)
max_d = max(d2u)
v = d2u.index(max_d)
d2v = dfs(v, g2)
d2 = [max(i, j) for i, j in zip(d2u, d2v)]
max_d2 = max(d2)
d2.sort()
pref_d2 = list(accumulate(d2))
ans = 0
for i in d1:
    cnt = bisect_left(d2, max(max_d1, max_d2) - i - 1)
    ans += max(max_d1, max_d2) * cnt
    ans += n2 - cnt
    ans += i * (n2 - cnt)
    ans += pref_d2[-1]
    if cnt > 0:
        ans -= pref_d2[cnt - 1]
print(ans)
