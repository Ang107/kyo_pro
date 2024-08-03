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
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x):
    return print(x)


def PY():
    return print("Yes")


def PN():
    return print("No")


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


import typing
from collections import defaultdict, deque


class BIT:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


# AをBにするのに必要な転倒数を計算
# O(NlogN)
def get_inversion_number(A, B):
    to_idx = defaultdict(deque)
    for idx, a in enumerate(A):
        to_idx[a].append(idx)
    nB = []
    for i in B:
        nB.append(to_idx[i][0])
        to_idx[i].popleft()
    bit = BIT(len(nB))
    ans = 0
    for idx, i in enumerate(nB):
        ans += bit.sum(i + 1, len(nB))
        bit.add(i, 1)
    return ans


n = II()
p = [LMII() for _ in range(n)]
yoko = [-1] * n
tate = [-1] * n
for i in range(n):
    for j in range(n):
        if p[i][j] != 0:
            yoko[j] = p[i][j]
            tate[i] = p[i][j]

ans = get_inversion_number(yoko, list(range(1, n + 1))) + get_inversion_number(
    tate, list(range(1, n + 1))
)
print(ans)
