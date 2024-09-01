from sys import stdin, setrecursionlimit
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
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


n, m = MII()
ed = []
g = [[] for _ in range(n)]
for i in range(m):
    tmp = LMII()
    tmp[0] -= 1
    tmp[1] -= 1
    ed.append(tmp)
    g[tmp[0]].append((tmp[2], tmp[1], i))
    g[tmp[1]].append((tmp[2], tmp[0], i))


class IntHash:
    def __init__(self, *args):
        """
        *args: 各要素の取りうる値の最大値
        """
        self.bit_len = [-1] * len(args)
        self.mask = [-1] * len(args)
        for idx, i in enumerate(args):
            l = len(bin(i)) - 2
            self.bit_len[idx] = l
            self.mask[idx] = (1 << l) - 1
        assert sum(self.bit_len) <= 63, "数字が大きすぎてhash化できません。"
        self.sum_bit_len = [0]
        for i in self.bit_len[1:][::-1]:
            self.sum_bit_len.append(self.sum_bit_len[-1] + i)
        self.sum_bit_len = self.sum_bit_len[::-1]

    def hash(self, *args):
        assert len(self.bit_len) == len(args), "引数の数が一致しません。"
        hash = 0
        for a, l in zip(args, self.sum_bit_len):
            hash |= a << l
        return hash

    def restore(self, hash, idx=-1):
        assert idx == -1 or 0 <= idx < len(self.bit_len), "idxの値が不正です。"
        if idx == -1:
            return [hash >> l & m for l, m in zip(self.sum_bit_len, self.mask)]
        else:
            return hash >> self.sum_bit_len[idx] & self.mask[idx]


q = II()
for _ in range(q):
    k = II()
    b = LMII()
    b = [i - 1 for i in b]
    ans = 0
    # 頂点iにいて、到達済みの座標の集合がjのときの移動距離の最小値
    visited = [[inf] * (1 << k) for _ in range(n)]
    ih = IntHash(400, (1 << k))
    # 距離、インデックス、集合
    heap = [(0, ih.hash(0, 0))]
    while heap:
        dis, vs = heappop(heap)
        v, s = ih.restore(vs)
        if visited[v][s] < dis:
            continue
        for d, next, i in g[v]:
            if i in b:
                index = b.index(i)
                new_dis = dis + d
                if new_dis < visited[next][s | (1 << index)]:
                    visited[next][s | (1 << index)] = new_dis
                    heappush(heap, (new_dis, ih.hash(next, s | (1 << index))))
            else:
                new_dis = dis + d
                if new_dis < visited[next][s]:
                    visited[next][s] = new_dis
                    heappush(heap, (new_dis, ih.hash(next, s)))
    print(visited[n - 1][(1 << k) - 1])
