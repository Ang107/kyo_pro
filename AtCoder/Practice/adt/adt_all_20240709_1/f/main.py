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
xy = [LMII() for _ in range(n)]


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


def ok(i, j, k):
    return get_s(xy[i], xy[j], xy[k]) != 0


ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if ok(i, j, k):
                ans += 1
print(ans)
