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
sys.setrecursionlimit(10**7)
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


t = II()
for _ in range(t):
    s = input()
    x = list(map(int, input()))
    y = list(map(int, input()))
    x_cnt = [0, 0]
    y_cnt = [0, 0]
    for i in x:
        x_cnt[i] += 1
    for i in y:
        y_cnt[i] += 1
    a, b = x_cnt
    c, d = y_cnt

    if len(s) * (a - c) % (d - b) != 0:
        print("No")
        continue

    if a == c and b == d:
        y_len == 0
        print("Yes")
        continue
    else:
        y_len = len(s) * (a - c) // (d - b)

        ny = []
        now = 0
        for i in x:
            if i == 0:
                now += len(s)
            else:
                ny.append((now, now + y_len))
                now += y_len

        # nowx = 0
        # nowy = 0
        # y_idx = 0
        # pair_list = []
        # pair = [[], []]
        # for i in x:
        #     pair[0].append(i)
        #     if i == 0:
        #         nowx += len(s)
        #     else:
        #         nowx += y_len

        #     while y_idx < len(y):
        #         if y[y_idx] == 0:
        #             tmp = len(s)
        #         else:
        #             tmp = y_len
        #         if nowy + tmp <= nowx:
        #             pair[1].append(y[y_idx])
        #             nowy += tmp
        #             y_idx += 1
        #         else:
        #             break
        #     if nowx == nowy:
        #         pair_list.append(pair)
        #         pair = [[], []]

        # print(pair_list)
        # correct_y = ["?"] * y_len
        # for p,q in pair_list:

        #     for i in p:

        # print(len(x), y_len)
        # nx = []
        # ny = []
        # for i in x:
        #     if i == 0:
        #         nx.extend(s)
        #     else:
        #         nx.extend(range(y_len))
        # for i in y:
        #     if i == 0:
        #         ny.extend(s)
        #     else:
        #         ny.extend(range(y_len))
        # correct_y = ["?"] * y_len
        # same = []
        # uf = UnionFind(26 + y_len)
        # rslt = "Yes"
        # for i, j in zip(nx, ny):
        #     if i == j:
        #         continue
        #     if i != j and i not in range(y_len) and j not in range(y_len):
        #         rslt = "No"
        #         break

        #     if i in range(y_len) and j in range(y_len):
        #         uf.merge(i, j)

        # for i, j in zip(nx, ny):
        #     if i in range(y_len) and j not in range(y_len):
        #         uf.merge(y_len + ord(j) - ord("a"), i)
        #     elif i not in range(y_len) and j in range(y_len):
        #         uf.merge(y_len + ord(i) - ord("a"), j)

        # for i in range(26):
        #     for j in range(i + 1, 26):
        #         if uf.same(y_len + i, y_len + j):
        #             rslt = "No"

        # print(rslt)
