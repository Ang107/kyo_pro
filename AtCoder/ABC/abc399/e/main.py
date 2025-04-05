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

n = II()
s = input()
t = input()
nt = set(t)
chnage = defaultdict(set)
for i, j in zip(s, t):
    # if i != j:
    chnage[i].add(j)
next = {}
used = set()
rev = defaultdict(set)
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


ok = defaultdict(lambda: True)

for i in abc:
    ok[i] = True
scc = SCCGraph(26)
cnt = 0
for k, v in chnage.items():
    if len(v) > 1:
        print(-1)
        exit()
    tmp = v.pop()
    used.add(k)
    used.add(tmp)
    # continue
    scc.add_edge(ord(k) - ord("a"), ord(tmp) - ord("a"))
    if k != tmp:
        next[k] = tmp
    else:
        ok[k] = False
    rev[tmp].add(k)

g = scc.scc()
# print(g)
for i in g:
    if len(i) > 1:
        for j in i:
            tmp = set()
            deq = deque()
            deq.append(j)
            tmp.add(j)
            while deq:
                v = deq.popleft()
                for nx in rev[v]:
                    if nx not in tmp:
                        tmp.add(nx)
                        deq.append(nx)
            for k in tmp:
                ok[k] = False
ans = len(next)
# print(ok)
for i in g:
    if len(i) > 1:
        ans += 1
if all(i == False for i in ok):
    print(-1)
    exit()
# for i in abc:
#     if len(rev[i]) == 0:
#         ok[i] = True
# print(len(tmp))
# visited = defaultdict(lambda: False)
# for i in abc:
#     if not visited[i]:
#         vv = defaultdict(lambda: False)
#         visited[i] = True
#         vv[i] = True
#         cnt = 1
#         while i in next and i != next[i]:
#             if visited[next[i]] == False:
#                 visited[next[i]] = True
#                 vv[next[i]] = True
#                 i = next[i]
#             else:
#                 if vv[next[i]] == True:
#                     if all(p == False for p in ok):
#                         print(-1)
#                         exit()
#                     else:
#                         ans += 1
#                         break
#                 else:
#                     break

print(ans)
