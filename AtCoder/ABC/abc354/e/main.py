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
ab = [tuple(LMII()) for _ in range(n)]

from functools import cache


@cache
def f(s, turn):
    fin = True
    print(turn, s)
    # 選べるカードがない場合
    for i in range(len(ab)):
        for j in range(i + 1, len(ab)):
            if (
                s >> i & 1 == 0
                and s >> j & 1 == 0
                and ab[i][0] == ab[j][0]
                or ab[i][1] == ab[j][1]
            ):
                fin = False
    if fin or s == 2**n - 1:
        if turn == 0:
            return -1
        else:
            return 1

    if turn == 0:
        result = -1
        for i in range(n):
            for j in range(i + 1, n):
                if (
                    s >> i & 1 == 0
                    and s >> j & 1 == 0
                    and (ab[i][0] == ab[j][0] or ab[i][1] == ab[j][1])
                ):
                    result = max(result, f(s | 1 << i | 1 << j, turn ^ 1))

    else:
        result = 1
        for i in range(len(ab)):
            for j in range(i + 1, len(ab)):
                if (
                    s >> i & 1 == 0
                    and s >> j & 1 == 0
                    and (ab[i][0] == ab[j][0] or ab[i][1] == ab[j][1])
                ):
                    result = min(result, f(s | 1 << i | 1 << j, turn ^ 1))

    return result


if f(0, 0) == 1:
    print("Takahashi")
else:
    print("Aoki")
