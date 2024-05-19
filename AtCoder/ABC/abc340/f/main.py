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
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


# 三頂点の外積を返す関数
def get_gaiseki(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x1 - x2) * (y3 - y2) - (y1 - y2) * (x3 - x2)


# 三頂点A,B,Cの角ABCを左回りに見た時の角の大きさが180度未満、180度、180より大きいかを返す
def get_angle_180_more_less_equal(a, b, c):
    gaiseki = get_gaiseki(a, b, c)
    # 180度
    if gaiseki == 0:
        return 0
    # 180度より小さい
    elif gaiseki > 0:
        return 1
    # 180度より大きい
    elif gaiseki < 0:
        return -1


# 三頂点の為す三角形の面積を返す
def get_s(a, b, c):
    return abs(get_gaiseki(a, b, c)) / 2


def get_s(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(-(x1 - x2) * y2 + (y1 - y2) * x2) / 2


x, y = MII()
# if x == 0:
#     if abs(y) <= 2:
#         print(2 // y, 0)
#     else:
#         print(-1)
# if y == 0:
#     if abs(x) <= 2:
#         print(0, 2 // x)
#     else:
#         print(-1)


tmp = math.gcd(x, y)
# print(tmp)


def extended_gcd(a, b):
    """拡張ユークリッドの互除法を用いて、ax + by = gcd(a, b) を満たす整数 x, y を求める"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def find_integer_solution(a, b):
    """ax + by = 2 を満たす整数 x, y を求める"""
    gcd, x0, y0 = extended_gcd(a, b)

    # ax0 + by0 = gcd(a, b) の倍数が解の一つなので、両辺を 2 / gcd(a, b) で割る
    factor = 2 // gcd
    x = x0 * factor
    y = y0 * factor

    return x, y


if 2 % tmp == 0:
    a, b = x, y
    x, y = find_integer_solution(b, -a)
    # print(get_s((a, b), (x, y)))
    print(x, y)
else:
    print(-1)
