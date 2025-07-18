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
        # self.MOD = MOD
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
        # assert n < self.MOD, "MOD 以上の階乗は逆元が取れません"

        old_len = len(self._factorials)  # 旧サイズ (＝最大 index + 1)

        # 1. 階乗を前方向に追加
        for k in range(old_len, n + 1):
            self._factorials.append(self._factorials[-1] * k)

        # 2. 逆階乗テーブルを後ろから畳み込む
        # self._inv_factorials.extend([0] * (n + 1 - old_len))
        # self._inv_factorials[n] = pow(self._factorials[n], -1, self.MOD)
        # for k in range(n, old_len, -1):  # 新規に増えた部分だけ
        #     self._inv_factorials[k - 1] = self._inv_factorials[k] * k % self.MOD

    # ---------- 公開 API ---------- #
    def comb(self, n: int, r: int) -> int:
        """nCr を返す（範囲外は 0）"""
        assert r >= 0 and r <= n and n < self.MOD
        self._extend(n)
        return (
            self._factorials[n]
            * self._inv_factorials[r]
            % self.MOD
            * self._inv_factorials[n - r]
            % self.MOD
        )

    def fac(self, n: int) -> int:
        # assert n >= 0 and n < self.MOD
        self._extend(n)
        return self._factorials[n]

    def inv_fac(self, n: int) -> int:
        assert n >= 0 and n < self.MOD
        self._extend(n)
        return self._inv_factorials[n]


fac = Factorial(0, 1 << 100)


# k -= 1
def solve(a, b, k):
    ans = []
    for i in range(a + b):
        # print(a, b, k)
        if a == 0:
            ans.append("b")
        elif b == 0:
            ans.append("a")
        else:
            if (fac.fac(a + b - 1) // fac.fac(b) // fac.fac(a - 1)) < k:
                k -= fac.fac(a + b - 1) // fac.fac(b) // fac.fac(a - 1)
                b -= 1
                ans.append("b")
            else:
                a -= 1
                ans.append("a")
    return "".join(ans)


def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False


if 1:
    a, b, k = MII()
    print(solve(a, b, k))
else:
    import random

    while True:
        a = random.randrange(5)
        b = random.randrange(5)
        k = random.randrange(1, fac.fac(a + b) // fac.fac(a) // fac.fac(b) + 1)
        l = []
        l.extend(["a"] * a)
        l.extend(["b"] * b)
        for _ in range(k - 1):
            next_permutation(l)
        l = "".join(l)
        print(l, solve(a, b, k), a, b, k)
        if l != solve(a, b, k):
            exit()
