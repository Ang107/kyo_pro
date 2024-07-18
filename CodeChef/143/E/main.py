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

t = II()
ans = []


def solve(n, s):
    rslt = -1
    rslt = []
    s = list(s)
    for i in range(n):
        rslt.append(s[i])
        # print(rslt, s[i + 1 : i + 3])
        if len(rslt) >= 2 and rslt[-1] != rslt[-2] and rslt[-2:] > s[i + 1 : i + 3]:
            rslt.pop()
            rslt.pop()
        # print(s[i : i + 2], s[i + 2 : i + 4], s[i : i + 2] > s[i + 2 : i + 4])
        # if s[i] != s[i + 1] and s[i : i + 2] > s[i + 2 : i + 4]:
        #     rslt = s[:i] + s[i + 2 :]
    if len(rslt) >= 2 and rslt[-1] != rslt[-2]:
        rslt.pop()
        rslt.pop()
    rslt = "".join(rslt)
    if rslt == "":
        rslt = "EMPTY"
    return rslt


def native(n, s):
    tmp = [s]
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            tmp.append(s[:i] + s[i + 2 :])
    rslt = min(tmp)
    if rslt == -1:
        rslt = s
    return rslt


import random

if 1:
    n = 10
    for i in range(1 << n):
        s = bin(i)[2:]
        s = "0" * (n - len(s)) + s
        print(s)
        # while True:
        #     s = input()
        #     n = len(s)
        print(solve(n, s))
        input()
        # ans1, ans2 = solve(n, s), native(n, s)
        # print(n, s)
        # if ans1 != ans2:

        #     print(ans1, ans2)
        #     exit()

for _ in range(t):
    n = II()
    s = input()
    rslt = solve(n, s)
    ans.append(rslt)

    pass


for i in ans:
    print(i)
