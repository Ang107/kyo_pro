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


n = II()
xy = [LMII() for _ in range(n)]
ans = 0


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


for i in combinations(xy, 3):
    if get_s(*i) == 0:
        pass
    else:
        ans += 1
print(ans)
