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
# # setrecursionlimit(10**7)
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


# t = II()
# aans = []
# import random

# for i in range(t):
#     n = II()
#     b = LMII()
#     # n = random.randrange(1, 100)
#     # while True:
#     #     b = [random.randrange(1, 10**9 + 1) for _ in range(2 * n)]
#     #     if len(b) == len(set(b)):
#     #         break
#     b.sort()
#     sb = set(b)
#     tmp = [0, 0]
#     l = [[], []]
#     for i in range(0, n * 2, 2):
#         p, q = b[i], b[i + 1]
#         p, q = min(p, q), max(p, q)
#         if tmp[0] < tmp[1]:
#             l[0].append(q)
#             l[1].append(p)
#             tmp[1] += p
#             tmp[0] += q
#         else:
#             l[0].append(p)
#             l[1].append(q)
#             tmp[0] += p
#             tmp[1] += q
#     if tmp[0] > tmp[1]:
#         tmp[0], tmp[1] = tmp[1], tmp[0]
#         l[0], l[1] = l[1], l[0]

#     # i = bisect_left(sb, abs(tmp[0] - tmp[1]))
#     # print(n, b, f"{len(l[0])=},{len(l[1])=}")
#     if 1 <= abs(tmp[0] - tmp[1]) <= 10**18 and abs(tmp[0] - tmp[1]) not in sb:
#         l[0].append(abs(tmp[0] - tmp[1]))
#         print("!!! 1")

#     else:
#         diff = abs(tmp[0] - tmp[1])
#         # print(f"{l=}")
#         while True:
#             i = random.randrange(n)
#             j = random.randrange(n)
#             ttmp = tmp[:]
#             # print(i, j)
#             ttmp[0] -= l[0][i]
#             ttmp[0] += l[1][j]
#             ttmp[1] -= l[1][j]
#             ttmp[1] += l[0][i]
#             # print(ttmp)
#             ndiff = abs(ttmp[0] - ttmp[1])
#             # k = bisect_left(sb, ndiff)
#             if 1 <= ndiff <= 10**18 and ndiff not in sb:
#                 p = l[0].pop(i)
#                 q = l[1].pop(j)
#                 l[0].append(q)
#                 l[1].append(p)
#                 if ttmp[0] > ttmp[1]:
#                     ttmp[0], ttmp[1] = ttmp[1], ttmp[0]
#                     l[0], l[1] = l[1], l[0]
#                 l[0].append(ndiff)
#                 print("!!! 2")

#                 break

#         # for i in l[0]:
#         #     idx = bisect_left(l[1], i)
#         #     if 0 <= idx < len(l[1]):
#         #         ttmp = tmp
#         #         ttmp[0] -= i
#         #         ttmp[0] += l[1][idx]
#         #         ttmp[1] -= l[1][idx]
#         #         ttmp[1] += i
#         #         ndiff = abs(ttmp[0] - ttmp[1])
#         #         j = bisect_left(sb, ndiff)
#         #         if 1 <= ndiff <= 10**18 and j < n and sb[j] != ndiff:
#         #             p = l[0].remove(i)
#         #             q = l[1].pop(idx)
#         #             l[0].append(q)
#         #             l[1].append(p)
#         #             if ttmp[0] > ttmp[1]:
#         #                 ttmp[0], ttmp[1] = ttmp[1], ttmp[0]
#         #                 l[0], l[1] = l[1], l[0]
#         #             l[0].append(ndiff)
#         #             print("!!! 2")

#         #             break
#         #     idx -= 1
#         #     if 0 <= idx < len(l[1]):
#         #         ttmp = tmp
#         #         ttmp[0] -= i
#         #         ttmp[0] += l[1][idx]
#         #         ttmp[1] -= l[1][idx]
#         #         ttmp[1] += i
#         #         ndiff = abs(ttmp[0] - ttmp[1])
#         #         j = bisect_left(sb, ndiff)
#         #         if 1 <= ndiff <= 10**18 and j < n and sb[j] != ndiff:
#         #             p = l[0].remove(i)
#         #             q = l[1].pop(idx)
#         #             l[0].append(q)
#         #             l[1].append(p)
#         #             if ttmp[0] > ttmp[1]:
#         #                 ttmp[0], ttmp[1] = ttmp[1], ttmp[0]
#         #                 l[0], l[1] = l[1], l[0]
#         #             l[0].append(ndiff)
#         #             print("!!! 2")

#         #             break
#     ans = []
#     # print(n, f"{len(l[0])=},{len(l[1])=}")
#     # print(f"{l=}")
#     for i in range(n + 1):
#         ans.append(l[0][i])
#         if i < n:
#             ans.append(l[1][i])
#     aans.append(ans)
#     print(b)
#     print(l)
#     print(ans)
#     print(
#         len(set(ans)) == 2 * n + 1,
#         min(ans) >= 1,
#         max(ans) <= 10**18,
#         sum(l[0]) == sum(l[1]),
#         len(l[0]) == n + 1,
#         len(l[1]) == n,
#     )
#     setb = set(b)
#     sum_ = 0
#     for i in range(1, 2 * n + 1):
#         if i % 2 == 0:
#             sum_ -= ans[i]
#         else:
#             sum_ += ans[i]
#     assert ans[0] == sum_
#     assert (
#         len([i for i in ans if i not in b]) == 1
#         and len(set(ans)) == 2 * n + 1
#         and min(ans) >= 1
#         and max(ans) <= 10**18
#         and sum(l[0]) == sum(l[1])
#         and len(l[0]) == n + 1
#         and len(l[1]) == n
#     )

# for i in aans:
#     print(*i)
from sys import stdin, setrecursionlimit
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
# setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


t = II()
aans = []
import random

for _ in range(t):
    n = II()
    b = LMII()
    sb = set(b)
    while True:
        random.shuffle(b)
        l = b[:n]
        r = b[n:]
        sl, sr = sum(l), sum(r)
        if sl > sr:
            sl, sr = sr, sl
            l, r = r, l
        diff = sr - sl
        if 1 <= diff <= 10**18 and diff not in sb:
            l.append(diff)
            break

    ans = []
    for i, j in zip(l, r):
        ans.append(i)
        ans.append(j)
    ans.append(l[-1])
    aans.append(ans)
for i in aans:
    print(*i)
