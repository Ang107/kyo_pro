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


a, n = MII()

dp = [10**18] * (10**6)
dp[1] = 0
s = set([1])
while s:
    # print(s)
    tmp = set()
    for i in s:
        # 操作1
        tmp1 = i * a
        # 操作2
        tmp2 = None
        if i >= 10 and i % 10 != 0:
            tmp2 = str(i)[-1] + str(i)[:-1]
            tmp2 = int(tmp2)

        if tmp1 and tmp1 <= 999999 and dp[tmp1] > dp[i] + 1:
            dp[tmp1] = dp[i] + 1
            tmp.add(tmp1)
        if tmp2 and tmp2 <= 999999 and dp[tmp2] > dp[i] + 1:
            dp[tmp2] = dp[i] + 1
            tmp.add(tmp2)
    s = tmp

if dp[n] != 10**18:
    print(dp[n])
else:
    print(-1)
# n_len = len(str(n))
# n_s = str(n)
# cnd = []
# tmp = 1
# while True:
#     if len(str(a**tmp)) < n_len:
#         tmp += 1
#     elif len(str(a**tmp)) == n_len:
#         cnd.append(a**tmp)
#         tmp += 1
#     elif len(str(a**tmp)) > n_len:
#         break
# ans = 10**18
# for i in cnd:
#     tmp = math.log(i, a)
#     s = str(i)
#     for j in range(n_len):
#         if n_s == s[j:] + s[:j]:
#             ans = min(ans, tmp + j)
#             break
