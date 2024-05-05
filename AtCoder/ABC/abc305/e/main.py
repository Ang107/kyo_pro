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

n, m, k = MII()
ed = [[] for _ in range(n)]
for i in range(m):
    u, v = MII()
    ed[u - 1].append(v - 1)
    ed[v - 1].append(u - 1)
g = [-1] * n
heap = []
for i in range(k):
    p, h = MII()
    p -= 1
    heap.append((-h, p))
heapify(heap)


def di():
    # print(heap)
    while heap:
        h, p = heappop(heap)
        h = -h
        if h < g[p]:
            continue
        g[p] = max(g[p], h)
        for next in ed[p]:
            if g[next] < h - 1 and h - 1 >= 0:
                g[next] = h - 1
                heappush(heap, (-(h - 1), next))


di()
print(len([i for i in g if i >= 0]))
print(*[i + 1 for i in range(n) if g[i] >= 0])
