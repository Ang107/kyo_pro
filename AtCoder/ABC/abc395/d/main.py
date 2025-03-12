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

n, q = MII()
# 鳩iがいる巣の場所
pos = [i for i in range(n)]
# 左からi番目の巣のラベル
label = [i for i in range(n)]
# ラベルがiの巣の場所
nest_pos = [i for i in range(n)]
for _ in range(q):
    tmp = LMII()
    if tmp[0] == 1:
        a, b = tmp[1:]
        a -= 1
        b -= 1
        pos[a] = nest_pos[b]
    elif tmp[0] == 2:
        a, b = tmp[1:]
        a -= 1
        b -= 1
        label[nest_pos[a]], label[nest_pos[b]] = label[nest_pos[b]], label[nest_pos[a]]
        nest_pos[a], nest_pos[b] = nest_pos[b], nest_pos[a]
    else:
        a = tmp[1]
        a -= 1
        print(label[pos[a]] + 1)
    # print(pos)
    # print(label)
    # print(nest_pos)
