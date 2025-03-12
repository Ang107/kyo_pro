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


n, k = MII()
a = LMII()
b = LMII()
c = LMII()
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)


def f(a, b, c):
    return a * b + b * c + c * a


class TupleHash:
    def __init__(self, *args):
        """
        *args: 各要素の取りうる値の最大値
        """
        self.bit_len = [-1] * len(args)
        self.mask = [-1] * len(args)
        for index, i in enumerate(args):
            l = len(bin(i)) - 2
            self.bit_len[index] = l
            self.mask[index] = (1 << l) - 1
        if sum(self.bit_len) > 63:
            from sys import stderr

            print("数字が大きすぎるため、低速になる可能性があります。", file=stderr)

        self.sum_bit_len = [0]
        for i in self.bit_len[1:][::-1]:
            self.sum_bit_len.append(self.sum_bit_len[-1] + i)
        self.sum_bit_len = self.sum_bit_len[::-1]

    def encode(self, *args):
        """
        タプルを整数にエンコード
        """
        assert len(self.bit_len) == len(args), "引数の数が一致しません。"
        assert all(0 <= i for i in args), f"引数に負の値が含まれています。引数: {args}"
        res = 0
        for a, l in zip(args, self.sum_bit_len):
            res |= a << l
        return res

    def deocde(self, res, index=None):
        """
        整数から元のタプルにデコード
        index: 特定の要素だけ取得する場合（省略時は全要素を取得）
        """
        assert index == None or 0 <= index < len(self.bit_len), "idxの値が不正です。"
        if index == None:
            return (res >> l & m for l, m in zip(self.sum_bit_len, self.mask))
        else:
            return res >> self.sum_bit_len[index] & self.mask[index]


TH = TupleHash(200000, 200000, 200000)
cnt = 0
heap = [(-f(a[0], b[0], c[0]), TH.encode(0, 0, 0))]
visited = set()
visited.add(TH.encode(0, 0, 0))
while True:
    ans, tmp = heappop(heap)
    i, j, l = TH.deocde(tmp)
    cnt += 1
    if cnt == k:
        print(-ans)
        break
    if i + 1 < n:
        ijl = TH.encode(i + 1, j, l)
        if ijl not in visited:
            visited.add(ijl)
            heappush(heap, (-f(a[i + 1], b[j], c[l]), ijl))
    if j + 1 < n:
        ijl = TH.encode(i, j + 1, l)
        if ijl not in visited:
            visited.add(ijl)
            heappush(heap, (-f(a[i], b[j + 1], c[l]), ijl))
    if l + 1 < n:
        ijl = TH.encode(i, j, l + 1)
        if ijl not in visited:
            visited.add(ijl)
            heappush(heap, (-f(a[i], b[j], c[l + 1]), ijl))
