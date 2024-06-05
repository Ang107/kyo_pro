import sys
from collections import deque, defaultdict

# from itertools import (
#     accumulate,  # 累積和
#     product,  # bit全探索 product(range(2),repeat=n)
#     permutations,  # permutations : 順列全探索
#     combinations,  # 組み合わせ（重複無し）
#     combinations_with_replacement,  # 組み合わせ（重複可）
# )
# import math
from bisect import bisect_left, bisect_right

# from heapq import heapify, heappop, heappush
# import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
# alph_s = tuple(string.ascii_lowercase)
# alph_l = tuple(string.ascii_uppercase)
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

n = II()
a = LMII()
a.sort()
d = defaultdict(int)
for i in a:
    d[i] += 1
ans = 0
# i未満の要素数
memo = [-1] * (10**6 + 10)
for i in range(1, 10**6 + 2):
    memo[i] = bisect_left(a, i)
ans = 0
# print(memo)
for k, v in d.items():
    # print(k, v)
    for j in range(1, 10**6 + 1):
        if k * j > a[-1]:
            break
        if j == 1:
            ans += (
                j
                * v
                * (memo[min(10**6 + 1, k * (j + 1))] - memo[min(10**6 + 1, k * j + 1)])
            )
        else:
            ans += (
                j
                * v
                * (memo[min(10**6 + 1, k * (j + 1))] - memo[min(10**6 + 1, k * j)])
            )
        # print(ans)
# print(ans)
# print(d)
for i in d.values():
    ans += i * (i - 1) // 2
print(ans)
