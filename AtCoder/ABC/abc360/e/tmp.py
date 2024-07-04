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
tmp = []
for i in range(998244354):
    # print(i)
    if (497172481 + 501071873 * i) % mod == 592707587:
        print(i)
        for j in range(1, mod + 1):
            if i * j % mod < 1000:
                print(j, i * j % mod)

# tmp = pow(3 - 1, -1, mod)
# for i in range(1, mod + 1):
#     if tmp * i % mod == 399297744:
#         print(i)
# print((554580198 - 911976323) % mod)
