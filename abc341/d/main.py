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


n, m, k = MII()

LCM = math.lcm(n, m)
a, b = LCM // n - 1, LCM // m - 1

tmp = k // (a + b)
amari = k % (a + b)
num = 0
# print(tmp, amari)
# print(a, b)
if amari == 0:
    print(LCM * tmp - min(n, m))
else:
    i = LCM * tmp
    j = LCM * tmp
    # print(i)
    while True:
        if (
            (i % n == 0 and i % m != 0)
            or (i % m == 0 and i % n != 0)
            or (j % n == 0 and j % m != 0)
            or (j % m == 0 and j % n != 0)
        ):
            num += 1

        if amari == num:
            print(max(i, j))
            break
        if i + n > j + m:
            j += m
        else:
            i += n
