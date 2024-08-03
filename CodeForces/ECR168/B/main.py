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
    n = II()
    s = [input() for _ in range(2)]
    uf = UnionFind(2 * n)
    for i in range(2):
        for j in range(n):
            if s[i][j] == "x":
                continue
            for p, q in around4:
                ni = i + p
                nj = j + q
                if ni in range(2) and nj in range(n) and s[ni][nj] == ".":
                    uf.merge(i * n + j, ni * n + nj)
    gr = uf.groups()
    gr_num = 0
    for i in gr:
        if len(i) == 1:
            p, q = i[0] // n, i[0] % n
            if s[p][q] == "x":
                continue
        gr_num += 1

    rslt = 0
    # add2 = [(+1, -1, "x"), (+1, +1, "x"), (+1, 0, "."),(0, -1,'.'), (0, +1,'.')]
    add1_1 = [(+1, -1, "x"), (0, -1, "."), (1, 0, ".")]
    add1_2 = [(+1, +1, "x"), (0, +1, "."), (1, 0, ".")]
    add1_3 = [(+1, 0, "x"), (0, -1, "."), (0, 1, ".")]
    minus1 = [(0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
    i = 0
    # print(gr_num)
    for j in range(n):
        tmp = (
            all(
                i + p in range(2) and j + q in range(n) and s[i + p][j + q] == r
                for p, q, r in add1_1
            )
            + all(
                i + p in range(2) and j + q in range(n) and s[i + p][j + q] == r
                for p, q, r in add1_2
            )
            + all(
                i + p in range(2) and j + q in range(n) and s[i + p][j + q] == r
                for p, q, r in add1_3
            )
        )
        # print(tmp)
        if gr_num + tmp == 3:
            rslt += 1

        if (
            all(
                i + p in range(2) and j + q in range(n) and s[i + p][j + q] == "x"
                for p, q in minus1
            )
            and gr_num - 1 == 3
        ):
            rslt += 1

    s = s[::-1]
    i = 0
    for j in range(n):
        tmp = (
            all(
                i + p in range(2) and j + q in range(n) and s[i + p][j + q] == r
                for p, q, r in add1_1
            )
            + all(
                i + p in range(2) and j + q in range(n) and s[i + p][j + q] == r
                for p, q, r in add1_2
            )
            + all(
                i + p in range(2) and j + q in range(n) and s[i + p][j + q] == r
                for p, q, r in add1_3
            )
        )
        if gr_num + tmp == 3:
            rslt += 1

        if (
            all(
                i + p in range(2) and j + q in range(n) and s[i + p][j + q] == "x"
                for p, q in minus1
            )
            and gr_num - 1 == 3
        ):
            rslt += 1
    ans.append(rslt)
    pass
for i in ans:
    print(i)
