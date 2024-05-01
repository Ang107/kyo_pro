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


a, b, c = MII()
c_n = bin(c)[2:]

c_n = "0" * (60 - len(c_n)) + c_n

num = 0
for i in c_n:
    if i == "0":
        pass
    else:
        num += 1
# print(num)
# print((a + b) % 2 == num % 2 and 2 * (60 - num) + num >= a + b >= num)

if (a + b) % 2 == num % 2 and 2 * (60 - num) + num >= a + b >= num:
    x, y = 0, 0
    x_1, y_1 = 0, 0
    for i, j in enumerate(c_n[::-1]):
        # print(x, y, x_1, y_1)
        if j == "1":
            if a - x_1 >= b - y_1:
                x_1 += 1
                x += 2**i
            else:
                y_1 += 1
                y += 2**i
        # else:
        #     if x_1 < a and y_1 < b:
        #         x_1 += 1
        #         x += 2**i
        #         y_1 += 1
        #         y += 2**i
        # if x_1 == a and y_1 == b:
        #     print(x, y)
        #     print(x ^ y)
        #     print(bin(x).count("1"), bin(y).count("1"))
        #     exit()

else:
    print(-1)
    exit()

for i, j in enumerate(c_n[::-1]):
    # print(x, y, x_1, y_1)
    if j == "0":
        if x_1 < a and y_1 < b:
            x_1 += 1
            x += 2**i
            y_1 += 1
            y += 2**i
    if x_1 == a and y_1 == b:
        print(x, y)
        # print(x ^ y)
        # print(bin(x).count("1"), bin(y).count("1"))
        exit()
print(-1)
