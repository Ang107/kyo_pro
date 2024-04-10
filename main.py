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


h, w = MII()
sx, sy = MII()
gx, gy = MII()
m = II()
ed = defaultdict(list)
for i in range(m):
    a, b, c, d = MII()
    ed[(a, b)].append((c, d))
    ed[(c, d)].append((a, b))


def bfs():
    deq = deque()
    deq.append((sx, sy))
    visited = defaultdict(lambda: -1)
    visited[(sx, sy)] = 0
    while deq:
        print(deq)
        x, y = deq.popleft()
        if x == gx and y == gy:
            print(visited[(x, y)])
            exit()
        for i, j in ed[(x, y)]:
            if visited[(i, j)] == -1:
                visited[(i, j)] = visited[(x, y)] + 5
                deq.append((i, j))
        for i, j in around4:
            if (
                x + i in range(1, w + 1)
                and y + j in range(1, h + 1)
                and visited[(x + i, y + j)] == -1
            ):
                visited[(x + i, y + j)] = visited[(x, y)] + 5
                deq.append((x + i, y + j))


bfs()
