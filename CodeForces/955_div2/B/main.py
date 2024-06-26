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
    x, y, k = MII()
    # print()
    # 切り上げた値
    x += 1
    k -= 1
    tmp = -(-x // y) * y
    # print(tmp)

    while True:
        # print(x, k)
        if tmp - x <= k:
            # print("a")
            k -= tmp - x
            x = tmp
            # print("a1", x, k)
        else:
            # print("b")

            ans.append(x + k)
            break

        while x % y == 0:
            x //= y
        # print("c", x, y, k)
        if x == 1:
            ans.append(k % (y - 1) + 1)
            break
        tmp = -(-x // y) * y
    # for _ in range(100):
    #     x += 1
    #     while x % y == 0:
    #         x //= y
    #     print(x)
    # pass
for i in ans:
    print(i)
