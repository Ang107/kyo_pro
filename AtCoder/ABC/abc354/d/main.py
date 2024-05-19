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

s = [0, 3, 6, 7, 8]
bk = [0, 1, 3, 4, 4]
gk = [0, 2, 3, 3, 4]
a, b, c, d = MII()
a += 10**9
b += 10**9
c += 10**9
d += 10**9
if (c // 4 - a // 4) == 0:
    tmp = 8
    if c % 4 == 0:
        tmp = s[4] - s[a % 4]
    else:
        tmp = s[c % 4] - s[a % 4]
    # print(tmp, ((d - b) // 2))

    if b % 2 == d % 2:
        ans = tmp * ((d - b) // 2)
    elif b % 2 == 1:
        ans = tmp * ((d - b) // 2)
        if c % 4 == 0:
            ans += b[4] - b[a % 4]
        else:
            ans += b[c % 4] - b[a % 4]

    elif d % 2 == 1:
        ans = tmp * ((d - b) // 2)
        if c % 4 == 0:
            ans += gk[4] - gk[a % 4]
        else:
            ans += gk[c % 4] - gk[a % 4]


# def get_s(a,b,c,d):
#     if

else:
    ans = 0
    ans += ((c + 1) // 4 - a // 4) * 8
    ans = ans * ((d - b) // 2)
    # print((d + 1) // 2 - b // 2)
    # print(ans)
    if a % 4 == 1:
        if b % 2 == d % 2:
            ans = ans + 5 * ((d - b) // 2)
        elif b % 2 == 1:
            ans = ans + 5 * ((d - b) // 2) + 3
        elif d % 2 == 1:
            ans = ans + 5 * ((d - b) // 2) + 2

    elif a % 4 == 2:
        ans = ans + 2 * (d - b) // 2

    elif a % 4 == 3:
        if b % 2 == d % 2:
            ans = ans + 2 * ((d - b) // 2)
        elif b % 2 == 1:
            ans = ans + 2 * ((d - b) // 2)
        elif d % 2 == 1:
            ans = ans + 2 * ((d - b) // 2) + 1

    if c % 4 == 1:
        if b % 2 == d % 2:
            ans = ans + 3 * ((d - b) // 2)
        elif b % 2 == 1:
            ans = ans + 3 * ((d - b) // 2) + 1
        elif d % 2 == 1:
            ans = ans + 3 * ((d - b) // 2) + 2

    elif c % 4 == 2:
        ans = ans + 6 * (d - b) // 2

    elif c % 4 == 3:
        if b % 2 == d % 2:
            ans = ans + 7 * ((d - b) // 2)
        elif b % 2 == 1:
            ans = ans + 7 * ((d - b) // 2) + 4
        elif d % 2 == 1:
            ans = ans + 7 * ((d - b) // 2) + 3
pritn(ans)
