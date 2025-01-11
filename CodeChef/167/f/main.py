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


class BIT:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, v: typing.Union[int, typing.List[typing.Any]]) -> None:
        if isinstance(v, int):
            self._n = v
            self.data = [0] * self._n
        else:
            self._n = len(v)
            self.data = [0] * self._n
            for i, x in enumerate(v):
                self.add(i, x)

    def __str__(self) -> str:
        return f"BIT: {[self.get(i) for i in range(self._n)]}"

    def __iter__(self) -> typing.Iterator[typing.Any]:
        return iter(self.get(i) for i in range(self._n))

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n
        return self.sum(p, p + 1)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n
        self.add(p, x - self.get(p))

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


t = II()
anss = []
for _ in range(t):
    n = II()
    s = list(map(int, input()))
    ans = 0
    for i in range(1, n + 1):
        ans += (n - i + 1) * (i // 2 + i % 2)
    for i in range(n-1):
        if s[i] == s[i+1]:
            ans += 


for ans in anss:
    print(ans)
