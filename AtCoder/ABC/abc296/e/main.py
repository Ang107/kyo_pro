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
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

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
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
import typing
import sys


class CSR:
    def __init__(self, n: int, edges: typing.List[typing.Tuple[int, int]]) -> None:
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)

        for e in edges:
            self.start[e[0] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = self.start.copy()
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1


class SCCGraph_:
    """
    Reference:
    R. Tarjan,
    Depth-First Search and Linear Graph Algorithms
    """

    def __init__(self, n: int) -> None:
        self._n = n
        self._edges: typing.List[typing.Tuple[int, int]] = []

    def num_vertices(self) -> int:
        return self._n

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self._edges.append((from_vertex, to_vertex))

    def scc_ids(self) -> typing.Tuple[int, typing.List[int]]:
        g = CSR(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n

        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def dfs(v: int) -> None:
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids

            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]
                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])

            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids

    def scc(self) -> typing.List[typing.List[int]]:
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: typing.List[typing.List[int]] = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups


class SCCGraph:
    def __init__(self, n: int = 0) -> None:
        self._internal = SCCGraph_(n)

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        n = self._internal.num_vertices()
        assert 0 <= from_vertex < n
        assert 0 <= to_vertex < n
        self._internal.add_edge(from_vertex, to_vertex)

    def scc(self) -> typing.List[typing.List[int]]:
        return self._internal.scc()


n = II()
a = LMII()
ans = 0
scc = SCCGraph(n)
for i, j in enumerate(a):
    scc.add_edge(i, j - 1)
    if i == j - 1:
        ans += 1
for i in scc.scc():
    if len(i) > 1:
        ans += len(i)
print(ans)

# ed = [[] for _ in range(n)]
# for i, j in enumerate(a):
#     ed[i].append(j - 1)
# visited = [False] * n
# finished = [False] * n
# roop = set()
# # 有向グラフの閉路に含まれる頂点列挙


# def get_roop(v):
#     deq = deque()
#     deq.append(v)
#     visited[v] = True
#     roopstart = -1
#     local_visited = set()
#     local_visited.add(v)
#     while deq:
#         v = deq.pop()
#         for i in ed[v]:
#             if i in local_visited:
#                 roopstart = i
#                 break
#             elif visited[i]:
#                 break
#             else:
#                 visited[i] = True
#                 local_visited.add(i)
#                 deq.append(i)
#         if roopstart != -1:
#             break
#     if roopstart == -1:
#         return {}

#     deq = deque()
#     roop = {roopstart}
#     deq.append(roopstart)
#     visited_n = set()
#     visited_n.add(roopstart)
#     while deq:
#         v = deq.pop()
#         for i in ed[v]:
#             if i not in visited_n:
#                 deq.append(i)
#                 visited_n.add(i)
#                 roop.add(i)
#     return roop


# for i in range(n):
#     if not visited[i]:
#         r = get_roop(i)
#         for j in r:
#             roop.add(j)
#     # print(visited)
# print(len(roop))
