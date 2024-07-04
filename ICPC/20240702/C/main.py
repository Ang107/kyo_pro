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
import inspect

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


def solve(n, c):
    d = {}
    for i in alph_l:
        d[i] = 0

    for idx, i in enumerate(c):
        d[i] += 1
        tmp = sorted(d.items(), key=lambda x: x[1], reverse=True)

        if tmp[0][1] > tmp[1][1] + n - 1 - idx:
            return f"{tmp[0][0]} {idx+1}"

    return "TIE"

    pass


ans = []

while 1:
    # 入力を記入
    n = II()
    if n == 0:
        break
    c = input().split()
    ans.append(solve(n, c))
    pass

for i in ans:
    print(i)
