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


n = II()
ed = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = MII()
    u -= 1
    v -= 1
    ed[u].append(v)
    ed[v].append(u)

for i in range(n):
    ed[i].sort(reverse=True)

ans = []
visited = set()

tmp = {}


def dfs(now, fr):
    if now not in tmp:
        tmp[now] = fr
    # print(ans)
    visited.add(now)
    ans.append(now)
    while ed[now] and ed[now][-1] in visited:
        ed[now].pop()

    if len(ed[now]) == 0:
        if now == 0:
            return
        else:
            dfs(tmp[now], now)
    else:
        i = ed[now].pop()
        if i not in visited:
            dfs(i, now)


dfs(0, -1)
print(*[i + 1 for i in ans])
