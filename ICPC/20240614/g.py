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

trans = {"m":1000,"c":100,"x":10,"i" : 1}

def conversion(letters):
    real_num = 0
    for i in range(len(letters)):
        if letters[i] in trans:
            if letters[i-1] not in trans and 0 < i: #数字かつ一個前がそんざいする
                real_num += int(letters[i-1]) * trans[letters[i]]
            else: #1が省略されている場合
                real_num += trans[letters[i]]

    return real_num

def reverse_conversion(integer_):
    tmp = "mcxi"
    ans = ""
    integer_fill_0 = "0" * (4-len(str(integer_))) + str(integer_)
    # print(integer_)
    for i in range(4):
        if integer_fill_0[i] == "0":
            pass
        elif integer_fill_0[i] == "1":
            ans += tmp[i]
        else:
            ans += integer_fill_0[i]
            ans += tmp[i]

    return ans

def solve(x,y):
    real_numX = conversion(x)
    real_numY = conversion(y)
    ans = reverse_conversion(real_numX + real_numY)

    return ans
    pass

ans = []
t = II()
for _ in range(t):
    x,y = input().split()
    ans.append(solve(x,y))

for i in ans:
    print(i)