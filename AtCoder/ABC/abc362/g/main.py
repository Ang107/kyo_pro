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


import random


class RollingHash:
    def __init__(self, s: str, base: int = None, mod: int = 2**61 - 1):
        self.s = s
        self.MOD = mod
        self.base = base if base is not None else random.randrange(100, 200)
        self.pow_base_mod = [1]
        for _ in range(len(s)):
            self.pow_base_mod.append(self.pow_base_mod[-1] * self.base % self.MOD)
        self.make_hash_l()
        self.make_hash_r()

    def make_hash_l(self) -> None:
        """左から見た文字列のrolling hashを計算。"""
        self.hash_l = [0]
        for i in self.s:
            self.hash_l.append((self.hash_l[-1] * self.base + ord(i)) % self.MOD)

    def make_hash_r(self) -> None:
        """右から見た文字列のrolling hashを計算。"""
        self.hash_r = [0]
        for i in self.s[::-1]:
            self.hash_r.append((self.hash_r[-1] * self.base + ord(i)) % self.MOD)
        self.hash_r = self.hash_r[::-1]

    def get_hash_l(self, l: int, r: int) -> int:
        """左から見た文字列[l, r)のハッシュの取得(0_index)"""
        if l < 0 or r > len(self.s) or l > r:
            raise ValueError(
                f"get {l=}, {r=}, but expected 0 <= l <= r <= {len(self.s)}"
            )
        return (self.hash_l[r] - self.pow_base_mod[r - l] * self.hash_l[l]) % self.MOD

    def get_hash_r(self, l: int, r: int) -> int:
        """右から見た文字列[l, r)のハッシュの取得(0_index)"""
        if l < 0 or r > len(self.s) or l > r:
            raise ValueError(
                f"get {l=}, {r=}, but expected 0 <= l <= r <= {len(self.s)}"
            )
        return (self.hash_r[l] - self.pow_base_mod[r - l] * self.hash_r[r]) % self.MOD


# 使用例
# rh = RollingHash("example")
# print(rh.get_hash_l(4, 3))  # "exa"のハッシュを取得
# print(rh.get_hash_r(0, 3))  # "exa"の右から見たハッシュを取得
s = input()
q = II()
t = [input() for _ in range(q)]
l = {len(i) for i in t}
rh = RollingHash(s, base=200)
d = defaultdict(int)
for i in l:
    for j in range(len(s) - i + 1):
        d[rh.get_hash_l(j, j + i)] += 1
for i in t:
    tmp = RollingHash(i, base=200)
    print(d[tmp.get_hash_l(0, len(i))])
