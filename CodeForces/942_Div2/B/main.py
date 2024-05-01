# import sys
# from collections import deque, defaultdict
# from itertools import (
#     accumulate,
#     product,
#     permutations,
#     combinations,
#     combinations_with_replacement,
# )
# import math
# from bisect import bisect_left, insort_left, bisect_right, insort_right
# from pprint import pprint
# from heapq import heapify, heappop, heappush
# import string

# # 小文字アルファベットのリスト
# alph_s = list(string.ascii_lowercase)
# # 大文字アルファベットのリスト
# alph_l = list(string.ascii_uppercase)

# # product : bit全探索 product(range(2),repeat=n)
# # permutations : 順列全探索
# # combinations : 組み合わせ（重複無し）
# # combinations_with_replacement : 組み合わせ（重複可）
# # from sortedcontainers import SortedSet, SortedList, SortedDict

# around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
# around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
# inf = float("inf")
# mod = 998244353
# input = lambda: sys.stdin.readline().rstrip()
# P = lambda *x: print(*x)
# PY = lambda: print("Yes")
# PN = lambda: print("No")
# II = lambda: int(input())
# MII = lambda: map(int, input().split())
# LMII = lambda: list(map(int, input().split()))


# def dlist(*l, fill=0):
#     if len(l) == 1:
#         return [fill] * l[0]
#     ll = l[1:]
#     return [dlist(*ll, fill=fill) for _ in range(l[0])]


# from functools import cache


# @cache
# def f(turn, x):
#     if 1 not in x or len(x) == 0:
#         if turn == 0:
#             result = -1
#         else:
#             result = 1

#     elif len(x) == 1:
#         if turn == 0:
#             if x[0] == 1:
#                 result = 1
#             else:
#                 result = -1
#         else:
#             if x[0] == 1:
#                 result = -1
#             else:
#                 result = 1

#     elif len(x) == 2:
#         if turn == 0:
#             if x.count(1) == 1:
#                 result = 1
#             else:
#                 result = -1
#         else:
#             if x.count(1) == 1:
#                 result = -1
#             else:
#                 result = 1

#     else:
#         if turn == 0:
#             result = -1
#             for i in range(len(x)):
#                 tmp = list(x)
#                 if x[i] == 1:
#                     if i == 0:
#                         tmp[i - 1] ^= 1
#                         tmp[i + 1] ^= 1
#                         result = max(result, f((turn + 1) % 2, tuple(tmp[1:])))
#                     elif i == len(x) - 1:
#                         tmp[i - 1] ^= 1
#                         tmp[(i + 1) % len(tmp)] ^= 1
#                         result = max(result, f((turn + 1) % 2, tuple(tmp[:-1])))
#                     else:
#                         tmp[i - 1] ^= 1
#                         tmp[i + 1] ^= 1
#                         result = max(
#                             result, f((turn + 1) % 2, tuple(tmp[:i] + tmp[i + 1 :]))
#                         )

#         else:
#             result = 1
#             for i in range(len(x)):
#                 tmp = list(x)
#                 if x[i] == 1:
#                     if i == 0:
#                         tmp[i - 1] ^= 1
#                         tmp[i + 1] ^= 1
#                         result = min(result, f((turn + 1) % 2, tuple(tmp[1:])))
#                     elif i == len(x) - 1:
#                         tmp[i - 1] ^= 1
#                         tmp[(i + 1) % len(tmp)] ^= 1
#                         result = min(result, f((turn + 1) % 2, tuple(tmp[:-1])))
#                     else:
#                         tmp[i - 1] ^= 1
#                         tmp[i + 1] ^= 1
#                         result = min(
#                             result, f((turn + 1) % 2, tuple(tmp[:i] + tmp[i + 1 :]))
#                         )
#     # print(turn, x, result)
#     return result


# t = II()
# for i in range(t):
#     n = II()
#     s = list(input())
#     tmp = []
#     for i in s:
#         if i == "U":
#             tmp.append(1)
#         else:
#             tmp.append(0)
#     s = tmp
#     if f(0, tuple(s)) == 1:
#         PY()
#     else:
#         PN()
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    count_u = s.count("U")
    if count_u % 2 == 1:
        print("YES")
    else:
        print("NO")
