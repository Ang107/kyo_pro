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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
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

d = [(1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (0, 1)]


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


ans = []
while True:
    t, n = MII()
    if t == n == 0:
        break
    xy = {tuple(LMII()) for _ in range(n)}
    sx, sy = MII()

    def bfs():
        deq = deque()
        visited = set()
        deq.append((sx, sy, 0))
        visited.add((sx, sy))
        while deq:
            x, y, turn = deq.popleft()
            if turn >= t:
                continue
            for i, j in d:
                nx = x + i
                ny = y + j
                if (nx, ny) not in visited and (nx, ny) not in xy:
                    deq.append((nx, ny, turn + 1))
                    visited.add((nx, ny))
        return len(visited)

    ans.append(bfs())

for i in ans:
    print(i)
