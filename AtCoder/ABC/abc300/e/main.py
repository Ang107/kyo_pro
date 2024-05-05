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
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = int(input())
mod_6 = pow(6, -1, mod)
mod_5 = pow(5, -1, mod)
from functools import cache


@cache
# def f(x):
#     if x == 1:
#         return 1
#     result = 0
#     for i in range(2, 7):
#         if x % i == 0:
#             result += f(x // i) * mod_5
#             result %= mod
#     return result


@cache
def f(x):
    if x == n:
        return 1
    elif x > n:
        return 0
    elif x < n:
        result = 0
        for i in range(2, 7):
            result += f(x * i) * mod_5
            result %= mod
        return result


print(f(1))
