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

import random

xor = random.randrange(1 << 62, 1 << 63)
# xor = 0
t = II()
ans = []

for _ in range(t):
    n, x = MII()
    a = LMII()

    rslt = 0
    s = set([x ^ xor])
    idx = 0
    while idx < n:
        i = a[idx]

        s_n = set()
        for j in s:
            if i == (j ^ xor):
                rslt += 1
                s_n = set([x ^ xor])
                idx -= 1
                break
            s_n.add(j)
            if (j ^ xor) % i == 0:
                s_n.add(((j ^ xor) // i) ^ xor)
        s = s_n
        idx += 1
    pass
    ans.append(rslt + 1)
for i in ans:
    print(i)
