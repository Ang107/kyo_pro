import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

t = II()
ans = []
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


for _ in range(t):
    n, m = MII()
    uf = UnionFind(n * 2)
    ed = [[] for _ in range(n)]
    for _ in range(m):
        a, b = MII()
        a -= 1
        b -= 1
        ed[a].append(b)
        ed[b].append(a)
        uf.merge(a, b + n)
        uf.merge(a + n, b)
    player = ""
    for i in range(n):
        # 二部グラフでないなら
        if uf.same(i, i + n):
            player = "Alice"
    if not player:
        player = "Bob"
    print(player)
    sys.stdout.flush()

    if player == "Bob":
        cand = set(range(n))
        color = [-1] * n
        for idx in range(n):

            def f():
                c = MII()
                for i in c:
                    for j in cand:
                        for k in ed[j]:
                            if i != color[k] and (
                                color[k] == -1
                                and (
                                    idx == n - 1
                                    or all(
                                        color[l] == -1 or color[l] == i for l in ed[k]
                                    )
                                )
                            ):
                                return (j, i)

            i, c = f()
            color[i] = c
            cand.remove(i)
            print(i + 1, c)
            sys.stdout.flush()

    else:
        for _ in range(n):
            print(1, 2)
            sys.stdout.flush()
            tmp = MII()

    # 二分グラフ判定
    # ->二部グラフ -> ボブ -> 塗り分け
    # -> not 二部グラフ- -> アリス -> 同一二色を擦る。

    pass
# for i in ans:
#     print(i)
