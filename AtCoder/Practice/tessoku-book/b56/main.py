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


import random


n, q = MII()
s = input()


class RollingHash:
    def __init__(self, s: str):
        self.s = s
        self.MOD = 2**61 - 1
        self.B = random.randrange(100, 200)
        self.pow_B_mod = [1]
        for _ in range(len(s)):
            self.pow_B_mod.append(self.pow_B_mod[-1] * self.B % self.MOD)

    def make_hash_l(self) -> None:
        """左から見た文字列のrolling hashを計算。"""
        self.hash_l = [0]
        for i in self.s:
            self.hash_l.append((self.hash_l[-1] * self.B + ord(i)) % self.MOD)

    def make_hash_r(self) -> None:
        """右から見た文字列のrolling hashを計算。"""
        self.hash_r = [0]
        for i in self.s[::-1]:
            self.hash_r.append((self.hash_r[-1] * self.B + ord(i)) % self.MOD)
        self.hash_r = self.hash_r[::-1]

    def get_hash_l(self, l: int, r: int) -> int:
        """左から見た文字列のl番目からr番目までの文字列のハッシュの取得(0index)"""
        return (
            self.hash_l[r + 1] - self.pow_B_mod[r - l + 1] * self.hash_l[l]
        ) % self.MOD

    def get_hash_r(self, l: int, r: int) -> int:
        """右から見た文字列のl番目からr番目までの文字列のハッシュの取得(0index)"""
        return (
            self.hash_r[l] - self.pow_B_mod[r - l + 1] * self.hash_r[r + 1]
        ) % self.MOD


rh = RollingHash(s)
rh.make_hash_l()
rh.make_hash_r()
for _ in range(q):
    l, r = MII()
    l -= 1
    r -= 1
    if rh.get_hash_l(l, r) == rh.get_hash_r(l, r):
        PY()
    else:
        PN()
