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
setrecursionlimit(10**7)
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

T = II()
for _ in range(T):
    n, k = MII()
    a = LMII()
    b = LMII()
    if k == 1:
        nb = []
        for i in b:
            if len(nb) == 0 or nb[-1] != i:
                nb.append(i)
        idx = 0
        for i in a:
            if i == nb[idx]:
                idx += 1
            if idx == len(nb):
                break
        if idx == len(nb):
            PY()
        else:
            PN()
        continue

    # a の各数字ごとのインデックス
    a_index_l = [[] for _ in range(n + 1)]
    for i in range(n):
        a_index_l[a[i]].append(i)
    # 現在の運び手の接触可能範囲の両端のインデックス
    limit_lr_l = [-1, -1]
    # 運び手になれるか
    can_move_l = [False] * n
    # 揃えらるか
    can_same_l = [False] * n
    s_l = set(a[:k])
    d_l = defaultdict(int)
    for i in a[:k]:
        d_l[i] += 1
    for i, (j, k) in enumerate(zip(a, b)):
        # 左端の削除
        if i >= k:
            d_l[a[i - k]] -= 1
            if d_l[a[i - k]] == 0:
                s_l.remove(a[i - k])
        # 右端の追加
        if i + k < n:
            d_l[a[i + k]] += 1
            if d_l[a[i + k]] == 1:
                s_l.add(a[i + k])
        if j == k:
            can_same_l[i] = True

        left_index = -1
        # 直近の左の同じ数字のインデックス
        tmp = bisect_left(a_index_l[j], i)
        if tmp < len(a_index_l[j]):
            left_index = a_index_l[j][tmp]

        if j in s_l or (
            limit_lr_l[0] <= left_index <= limit_lr_l[1] and i - k <= limit_lr_l[1]
        ):
            can_move_l[i] = True
            can_same_l[i] = True
            if i - k <= limit_lr_l[1]:
                limit_lr_l[1] = i + k
            else:
                limit_lr_l = [i - k, i + k]

    a = a[::-1]
    b = b[::-1]
    # a の各数字ごとのインデックス
    a_index_r = [[] for _ in range(n + 1)]
    for i in range(n):
        a_index_r[a[i]].append(i)
    # 現在の運び手の接触可能範囲の両端のインデックス
    limit_lr_r = [-1, -1]
    # 運び手になれるか
    can_move_r = [False] * n
    # 揃えらるか
    can_same_r = [False] * n
    s_r = set(a[:k])
    d_r = defaultdict(int)
    for i in a[:k]:
        d_r[i] += 1
    for i, (j, k) in enumerate(zip(a, b)):
        # 左端の削除
        if i >= k:
            d_r[a[i - k]] -= 1
            if d_r[a[i - k]] == 0:
                s_r.remove(a[i - k])
        # 右端の追加
        if i + k < n:
            d_r[a[i + k]] += 1
            if d_r[a[i + k]] == 1:
                s_r.add(a[i + k])
        if j == k:
            can_same_r[i] = True

        left_index = -1
        # 直近の左の同じ数字のインデックス
        tmp = bisect_left(a_index_r[j], i)
        if tmp < len(a_index_r[j]):
            left_index = a_index_r[j][tmp]

        if j in s_r or (
            limit_lr_r[0] <= left_index <= limit_lr_r[1] and i - k <= limit_lr_r[1]
        ):
            can_move_r[i] = True
            can_same_r[i] = True
            if i - k <= limit_lr_r[1]:
                limit_lr_r[1] = i + k
            else:
                limit_lr_l = [i - k, i + k]

    can_same_r = can_same_r[::-1]
    # print(can_same_l)
    # print(can_same_r)
    # print(can_move_l)
    # print(can_move_r)
    if all(i or j for i, j in zip(can_same_l, can_same_r)):
        PY()
    else:
        PN()
