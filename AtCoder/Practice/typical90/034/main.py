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

# import pypyjit

# pypyjit.set_param("max_unroll_recursion=-1")
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
from typing import Generic, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


class MyDeque(Generic[T]):
    """
    インデックスアクセスがO(1)な両端キュー
    """

    def __init__(self, v: Iterable[T] = (), maxlen: int = 1 << 60):
        assert len(v) <= maxlen
        self.maxlen = maxlen
        self._size = len(v)
        self._l: List[T] = []
        self._r: List[T] = []
        for i, x in enumerate(v):
            if i < self._size >> 1:
                self._l.append(x)
            else:
                self._r.append(x)
        self._l.reverse()
        self._l_delled = 0
        self._r_delled = 0

    def __iter__(self) -> Iterator[T]:
        for i in reversed(range(self._l_delled, len(self._l))):
            yield self._l[i]
        for i in range(self._r_delled, len(self._r)):
            yield self._r[i]

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(range(self._r_delled, len(self._r))):
            yield self._r[i]
        for i in range(self._l_delled, len(self._l)):
            yield self._l[i]

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return f"MyDeque: {list(self)}"

    def __contains__(self, x: T) -> bool:
        return x in self._l[self._l_delled :] or x in self._r[self._r_delled :]

    def __getitem__(self, i: int) -> T:
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            return self._l[-i - 1]
        else:
            return self._r[self._r_delled + i - (len(self._l) - self._l_delled)]

    def __setitem__(self, i: int, x: T) -> None:
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            self._l[-i - 1] = x
        else:
            self._r[self._r_delled + i - (len(self._l) - self._l_delled)] = x

    def count(self, x: T) -> int:
        return self._l[self._l_delled :].count(x) + self._r[self._r_delled :].count(x)

    def append(self, x: T) -> None:
        self._size += 1
        self._r.append(x)
        if self._size > self.maxlen:
            self.popleft()

    def pop(self) -> T:
        assert self._size > 0
        self._size -= 1
        if len(self._r) - self._r_delled > 0:
            return self._r.pop()
        else:
            self._l_delled += 1
            return self._l[self._l_delled - 1]

    def appendleft(self, x: T) -> None:
        self._size += 1
        self._l.append(x)
        if self._size > self.maxlen:
            self.pop()

    def popleft(self) -> T:
        assert self._size > 0
        self._size -= 1
        if len(self._l) - self._l_delled > 0:
            return self._l.pop()
        else:
            self._r_delled += 1
            return self._r[self._r_delled - 1]


n, k = MII()
a = LMII()
deq = deque()
d = defaultdict(int)
ans = 0
for i in a:
    d[i] += 1
    deq.append(i)
    while len(d) > k:
        num = deq.popleft()
        d[num] -= 1
        if d[num] == 0:
            d.pop(num)
    ans = max(ans, len(deq))
print(ans)
