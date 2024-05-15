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


import typing


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
        self.max_elem = list(range(n))  # 各連結成分の最大要素を保持

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
        self.max_elem[x] = max(
            self.max_elem[x], self.max_elem[y]
        )  # 新しい代表を最大要素に更新

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

    def max_element(self, a: int) -> int:
        assert 0 <= a < self._n

        return self.max_elem[self.leader(a)]


n, m, e = MII()
uf = UnionFind(n + m)

ed = []
for _ in range(e):
    u, v = MII()
    u -= 1
    v -= 1
    ed.append((u, v))
q = II()
qry = [II() - 1 for _ in range(q)]

qry_set = set(qry)
for i in range(e):
    if i not in qry_set:
        uf.merge(ed[i][0], ed[i][1])
        print(ed[i][0], ed[i][1])
        print(uf.max_elem)
        print(uf.parent_or_size)


r = 0
groups = uf.groups()
for i in groups:
    if i[-1] >= n:
        r += bisect_left(i, n)
ans = []

for i in qry[::-1]:
    ans.append(r)
    u, v = ed[i]
    if uf.max_element(u) < n and uf.max_element(v) >= n:
        r += uf.size(u)
    elif uf.max_element(u) >= n and uf.max_element(v) < n:
        r += uf.size(v)
    uf.merge(u, v)
    print(u, v)
    print(uf.max_elem)
    print(uf.parent_or_size)

for i in ans[::-1]:
    print(i)
