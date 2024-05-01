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
from sortedcontainers import SortedSet, SortedList, SortedDict

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


n, k = MII()
p = LMII()

ba = SortedSet()
maisuu = {}
d = defaultdict(list)
ans = [-1] * n

for j, i in enumerate(p):
    if len(ba) == 0:
        ba.add(i)
        maisuu[i] = 1
    else:
        idx = ba.bisect_left(i)
        if idx == len(ba):
            ba.add(i)
            maisuu[i] = 1
        else:
            maisuu[i] = maisuu[ba[idx]] + 1
            d[i] = d[ba[idx]]
            d[i].append(ba[idx])
            ba.remove(ba[idx])
            ba.add(i)

    if maisuu[i] == k:
        # print(d[i])
        # print(i)
        ba.remove(i)
        ans[i - 1] = j + 1
        for l in d[i]:
            ans[l - 1] = j + 1
    # print(ba)
    # print(maisuu)
for i in ans:
    print(i)
