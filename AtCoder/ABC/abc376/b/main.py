# from sys import stdin, setrecursionlimit
# from collections import deque, defaultdict
# from itertools import accumulate
# from itertools import permutations
# from itertools import product
# from itertools import combinations
# from itertools import combinations_with_replacement
# from math import ceil, floor, log, log2, sqrt, gcd, lcm
# from bisect import bisect_left, bisect_right
# from heapq import heapify, heappop, heappush
# from functools import cache
# from string import ascii_lowercase, ascii_uppercase

# DEBUG = False
# # import pypyjit
# # pypyjit.set_param("max_unroll_recursion=-1")
# # 外部ライブラリ
# # from sortedcontainers import SortedSet, SortedList, SortedDict
# setrecursionlimit(10**7)
# alph_s = ascii_lowercase
# alph_l = ascii_uppercase
# around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
# around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
# inf = float("inf")
# mod = 998244353
# input = lambda: stdin.readline().rstrip()
# pritn = lambda *x: print(*x)
# deb = lambda *x: print(*x) if DEBUG else None
# PY = lambda: print("Yes")
# PN = lambda: print("No")
# SI = lambda: input()
# IS = lambda: input().split()
# II = lambda: int(input())
# MII = lambda: map(int, input().split())
# LMII = lambda: list(map(int, input().split()))


# n, q = MII()
# l = 0
# r = 1
# ans = 0
# for _ in range(q):
#     h, t = input().split()
#     t = int(t) - 1
#     if h == "R":
#         for i in [-1, 1]:
#             tmp = r
#             ok = True
#             cnt = 0
#             while tmp != t:
#                 cnt += 1
#                 if tmp != l:
#                     tmp += i
#                     tmp %= n
#                 else:
#                     ok = False
#                     break
#             if ok:
#                 r = tmp
#                 ans += cnt
#     else:
#         for i in [-1, 1]:
#             tmp = l
#             ok = True
#             cnt = 0
#             while tmp != t:
#                 cnt += 1
#                 if tmp != r:
#                     tmp += i
#                     tmp %= n
#                 else:
#                     ok = False
#                     break
#             if ok:
#                 l = tmp
#                 ans += cnt
#     # print(l, r, ans)
# print(ans)

n, q = map(int, input().split())
l = 0
r = 1
ans = 0
for _ in range(q):
    h, t = input().split()
    t = int(t) - 1
    if h == "L":
        move = l
        not_move = r
    else:
        move = r
        not_move = l
    for v in (-1, 1):
        tmp = move
        cnt = 0
        while tmp != not_move and tmp != t:
            tmp = (tmp + v) % n
            cnt += 1
        if tmp == t:
            ans += cnt
    if h == "L":
        l = t
    else:
        r = t
print(ans)
