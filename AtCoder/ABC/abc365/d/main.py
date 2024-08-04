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

n = II()
s = input()


def get_cand(s):
    if s == "P":
        return ("P", "S")
    elif s == "S":
        return ("S", "R")
    elif s == "R":
        return ("R", "P")
    else:
        print(-1)
        exit()


dp = defaultdict(int)
for i in range(n):
    cand = get_cand(s[i])
    ndp = defaultdict(int)
    # print(s[i], cand)
    for j in cand:
        for k in "PSR":
            if j == k:
                continue
            if s[i] == j:
                ndp[j] = max(ndp[j], dp[k])
            else:
                ndp[j] = max(ndp[j], dp[k] + 1)
    dp = ndp
print(max(dp.values()))
