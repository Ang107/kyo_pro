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

MII = lambda: map(int, input().split())


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


II = lambda: int(input())
LMII = lambda: list(map(int, input().split()))
n = II()
a = LMII()
l, r = a[:], a[::-1]
count = 0
kaidan_l = []
for i, x in enumerate(l):
    if count < x:
        count += 1
    else:
        count = x
    kaidan_l.append(count)

count = 0
kaidan_r = []
for i, x in enumerate(r):
    if count < x:
        count += 1
    else:
        count = x
    kaidan_r.append(count)

kaidan_r = kaidan_r[::-1]
kaidan_lr = []

for i, j in zip(kaidan_l, kaidan_r):
    kaidan_lr.append(min(i, j))

print(max(kaidan_lr))
