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


h, w, n = MII()
tmp = []
for _ in range(n):
    a, b = MII()
    a -= 1
    b -= 1
    tmp.append((a, b))

x = [i for i, j in tmp]
y = [j for i, j in tmp]
x_d = {j: i for i, j in enumerate(sorted(set(x)))}
y_d = {j: i for i, j in enumerate(sorted(set(y)))}
# ans = [["*"] * len(y_d) for _ in range(len(x_d))]
for idx, (i, j) in enumerate(tmp):
    print(x_d[i] + 1, y_d[j] + 1)
    # ans[x_d[i]][y_d[j]] = idx + 1
