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

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

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


def solve(n: int, k: int, s: list[int]):
    rslt = inf
    idx_0 = []
    idx_1 = []
    bit_0 = BIT(n)
    bit_1 = BIT(n)
    for i in range(n):
        if s[i] == 0:
            bit_0.add(i, 1)
            idx_0.append(i)
        else:
            bit_1.add(i, 1)
            idx_1.append(i)
    idx_0 = idx_0[::-1]
    for i in range(k + 1):
        s_n = s[:]
        a = i
        b = k - i
        for i in idx_1[:a]:
            s_n[i] ^= 1
        for i in idx_0[:b]:
            s_n[i] ^= 1
        rslt = min(rslt, get_inversion_number(s_n, sorted(s_n)))

    # s_n = s[:]
    # for _ in range(k):
    #     if not idx_0:
    #         continue
    #     tmp = idx_0.pop()
    #     bit_1.add(tmp, 1)
    #     bit_0.add(tmp, -1)
    #     s_n[tmp] ^= 1
    # rslt = min(rslt, get_inversion_number(s_n, sorted(s_n)))

    # idx_0 = deque()
    # idx_1 = deque()
    # bit_0 = BIT(n)
    # bit_1 = BIT(n)
    # for i in range(n):
    #     if s[i] == 0:
    #         bit_0.add(i, 1)
    #         idx_0.append(i)
    #     else:
    #         bit_1.add(i, 1)
    #         idx_1.append(i)
    # s_n = s[:]
    # for _ in range(k):
    #     if not idx_1:
    #         continue
    #     tmp = idx_1.popleft()
    #     bit_0.add(tmp, 1)
    #     bit_1.add(tmp, -1)
    #     s_n[tmp] ^= 1
    # rslt = min(rslt, get_inversion_number(s_n, sorted(s_n)))

    # for _ in range(k):
    #     r1, r2 = 0, 0
    #     if idx_1 and 0 <= idx_1[0] + 1 <= n:
    #         r1 = bit_0.sum(idx_1[0] + 1, n)
    #     if idx_0 and 0 <= idx_0[-1] <= n:
    #         r2 = bit_1.sum(0, idx_0[-1])
    #     pritn(r1, r2)
    #     if r1 == r2 == 0:
    #         continue
    #     if r1 <= r2:
    #         tmp = idx_0.pop()
    #         bit_1.add(tmp, 1)
    #         bit_0.add(tmp, -1)
    #         s_n[tmp] ^= 1
    #     else:
    #         tmp = idx_1.popleft()
    #         bit_0.add(tmp, 1)
    #         bit_1.add(tmp, -1)
    #         s_n[tmp] ^= 1
    #     print(s_n)

    return rslt


def native(n: int, k: int, s: list[int]):
    min_rslt = inf
    for i in range(1 << n):
        tmp = []
        for j in range(n):
            if i >> j & 1:
                tmp.append(j)

        if len(tmp) > k:
            continue

        s_n = s[:]
        for j in tmp:
            s_n[j] ^= 1
        rslt = get_inversion_number(s_n, sorted(s_n))
        if min_rslt > rslt:
            min_rslt = rslt
            print(s_n)

    return min_rslt


import random

if 0:
    while 1:
        n = 10
        k = random.randrange(0, n + 1)
        s = list(random.randrange(2) for _ in range(n))
        r1 = solve(n, k, s)
        r2 = native(n, k, s)
        print(r1, r2)
        if r1 != r2:
            print(n, k, s)
            exit()
else:
    T = II()
    ans = []
    for _ in range(T):
        n, k = MII()
        s = list(map(int, input()))
        ans.append(solve(n, k, s))
        # native(n, k, s)
        pass

    for i in ans:
        print(i)
