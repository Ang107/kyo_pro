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
sx, sy, gx, gy = MII()
XYR = [LMII() for _ in range(n)]

ed = defaultdict(list)

for i in range(n):
    for j in range(i + 1, n):
        tmp1 = XYR[i]
        tmp2 = XYR[j]
        dis = (tmp1[0] - tmp2[0]) ** 2 + (tmp1[1] - tmp2[1]) ** 2
        if dis <= (tmp1[2] + tmp2[2]) ** 2 and dis >= abs(tmp1[2] - tmp2[2]):
            ed[i].append(j)
            ed[j].append(i)

s_list, g_list = [], []
for i in range(n):
    x, y, r = XYR[i]
    if (sx - x) ** 2 + (sy - y) ** 2 == r**2:
        s_list.append(i)
    if (gx - x) ** 2 + (gy - y) ** 2 == r**2:
        g_list.append(i)

visited = set()


def bfs(v):
    deq = deque()
    deq.append(v)
    visited.add(v)
    while deq:
        v = deq.popleft()
        for i in ed[v]:
            if i not in visited:
                visited.add(i)
                deq.append(i)


for i in s_list:
    if i not in visited:
        bfs(i)
# print(ed)
for i in g_list:
    if i in visited:
        PY()
        exit()

PN()
