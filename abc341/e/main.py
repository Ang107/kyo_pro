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
from sortedcontainers import SortedSet, SortedList, SortedDict

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


n, q = MII()
s = input()
num_0, num_1 = [0], [0]
renzoku = SortedSet()
for i in range(n - 1):
    if s[i] == s[i + 1]:
        renzoku.add(i)


for i in range(q):
    m, l, r = MII()
    l = l - 1
    r = r - 1
    # print(renzoku, l, r)
    if m == 1:
        if l != 0:
            if l - 1 in renzoku:
                renzoku.remove(l - 1)
            else:
                renzoku.add(l - 1)
        if r != n - 1:
            if r in renzoku:
                renzoku.remove(r)
            else:
                renzoku.add(r)
    else:
        if renzoku.bisect_left(l) == renzoku.bisect_left(r):
            PY()
        else:
            PN()
