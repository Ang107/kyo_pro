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


class IntHash:
    def __init__(self, *args):
        """
        *args: 各要素の取りうる値の最大値
        """
        self.bit_len = [-1] * len(args)
        self.mask = [-1] * len(args)
        for idx, i in enumerate(args):
            l = len(bin(i)) - 2
            self.bit_len[idx] = l
            self.mask[idx] = (1 << l) - 1
        assert sum(self.bit_len) <= 63, "数字が大きすぎてhash化できません。"
        self.sum_bit_len = [0]
        for i in self.bit_len[1:][::-1]:
            self.sum_bit_len.append(self.sum_bit_len[-1] + i)
        self.sum_bit_len = self.sum_bit_len[::-1]

    def hash(self, *args):
        assert len(self.bit_len) == len(args), "引数の数が一致しません。"
        hash = 0
        for a, l in zip(args, self.sum_bit_len):
            hash |= a << l
        return hash

    def restore(self, hash, idx=-1):
        assert idx == -1 or 0 <= idx < len(self.bit_len), "idxの値が不正です。"
        if idx == -1:
            return [hash >> l & m for l, m in zip(self.sum_bit_len, self.mask)]
        else:
            return hash >> self.sum_bit_len[idx] & self.mask[idx]


n, m, k = MII()
stab = []
# ihst = IntHash(10**9, 10**9)
# ihab = IntHash(10**5, 10**5)
for _ in range(m):
    a, s, b, t = MII()
    a -= 1
    b -= 1
    stab.append((s, t, a, b))
stab.sort()

dp = [0] * n
while stab:
    s, t, a, b = heappop(stab)

    if t == 0:
        dp[a] = max(dp[a], b)
    else:
        heappush(stab, (t + k, 0, b, dp[a] + 1))
print(max(dp))
