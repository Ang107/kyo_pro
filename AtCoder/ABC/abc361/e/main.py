# import sys
# from collections import deque, defaultdict
# from itertools import (
#     accumulate,  # 累積和
#     product,  # bit全探索 product(range(2),repeat=n)
#     permutations,  # permutations : 順列全探索
#     combinations,  # 組み合わせ（重複無し）
#     combinations_with_replacement,  # 組み合わせ（重複可）
# )
# import math
# from bisect import bisect_left, bisect_right
# from heapq import heapify, heappop, heappush
# import string

# # 外部ライブラリ
# # from sortedcontainers import SortedSet, SortedList, SortedDict
# sys.setrecursionlimit(10**7)
# alph_s = tuple(string.ascii_lowercase)
# alph_l = tuple(string.ascii_uppercase)
# around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
# around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
# inf = float("inf")
# mod = 998244353
# input = lambda: sys.stdin.readline().rstrip()
# pritn = lambda *x: print(*x)
# PY = lambda: print("Yes")
# PN = lambda: print("No")
# SI = lambda: input()
# IS = lambda: input().split()
# II = lambda: int(input())
# MII = lambda: map(int, input().split())
# LMII = lambda: list(map(int, input().split()))
# n = II()
# cab = []
# for _ in range(n - 1):
#     a, b, c = MII()
#     a -= 1
#     b -= 1
#     cab.append((c, a, b))
# # 端
# h = []
# ed = [[] for _ in range(n)]
# for c, a, b in cab:
#     ed[a].append((c, b))
#     ed[b].append((c, a))
# for i in range(n):
#     if len(ed[i]) == 1:
#         h.append((ed[i][0][0], i))
# # # 根
# ne = max(h)[1]
# # print(max_h)
# # frmから来た時のxの部分木を全部めぐってxに戻ってくるのに掛かる最小コスト
# from functools import cache


# @cache
# def f(x, frm):
#     # 往復の場合と片道両方求める
#     ouhuku_num = 0
#     max_diff = 0
#     for c, nxt in ed[x]:
#         if nxt == frm:
#             continue
#         rslt = f(nxt, x)
#         ouhuku_num += rslt[0] + c * 2

#         max_diff = max(max_diff, rslt[0] + c * 2 - (rslt[1] + c))

#     katamiti_num = ouhuku_num - max_diff
#     return ouhuku_num, katamiti_num


# ans = inf
# ans = f(ne, -1)[1]
# deq = deque([ne, -1,ans])


# while deq:
#     x, prv,cost = deq.pop()
#     for c,nxt in ed[x]:
#         if nxt == prv:
#             continue
#         cost_n = cost
#         cost +=


# for i in range(n):
#     ans = min(ans, f(i, -1)[1])
# print(ans)
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
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
cab = []
for _ in range(n - 1):
    a, b, c = MII()
    a -= 1
    b -= 1
    cab.append((c, a, b))
# 端
h = []
ed = [[] for _ in range(n)]
for c, a, b in cab:
    ed[a].append((c, b))
    ed[b].append((c, a))


for i in range(n):
    if len(ed[i]) == 1:
        h.append((ed[i][0][0], i))
# 根
ne = max(h)[1]
# print(max_h)
# frmから来た時のxの部分木を全部めぐってxに戻ってくるのに掛かる最小コスト
from functools import cache


@cache
def f(x, frm):
    # 往復の場合と片道両方求める
    ouhuku_num = 0
    max_diff = 0
    for c, nxt in ed[x]:
        if nxt == frm:
            continue
        rslt = f(nxt, x)
        ouhuku_num += rslt[0] + c * 2

        max_diff = max(max_diff, rslt[0] + c * 2 - (rslt[1] + c))

    katamiti_num = ouhuku_num - max_diff
    return ouhuku_num, katamiti_num


ans = inf
for _, i in h:
    ans = min(ans, f(i, -1)[1])
print(ans)
