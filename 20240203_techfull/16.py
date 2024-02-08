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


n, m = MII()
q = [LMII() for _ in range(m)]
a = [0] * n
basyo = list(range(n))
for i in q:
    if i[0] == 1:
        _, l, r = i
        a[l - 1], a[r - 1] = a[r - 1], a[l - 1]
        basyo[l - 1], basyo[r - 1] = basyo[r - 1], basyo[l - 1]
    else:
        _, idx = i
        a[idx - 1] = (a[idx - 1] + 1) % 2
# print(a)
print(basyo)

a_basyo = [(i, j) for i, j in zip(a, basyo)]
a_basyo.sort(key=lambda x: x[1])
print(a_basyo)
l, r = [0], [0]
for idx, (i, j) in enumerate(a_basyo):

    l.append(l[-1] + i * 2 ** (n - 1 - idx))

for idx, (i, j) in enumerate(a_basyo[::-1]):
    r.append(r[-1] + ((i + 1) % 2) * 2**idx)
r = r[::-1]

mi = inf
print(l, r)
for i in range(n + 1):
    if mi > l[i] + r[i]:
        idx = i
        mi = l[i] + r[i]

ans = []
print(idx)
print([i for i, j in a_basyo])
for i in range(idx):
    if a_basyo[i][0] == 0:
        ans.append("A")
    else:
        ans.append("B")
for i in range(idx, n):
    if a_basyo[i][0] == 1:
        ans.append("A")
    else:
        ans.append("B")
print("".join(ans))
