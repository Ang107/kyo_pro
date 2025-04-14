import time

START = time.perf_counter()
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
import random

# 誤差の大きさによって解法の場合分けもあり

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


def question_query(vs):
    print("?", len(vs), *vs, flush=True)
    return [tuple(map(int, input().split())) for _ in range(len(vs) - 1)]


def answer_query(vv, ee):
    print("!")
    for i in range(M):
        print(*vv[i])
        for u, v in ee[i]:
            print(u, v)


import random

N, M, Q, L, W = MII()
weight = [[0] * N for _ in range(N)]

G = list(map(int, input().split()))
sq = []
pos = []
# 雑な場所の計算
for _ in range(N):
    lx, rx, ly, ry = MII()
    sq.append((lx, rx, ly, ry))
    pos.append(((lx + rx) / 2, (ly + ry) / 2))


def get_dis(a, b, c, d):
    return ((a - c) ** 2 + (b - d) ** 2) ** 0.5


# 最悪でも充分に短いものはスコアを付与
lim = 180 * 3
for i in range(N):
    for j in range(i + 1, N):
        worst = 0
        best = inf
        for ai in range(2):
            for bi in range(2):
                for ci in range(2):
                    for di in range(2):
                        a = sq[i][ai]
                        b = sq[j][bi]
                        c = sq[i][2 + ci]
                        d = sq[j][2 + di]
                        worst = max(worst, get_dis(a, b, c, d))
                        best = min(best, get_dis(a, b, c, d))
        # if worst <= lim:
        #     weight[i][j] += L * 10 * lim / worst
        if best > 1000:
            weight[i][j] -= 10000000

# 正方形の辺の長さ
length = int((L * 10**8 / N) ** 0.5)
alph = L / 2
beta = 1
# クエリを元に重みを付与
for _ in range(Q):
    while True:
        lx = random.randrange(10001 - length)
        ly = random.randrange(10001 - length)
        rx = lx + length
        ry = ly + length
        cand = []
        for i in range(N):
            if lx <= pos[i][0] <= rx and ly <= pos[i][1] <= ry:
                cand.append(i)
        if len(cand) >= L:
            break
    random.shuffle(cand)
    cand = cand[:L]
    new_ed = question_query(cand)
    for i in range(L):
        for j in range(i + 1, L):
            weight[cand[i]][cand[j]] -= beta
            weight[cand[j]][cand[i]] -= beta
    for u, v in new_ed:
        weight[u][v] += beta + alph
        weight[v][u] += beta + alph

edges = []
for i in range(N):
    for j in range(i + 1, N):
        edges.append((weight[i][j], i, j))
edges.sort(key=lambda x: x[0], reverse=True)
print(edges, file=stderr)


def evaluate(vs):
    # 頂点の集合vsで最小全域木を構築したときの重みの総和を返す(大きいほど良い)
    visited = set()
    visited.add(vs[0])
    mst_cost = 0

    edges = []
    for next in vs:
        if next not in visited:
            heappush(edges, (-weight[vs[0]][next], next))
    while edges and len(visited) < len(vs):
        cost, to = heappop(edges)
        if to not in visited:
            visited.add(to)
            mst_cost += -cost
            for next in vs:
                if next not in visited:
                    heappush(edges, (-weight[to][next], next))
    return mst_cost


def make_mst(vs):
    # 頂点の集合vsで最小全域木を構築したときの全域木を構築するための辺の集合を返す
    visited = set()
    visited.add(vs[0])
    mst_cost = 0
    mst_edges = []

    edges = []
    for next in vs:
        if next not in visited:
            heappush(edges, (-weight[vs[0]][next], vs[0], next))
    while edges and len(visited) < len(vs):
        cost, frm, to = heappop(edges)
        if to not in visited:
            visited.add(to)
            mst_cost += cost
            mst_edges.append((frm, to))
            for next in vs:
                if next not in visited:
                    heappush(edges, (-weight[to][next], to, next))
    return mst_edges


print(len(edges), file=stderr)

# グループの分解の初期解を貪欲法で作成
used = [False] * N
vv = [[] for _ in range(M)]
for i in range(M):
    size = G[i]
    used2 = [False] * N
    if len(vv[i]) == 0:
        for j in range(N):
            if used[j] == False:
                vv[i].append(j)
                used[j] = True
                used2[j] = True
                break
    while len(vv[i]) < size:
        for _, u, v in edges:
            if used[u] == False and used2[v] == True:
                vv[i].append(u)
                used[u] = True
                used2[u] = True
                break
            elif used[v] == False and used2[u] == True:
                vv[i].append(v)
                used[v] = True
                used2[v] = True
                break

scores = [evaluate(i) for i in vv]
# グループの分割を山登り
while time.perf_counter() - START < 1.8:
    print(scores, file=stderr)
    i = random.randrange(M)
    j = random.randrange(M)
    if i == j:
        continue
    p = random.randrange(G[i])
    q = random.randrange(G[j])

    vv[i][p], vv[j][q] = vv[j][q], vv[i][p]
    score_i = evaluate(vv[i])
    score_j = evaluate(vv[j])
    if score_i + score_j >= scores[i] + scores[j]:
        scores[i] = score_i
        scores[j] = score_j
    else:
        vv[i][p], vv[j][q] = vv[j][q], vv[i][p]

ee = [make_mst(i) for i in vv]

answer_query(vv, ee)
