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


n = II()
s = [list(input()) for _ in range(n)]

# yoko
for i in range(n):
    deq = deque(maxlen=6)
    for j in range(n):
        deq.append(s[i][j])
        if deq.count("#") >= 4:
            PY()
            exit()

# tate
for i in range(n):
    deq = deque(maxlen=6)
    for j in range(n):
        deq.append(s[j][i])
        if deq.count("#") >= 4:
            PY()
            exit()


# 斜めに取得し、二つのリストを返す
def get_slant(l):
    n = len(l)

    # 右下→左上
    rl_d = [
        [l[max(0, -d) + i][max(0, d) + i] for i in range(n - abs(d))]
        for d in range(1 - n, n)
    ]

    # 左下→右上

    lr_d = [
        [l[max(0, d) + i][min(n + d, n) - i - 1] for i in range(n - abs(d))]
        for d in range(1 - n, n)
    ]

    return rl_d, lr_d


l1, l2 = get_slant(s)

for i in l1:
    if len(i) < 6:
        continue
    deq = deque(maxlen=6)
    for j in i:
        deq.append(j)
        if deq.count("#") >= 4:
            PY()
            exit()

for i in l2:
    if len(i) < 6:
        continue
    deq = deque(maxlen=6)
    for j in i:
        deq.append(j)
        if deq.count("#") >= 4:
            PY()
            exit()


# # naname
# for i in range(n):
#     j = 0
#     p, q = 0, 0
#     deq = deque(maxlen=6)
#     while True:
#         if i + p in range(n) and j + q in range(n):
#             deq.append(s[i + p][j + q])
#             p += 1
#             q += 1
#             if deq.count("#") >= 4 and len(deq) >= 6:
#                 PY()
#                 exit()
#         else:
#             break

# # naname
# for j in range(n):
#     i = 0
#     p, q = 0, 0
#     deq = deque(maxlen=6)
#     while True:
#         if i + p in range(n) and j + q in range(n):
#             deq.append(s[i + p][j + q])
#             p += 1
#             q += 1
#             if deq.count("#") >= 4 and len(deq) >= 6:
#                 PY()
#                 exit()
#         else:
#             break

# # naname
# for i in range(n):
#     j = 0
#     p, q = 0, 0
#     deq = deque(maxlen=6)
#     while True:
#         if i + p in range(n) and j + q in range(n):
#             deq.append(s[i + p][j + q])
#             p += 1
#             q -= 1
#             if deq.count("#") >= 4 and len(deq) >= 6:
#                 PY()
#                 exit()
#         else:
#             break


# # naname
# for j in range(n):
#     i = 0
#     p, q = 0, 0
#     deq = deque(maxlen=6)
#     while True:
#         if i + p in range(n) and j + q in range(n):
#             deq.append(s[i + p][j + q])
#             p += 1
#             q -= 1
#             if deq.count("#") >= 4 and len(deq) >= 6:
#                 PY()
#                 exit()
#         else:
#             break

PN()
