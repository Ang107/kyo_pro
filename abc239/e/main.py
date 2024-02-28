import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n, q = MII()
x = LMII()
ed = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = MII()
    ed[u - 1].append(v - 1)
    ed[v - 1].append(u - 1)

ans = [[] for _ in range(n)]
for i in range(n):
    ans[i].append(x[i])

visited = [False] * n


def solve(v):
    visited[v] = True
    for i in ed[v]:
        if not visited[i]:
            ans[v].extend(solve(i))
    ans[v].sort(reverse=True)
    return ans[v][:20]


solve(0)
for i in ans:
    i.sort(reverse=True)

for i in range(q):
    v, k = MII()
    print(ans[v - 1][k - 1])
