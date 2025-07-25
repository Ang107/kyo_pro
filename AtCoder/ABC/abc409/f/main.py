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


n, q = MII()
uf = UnionFind(n + q)
xys = []
xys_rotate = []


def rotate(x, y):
    return (x + y, x - y)


def dis(i, j):
    return abs(xys[i][0] - xys[j][0]) + abs(xys[i][1] - xys[j][1])


ans = []
heapq = []
for _ in range(n):
    xys.append(LMII())
for i in range(n):
    for j in range(i + 1, n):
        heappush(heapq, (dis(i, j), i << 30 | j))
for _ in range(q):
    # print(heapq)
    tmp = LMII()
    if tmp[0] == 1:
        xys.append([tmp[1], tmp[2]])
        tmp = defaultdict(lambda: inf)
        for i in range(len(xys) - 1):
            tmp[uf.leader(i)] = min(tmp[uf.leader(i)], dis(i, len(xys) - 1))
        for i, j in tmp.items():
            heappush(heapq, (j, i << 30 | (len(xys) - 1)))
    elif tmp[0] == 2:
        if uf.size(0) == len(xys):
            print(-1)
        else:
            while heapq:
                # print(heapq[0][1] >> 30, heapq[0][1] & ((1 << 30) - 1))
                if uf.same(heapq[0][1] >> 30, heapq[0][1] & ((1 << 30) - 1)):
                    heappop(heapq)
                else:
                    break
            if heapq:
                min_dis = heapq[0][0]
                while heapq and heapq[0][0] == min_dis:
                    _, uv = heappop(heapq)
                    u, v = uv >> 30, uv & ((1 << 30) - 1)
                    uf.merge(u, v)
                # print(heapq)
                print(min_dis)
            else:
                print(-1)
    else:
        u, v = tmp[1:]
        u -= 1
        v -= 1
        if uf.same(u, v):
            PY()
        else:
            PN()
