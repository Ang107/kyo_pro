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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
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

ans = []
while 1:
    h = II()
    if h == 0:
        break
    s = [list(input()) for _ in range(h)]
    s = s[::-1]
    max_len = max(len(i) for i in s)
    for i in range(h):
        s[i] += [""] * (max_len - len(s[i]))
    for i in range(h):
        for j in range(len(s[i])):
            if s[i][j] in alph_s:
                break
            if s[i][j + 1] in alph_s:
                s[i][j] = "+"
            else:
                s[i][j] = "|"

    for j in range(max_len):
        f = True
        for i in range(h):
            if s[i][j] == "+":
                if j == 0:
                    f = False

            if s[i][j] in alph_s:
                f = True

            if f and s[i][j] == "|":
                s[i][j] = " "
    s = s[::-1]
    ans.append("\n".join("".join(i) for i in s))
for i in ans:
    print(i)
