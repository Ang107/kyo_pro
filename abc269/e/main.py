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

MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


II = lambda: int(input())
n = II()
# 1000->500->250->125->63->32->16->8->4->2で9回、最後の二択判定で10回なのでXY合計20回で問題なく判定可能

# x座標
a, b, c, d = 1, n, 1, n
num = n
# 候補を二部探索で二つに絞る
while b - a > 1:
    mid = (a + b) // 2
    num = mid - a + 1  # 指定した範囲に含まれるX座標マスの幅
    print("?", a, mid, c, d, flush=True)
    t = II()
    if t < num:
        b = mid
    else:
        a = mid + 1
# 候補のうちどちらかを判定
print("?", a, a, c, d, flush=True)
t = II()
if t == 0:
    x = a
else:
    x = b

# y座標
a, b, c, d = 1, n, 1, n
num = n
# 候補を二部探索で二つに絞る
while d - c > 1:
    mid = (c + d) // 2
    num = mid - c + 1  # 指定した範囲に含まれるY座標マスの幅
    print("?", a, b, c, mid, flush=True)
    t = II()
    if t < num:
        d = mid
    else:
        c = mid + 1
# 候補のうちどちらかを判定
print("?", a, b, c, c, flush=True)
t = II()
if t == 0:
    y = c
else:
    y = d

print("!", x, y, flush=True)
