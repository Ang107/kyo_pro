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


s = input()
retu = [(7,), (4,), (8, 2), (5, 1), (9, 3), (6,), (10,)]
all_0 = [False] * 7
for i, j in enumerate(retu):
    tmp = True
    for k in j:
        if s[k - 1] == "1":
            tmp = False
    if tmp:
        all_0[i] = True
tmp = 0
# print(all_0)
for i in all_0:
    if i == False and tmp == 0:
        tmp = 1
    elif i == True and tmp == 1:
        tmp = 2
    elif i == False and tmp == 2:
        tmp = 3

if tmp == 3 and s[0] == "0":
    PY()
else:
    PN()
