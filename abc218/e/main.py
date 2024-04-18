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
ed = []
d = {}
ans = 0
for i in range(m):
    a, b, c = MII()
    ed.append((c, a, b))
    ans += c

import typing


class UnionFind:
    """
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    """

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]],
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))


ed.sort()
UF = UnionFind(n)
for p, u, v in ed:
    if p < 0:
        UF.merge(u - 1, v - 1)
        ans -= p
        continue
    if UF.leader(u - 1) != UF.leader(v - 1):
        UF.merge(u - 1, v - 1)
        ans -= p
print(ans)

# for i in range(m):
#     a, b, c = MII()
#     if a == b:
#         if c > 0:
#             ans += c
#         continue

#     a, b = min(a, b), max(a, b)
#     ed[a - 1].add(b - 1)
#     ed[b - 1].add(a - 1)
#     if (a - 1, b - 1) in d:
#         if max(d[(a - 1, b - 1)], c) > 0:
#             ans += max(d[(a - 1, b - 1)], c)
#         d[(a - 1, b - 1)] = min(d[(a - 1, b - 1)], c)
#         continue

#     d[(a - 1, b - 1)] = c

# d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)

# for (u, v), p in d_sorted:
#     # print(u, v, p, len(ed[u]), len(ed[v]))
#     if len(ed[u]) > 1 and len(ed[v]) > 1 and p > 0:
#         ans += p
#         ed[u].remove(v)
#         ed[v].remove(u)

# print(ans)
