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
import random


class RollingHash:
    def __init__(self, s: str, base: int = None, mod: int = 2**61 - 1):
        self.s = s
        self.MOD = mod
        self.base = 114
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


base = 114
pow_base_mod = [1]
MOD = 2**61 - 1
# for _ in range(500000+1):
#     pow_base_mod.append(pow_base_mod[-1] * base % MOD)
q = II()
x = set()
y = defaultdict(set)


def to_hash(s):
    hash_l = [0]
    for i in s:
        hash_l.append((hash_l[-1] * base + ord(i)) % MOD)
    return hash_l[1:]


ans = 0
ss = []
for index in range(q):
    t, s = input().split()

    ss.append(s)
    if t == "1":
        hash = to_hash(s)
        ans -= len(y[hash[-1]])
        for idx in y[hash[-1]]:
            nhash = to_hash(ss[idx])
            for h in nhash:
                if h != hash[-1]:
                    y[h].remove(idx)
        y[hash[-1]] = set()
        x.add(hash[-1])
    else:
        hash = to_hash(s)
        if all(h not in x for h in hash):
            ans += 1
            for h in hash:
                y[h].add(index)
    print(ans)
