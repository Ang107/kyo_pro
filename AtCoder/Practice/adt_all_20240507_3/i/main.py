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
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, m = MII()
ed = [set() for _ in range(n)]
ed_qry = []
for _ in range(m):
    u, v = MII()
    u -= 1
    v -= 1
    ed[u].add(v)
    ed_qry.append((u, v))


def bfs_all():
    deq = deque()
    visited = [-1] * n
    deq.append(0)
    visited[0] = 0
    prv = [-1] * n

    while deq:
        v = deq.popleft()
        for i in ed[v]:
            if visited[i] == -1:
                prv[i] = v
                deq.append(i)
                visited[i] = visited[v] + 1
    root = set()
    v = n - 1
    while prv[v] != -1:
        root.add((prv[v], v))
        v = prv[v]
    return visited, root


def bfs():
    deq = deque()
    visited = [-1] * n
    deq.append(0)
    visited[0] = 0

    while deq:
        v = deq.popleft()
        for i in ed[v]:
            if visited[i] == -1:
                deq.append(i)
                visited[i] = visited[v] + 1
    return visited


visited, root = bfs_all()

for i in range(m):
    u, v = ed_qry[i]
    if (u, v) in root:
        ed[u].discard(v)
        print(bfs()[n - 1])
        ed[u].add(v)
    else:
        print(visited[n - 1])
