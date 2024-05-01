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


h1, h2, h3, w1, w2, w3 = MII()
ans = 0
tmp = max(h1, h2, h3, w1, w2, w3)
for a in range(1, tmp):
    for b in range(1, tmp):
        for d in range(1, tmp):
            for e in range(1, tmp):
                c = w1 - a - b
                f = w2 - d - e
                g = h1 - a - d
                h = h2 - b - e
                i = w3 - g - h
                if (
                    c + f + i == h3
                    and 1 <= c
                    and 1 <= f
                    and 1 <= g
                    and 1 <= h
                    and 1 <= i
                ):
                    # print(
                    #     a,
                    #     b,
                    #     c,
                    #     d,
                    #     e,
                    #     f,
                    #     g,
                    #     h,
                    #     i,
                    # )
                    ans += 1
print(ans)
