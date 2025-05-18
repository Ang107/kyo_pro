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


class Factorial:
    """
    階乗 / 逆階乗を必要になったぶんだけ動的に拡張するクラス。
    逆元は『一括逆元法』で計算するので高速。
    comb(n, r) は nCr を O(1) で返す。
    """

    def __init__(self, n: int = 0, MOD: int = 998244353):
        assert n < MOD, "MOD 以上の階乗は逆元が取れません"
        self.MOD = MOD
        # 0! から n! まで作る（まだ逆元は作らない）
        self._factorials = [1]
        for k in range(1, n + 1):
            self._factorials.append(self._factorials[-1] * k % MOD)

        # 逆階乗テーブル（先に正しい長さだけ確保）
        self._inv_factorials = [1] * (n + 1)
        if n:
            # 一括逆元法：まず n! の逆元を 1 回だけ pow で取る
            self._inv_factorials[n] = pow(self._factorials[n], -1, MOD)
            # 後ろから流し込む
            for k in range(n, 0, -1):
                self._inv_factorials[k - 1] = self._inv_factorials[k] * k % MOD

    # ---------- 内部ユーティリティ ---------- #
    def _extend(self, n: int) -> None:
        """テーブルを n まで拡張。既に長ければ何もしない。"""
        if n < len(self._factorials):
            return
        assert n < self.MOD, "MOD 以上の階乗は逆元が取れません"

        old_len = len(self._factorials)  # 旧サイズ (＝最大 index + 1)

        # 1. 階乗を前方向に追加
        for k in range(old_len, n + 1):
            self._factorials.append(self._factorials[-1] * k % self.MOD)

        # 2. 逆階乗テーブルを後ろから畳み込む
        self._inv_factorials.extend([0] * (n + 1 - old_len))
        self._inv_factorials[n] = pow(self._factorials[n], -1, self.MOD)
        for k in range(n, old_len, -1):  # 新規に増えた部分だけ
            self._inv_factorials[k - 1] = self._inv_factorials[k] * k % self.MOD

    # ---------- 公開 API ---------- #
    def comb(self, n: int, r: int) -> int:
        """nCr を返す（範囲外は 0）"""
        try:
            assert r >= 0 and r <= n and n < self.MOD
        except:
            return 0
        self._extend(n)
        return (
            self._factorials[n]
            * self._inv_factorials[r]
            % self.MOD
            * self._inv_factorials[n - r]
            % self.MOD
        )

    def fac(self, n: int) -> int:
        assert n >= 0 and n < self.MOD
        self._extend(n)
        return self._factorials[n]

    def inv_fac(self, n: int) -> int:
        assert n >= 0 and n < self.MOD
        self._extend(n)
        return self._inv_factorials[n]


fac = Factorial()
t = II()

min_ = [0]
for i in range(63):
    min_.append(min_[-1] | (1 << i))
# print([bin(i) for i in min_])


def g(n, k):
    global ans
    if min_[k] > n:
        return 0
    if n == 0 and k == 0:
        return 1

    bn = bin(n)[2:]
    res = 0
    for i in range(len(bn) - 1):
        ans += (1 << i) * fac.comb(len(bn) - 2, k - 1)
        res += fac.comb(len(bn) - 2, k - 1)
        ans %= mod
        res %= mod
    tmp = g(n - (1 << (len(bn) - 1)), k - 1)
    ans += (1 << (len(bn) - 1)) * tmp
    res += tmp
    ans %= mod
    res %= mod
    # print(n, k, res, ans)
    return res


def f(n, k):
    global ans
    bn = bin(n)[2:]
    for i in range(len(bn) - 1):
        ans += (1 << i) * fac.comb(len(bn) - 2, k - 1)
        ans %= mod
    # print(ans)
    ans += (1 << (len(bn) - 1)) * g(n - (1 << (len(bn) - 1)), k - 1)

    # print(ans, g(n - (1 << (len(bn) - 1)), k - 1))
    # print(bn, bin(n - (1 << (len(bn) - 1)))[2:])

    ans %= mod
    return ans


for _ in range(t):
    n, k = MII()
    ans = 0
    g(n, k)
    print(ans)
