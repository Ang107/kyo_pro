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


def isOK(mid, n, num, k):
    need = 0
    for i in range(1, n + 1):
        need += max(0, mid - num[i])
    return need <= k


def meguru(ng, ok, n, num, k):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid, n, num, k):
            ok = mid
        else:
            ng = mid
    return ok


t = II()
for _ in range(t):
    n, k = MII()
    card = [0] + LMII()

    p = meguru(10**18, 0, n, card, k)
    amari = 0
    for i in card:
        if i - p > 0:
            amari += 1

    need = 0
    for i in range(1, n + 1):
        need += max(0, p - card[i])

    amari = amari + (k - need)
    ans = n * p + amari - n + 1

    print(ans)
