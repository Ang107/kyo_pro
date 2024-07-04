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
import inspect

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
    def __init__(self, s: str):
        self.s = s
        self.MOD = 2**61 - 1
        self.B = 100
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


def solve(s):
    l = s[: len(s) // 2]
    if len(s) % 2 == 1:
        r = s[len(s) // 2 + 1 :]
    else:
        r = s[len(s) // 2 :]
    r = r[::-1]
    rh_l = RollingHash(l)
    rh_l.make_hash_l()
    rh_r = RollingHash(r)
    rh_r.make_hash_r()
    l_idx = -1
    # r_idx = -1
    ans = 0
    for i in range(len(l)):
        if l_idx == -1:
            if l[i] == r[i]:
                pass
            else:
                l_idx = i

        else:
            # print(l[l_idx : i + 1])
            # print(r[l_idx : i + 1])
            # print(rh_l.get_hash_l(l_idx, i))
            # print(rh_r.get_hash_r(l_idx, i))

            if rh_l.get_hash_l(l_idx, i) == rh_r.get_hash_r(l_idx, i):
                ans += (i - l_idx + 1) ** 2
                l_idx = -1
    if l_idx == -1:
        return ans
    else:
        return -1
    pass


ans = []

while 1:
    # 入力を記入
    s = input()
    if s == "#":
        break
    ans.append(solve(s))

    pass

for i in ans:
    print(i)
