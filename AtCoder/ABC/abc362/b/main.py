import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
xy1 = LMII()
xy2 = LMII()
xy3 = LMII()


def naiseki(a, b, c):
    p, q, r = a[:], b[:], c[:]
    p[0] -= q[0]
    p[1] -= q[1]
    r[0] -= q[0]
    r[1] -= q[1]
    return p[0] * r[0] + p[1] * r[1] == 0


tmp = [xy1, xy2, xy3]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                if naiseki(tmp[i], tmp[j], tmp[k]):
                    PY()
                    exit()

# for i in permutations([xy1, xy2, xy3]):
#     print(list(i))
#     if naiseki(*list(i)):
#         PY()
#         exit()
PN()
