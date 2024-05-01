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


n, p, q, r = MII()
a = LMII()
prf = [0] + list(accumulate(a))
ans = False
# xを全探索
num = n + 1
for i in range(0, n + 1):
    x = i
    y = bisect_left(prf, prf[x] + p)
    if y == n + 1 or prf[y] != prf[x] + p:
        continue
    z = bisect_left(prf, prf[y] + q)
    if z == n + 1 or prf[z] != prf[y] + q:
        continue
    w = bisect_left(prf, prf[z] + r)
    if w == n + 1 or prf[w] != prf[z] + r:
        continue
    ans = True

if ans:
    PY()
else:
    PN()
