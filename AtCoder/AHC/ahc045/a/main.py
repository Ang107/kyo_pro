from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
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
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
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

    def __init__(
        self,
        n: int = 0,
        vs: list[list[int]] = [],
        ops: typing.Callable[[int, int], int] = [],
    ) -> None:
        """
        n: 要素数
        vs: 集約操作の結果を保存する初期状態のリスト
        ops: 集約操作のリスト
        """
        assert len(vs) == len(ops)
        self._n = n
        self.parent_or_size = [-1] * n
        self.vs = [i[:] for i in vs]
        self.ops = ops

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

        for i in range(len(self.vs)):
            self.vs[i][x] = self.ops[i](self.vs[i][x], self.vs[i][y])

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

    def op(self, a: int, op_index: int) -> int:
        """
        指定した要素 a が属するグループに対して、vs[op_index] に基づく集約値を取得する。

        Args:
            a (int): 要素のインデックス
            op_index (int): 集約操作のインデックス

        Returns:
            int: 集約された値
        """
        assert 0 <= a < self._n
        assert 0 <= op_index < len(self.vs)
        return self.vs[op_index][self.leader(a)]


import random

N, M, Q, L, W = MII()
G = list(map(int, input().split()))
sq = []
pos = []
for _ in range(N):
    lx, rx, ly, ry = MII()
    sq.append((lx, rx, ly, ry))
    pos.append(((lx + rx) / 2, (ly + ry) / 2))
dis = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dis[i][j] = ((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2) ** 0.5
uf = UnionFind(N)
edges = []
for i in range(N):
    for j in range(i + 1, N):
        edges.append((dis[i][j], i, j))
edges.sort(key=lambda x: x[0])
mst = [[] for _ in range(N)]
for _, i, j in edges:
    if uf.same(i, j):
        continue
    uf.merge(i, j)
    mst[i].append(j)
    mst[j].append(i)

for _ in range(Q):
    cand = [random.randrange(N)]
    deq = deque()
    deq.append(cand[0])
    visited = [False] * N
    visited[cand[0]] = True
    dell_ed = []

    while len(cand) < L:
        v = deq.popleft()
        for next in mst[v]:
            if visited[next] == False and len(cand) < L:
                visited[next] = True
                deq.append(next)
                cand.append(next)
                dell_ed.append((v, next))
    for u, v in dell_ed:
        mst[u].remove(v)
        mst[v].remove(u)
    print("?", len(cand), *cand, flush=True)
    for _ in range(len(cand) - 1):
        u, v = MII()
        mst[u].append(v)
        mst[v].append(u)
print("!")
used = [False] * N
for i in G:
    c = []
    ed = []
    prev = -1
    while len(c) < i:
        for j in range(N):
            if not used[j]:
                s = j
                break
        if prev != -1:
            ed.append((prev, s))
        prev = s
        c = [s]
        deq = deque()
        deq.append(s)
        used[s] = True
        while deq:
            v = deq.popleft()
            for next in mst[v]:
                if used[next] == False and len(c) < i:
                    used[next] = True
                    c.append(next)
                    deq.append(next)
                    ed.append((v, next))
    print(*c, flush=True)
    for u, v in ed:
        print(u, v, flush=True)
