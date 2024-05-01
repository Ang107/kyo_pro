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

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x):
    return print(x)


def PY():
    return print("Yes")


def PN():
    return print("No")


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


n = II()
n_str = str(n)
ans = 0
for i in range(1, len(n_str) + 1):
    num = int(n_str[-i])
    # 通り数の計算
    tmp = 1
    tmp *= n // 10**i
    tmp *= 10 ** (i - 1)
    # print(tmp)
    for j in range(1, 10):
        ans += j * tmp
        # print(j, j * tmp)
    # 端数
    for j in range(1, num + 1):
        if j == num:
            ans += j * (n % 10 ** (i - 1) + 1)
            # print(j, j * (n % 10 ** (i - 1) + 1))
        else:
            ans += j * 10 ** (i - 1)
            # print(j, j * 10 ** (i - 1))


print(ans)
# ans = 0
# for i in range(n + 1):
#     for j in str(i):
#         ans += int(j)
# print(ans)
