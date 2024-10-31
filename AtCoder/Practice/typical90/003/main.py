import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = MII()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


def dfs(s):
    stack = [s]
    visited = [-1] * n
    visited[s] = 0
    while stack:
        v = stack.pop()
        for next in g[v]:
            if visited[next] == -1:
                visited[next] = visited[v] + 1
                stack.append(next)
    return visited


dis1 = dfs(0)
s = dis1.index(max(dis1))
dis = dfs(s)
ans = max(dis) + 1
print(ans)
