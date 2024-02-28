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


n = II()
s = input()
next = [None] * (n + 1)
prv = [None] * (n + 1)
for i, j in enumerate(s):
    if j == "L":
        if prv[i] != None:
            next[prv[i]] = i + 1
            prv[i + 1] = prv[i]

        next[i + 1] = i
        prv[i] = i + 1

    elif j == "R":
        if next[i] != None:
            next[i + 1] = next[i]
            prv[next[i]] = i + 1
        next[i] = i + 1
        prv[i + 1] = i

# print(next)
# print(prv)
for i in range(n + 1):
    if prv[i] == None:
        st = i
        break
ans = [st]
for i in range(n):
    ans.append(next[ans[-1]])
print(*ans)
