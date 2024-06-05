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

t = II()
ans = []

for _ in range(t):
    n = II()
    a = LMII()
    g = []
    k = []

    # 左右からT or Fを取る
    gcd_list = []
    for i in range(n - 1):
        gcd_list.append(math.gcd(a[i], a[i + 1]))
    # print(gcd_list)
    # print(len(gcd_list))
    l_bool = [True, True, True]
    r_bool = [True, True, True]
    for i in range(0, n - 2):
        l_bool.append(l_bool[-1] and gcd_list[i] <= gcd_list[i + 1])
    for i in reversed(range(0, n - 2)):
        r_bool.append(r_bool[-1] and gcd_list[i] <= gcd_list[i + 1])
    r_bool = r_bool[::-1]
    # print(l_bool)
    # print(r_bool)
    gcd_list = gcd_list
    flag = False
    for i in range(len(l_bool)):
        if l_bool[i] and r_bool[i + 1]:
            if i - 1 not in range(len(a)) or i + 1 not in range(len(a)):
                flag = True
                break
            if (
                i - 2 not in range(len(gcd_list))
                or gcd_list[i - 2] <= math.gcd(a[i - 1], a[i + 1])
            ) and (
                i + 1 not in range(len(gcd_list))
                or math.gcd(a[i - 1], a[i + 1]) <= gcd_list[i + 1]
            ):
                flag = True
                break
            # print(
            #     i,
            #     a[i - 1],
            #     a[i + 1],
            #     gcd_list[i - 2],
            #     math.gcd(a[i - 1], a[i + 1]),
            #     gcd_list[i + 1],
            # )
    if flag:
        ans.append("Yes")
    else:
        ans.append("No")
    pass

for i in ans:
    print(i)
