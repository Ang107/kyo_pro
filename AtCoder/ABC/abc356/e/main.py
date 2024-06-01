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
ans = 0
memo = {}
d = defaultdict(int)
for i in a:
    d[i] += 1
# print(d)
# for i in d.values():
#     ans += i * (i - 1)
# print(a)
for i in a:
    for j in range(1, 10**6):
        if i * 10**7 + j not in memo:
            if j == 1:
                l = bisect_left(a, i * j + 1)
            else:
                l = bisect_left(a, i * j)
            r = bisect_left(a, i * (j + 1))
            ans += (r - l) * j
            # if (r - l) * j != 0:
            #     print(i, j, l, r, (r - l) * j)
            memo[i * 10**7 + j] = (r - l) * j
            if r == n:
                break
        else:
            ans += memo[i * 10**7 + j]
        # print(ans)
# print(ans)
for i in d.values():
    ans += i * (i - 1) // 2
pritn(ans)
