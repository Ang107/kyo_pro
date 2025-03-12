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

n = II()
a = LMII()
cnt = [0] * 2
if n == 1:
    print("Fennec")
    exit()
elif n == 2:
    print("Snuke")
    exit()
elif n == 3:
    if any(i for i in a if i % 2 == 1):
        print("Fennec")
    else:
        print("Snuke")
    exit()

for i in a:
    cnt[i % 2] += 1
if cnt[1] % 2 == 1:
    print("Fennec")
else:
    print("Snuke")

"""
触られてないものが，残り二個になった時点で，あとは，既出分を減らすことが最適になるので，その時点で勝敗は決まる
二個になった時点での残りの個数の総和が偶数にした人の勝ち，奇数にしたなら負け
n = 1 先手勝ち
n = 2 後手勝ち
n = 3 奇数が一個でもあれば勝ち
n = 4 偶数が一個，もしくは奇数が一個なら先手勝ち
"""
