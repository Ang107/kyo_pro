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

n, m = MII()
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = MII()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
ans = [-1] * n
can_go = set()
visited = set()
visited.add(0)
for next in g[0]:
    can_go.add(next)
ans[0] = len(can_go)
vv = set()
deq = deque([0])
while deq:
    v = deq.pop()
    for next in g[v]:
        if next not in vv:
            vv.add(next)
            deq.append(next)
if len(vv) == n:
    ans[-1] = 0
for i in range(1, n - 1):
    if i in can_go:
        visited.add(i)
        can_go.remove(i)
        deq = deque()
        deq.append(i)
        while deq:
            v = deq.popleft()
            for next in g[v]:
                if next not in can_go and next not in visited:
                    if next <= i:
                        visited.add(next)
                        deq.append(next)
                    else:
                        can_go.add(next)
    if len(visited) == i + 1:
        ans[i] = len(can_go)
    else:
        ans[i] = -1
print(*ans, sep="\n")
