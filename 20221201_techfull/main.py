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
ed = defaultdict(list)
p = LMII()
for i, j in enumerate(p):
    ed[j].append(i + 2)
ans = 0

node, branch = max([(i, len(j)) for i, j in ed.items()], key=lambda x: x[1])


def bfs():
    deq = deque()
    visited = [-1] * (n + 10)
    visited[node] = 0
    deq.append(node)
    while deq:
        v = deq.popleft()
        for i in ed[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                deq.append(i)
    return visited


visited = bfs()
depth = max(visited)
print(pow(branch, depth, mod))
