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

n = II()
XY = []
for i in range(n):
    a, b = MII()
    XY.append((a + b, a - b))
XY_G = [(i, j) for i, j in XY if i % 2 == 0]
XY_K = [(i, j) for i, j in XY if i % 2 == 1]

XY_G_X = [i for i, j in XY_G]
XY_G_Y = [j for i, j in XY_G]

XY_K_X = [i for i, j in XY_K]
XY_K_Y = [j for i, j in XY_K]

XY_G_X.sort()
XY_G_Y.sort()
XY_K_X.sort()
XY_K_Y.sort()

acc_XY_G_X = list(accumulate(XY_G_X))
acc_XY_G_Y = list(accumulate(XY_G_Y))
acc_XY_K_X = list(accumulate(XY_K_X))
acc_XY_K_Y = list(accumulate(XY_K_Y))


def solve(l, acc_l):
    result = 0
    n = len(l)
    for i in range(len(l)):
        result += acc_l[-1] - acc_l[i] - l[i] * (n - i - 1)
    return result // 2


ans = (
    solve(XY_G_X, acc_XY_G_X)
    + solve(XY_G_Y, acc_XY_G_Y)
    + solve(XY_K_X, acc_XY_K_X)
    + solve(XY_K_Y, acc_XY_K_Y)
)
print(ans)
