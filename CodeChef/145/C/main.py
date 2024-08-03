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
mod = 10**9 + 7
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

T = II()
ans = []

# pref = [0, 1]
# for i in range(2, 5 * 10**5 + 1):
#     pref.append((pref[-1] + i**2 * ) % mod)
# print(pref[:10])
for _ in range(T):
    n = II()
    rslt = 0
    for i in range(n):
        # 長さ
        m = i + 1
        rslt += 2 * (n - m + 1) * (m - 1) ** 2 * pow(2, (n - m), mod) % mod
        # print(2 * (n - m + 1) * (m - 1) ** 2 * pow(2, (n - m), mod))
        rslt %= mod

    # for i in range(n):
    #     m = i + 1
    #     rslt += 2 * pref[m - 1] * pow(2, n - m, mod) % mod
    #     rslt %= mod
    ans.append(rslt)
    pass


for i in ans:
    print(i)
