from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

k = II()
s = input()
t = input()
if s == t:
    PY()
    exit()
if abs(len(s) - len(t)) > 1:
    PN()
    exit()
l = 0
r = 0
for i, j in zip(s, t):
    if i == j:
        l += 1
    else:
        break
for i, j in zip(s[::-1], t[::-1]):
    if i == j:
        r += 1
    else:
        break
if l + r >= min(len(s), len(t)):
    PY()
    exit()
if len(s) == len(t) and len([i for i, j in zip(s, t) if i != j]) == 1:
    PY()
    exit()
PN()
"""
c,fの問題の操作は、
s,tのいずれかの任意位置の一文字の削除or置換
と言い換えるとやりやすかった"""
