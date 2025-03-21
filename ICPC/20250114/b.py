from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
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
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def solve(n, c, p, q, s):
    rank = 0
    correct = 0
    incorrect = 0
    visited = 0
    ans = 0
    y_pref = [0]
    n_pref = [0]
    for i in s:
        if i == "Y":
            y_pref.append(y_pref[-1] + 1)
            n_pref.append(n_pref[-1])
        else:
            y_pref.append(y_pref[-1])
            n_pref.append(n_pref[-1] + 1)

    for i in range(n + 1):
        for j in range(max(visited, i - 2 * c - 10), i + 1):
            if i - j < c:
                break
            y_cnt = y_pref[i] - y_pref[j]
            n_cnt = n_pref[i] - n_pref[j]
            if y_cnt * q >= p * (y_cnt + n_cnt):
                # if y_cnt / (y_cnt + n_cnt) >= p / q:
                visited = i
                ans += 1
                break

    return ans


def native(n, c, p, q, s):
    ans = 0
    visited = 0
    y_pref = [0]
    n_pref = [0]
    for i in s:
        if i == "Y":
            y_pref.append(y_pref[-1] + 1)
            n_pref.append(n_pref[-1])
        else:
            y_pref.append(y_pref[-1])
            n_pref.append(n_pref[-1] + 1)
    for r in range(n + 1):
        for l in range(visited, r + 1):
            if r - l < c:
                break
            y_cnt = y_pref[r] - y_pref[l]
            n_cnt = n_pref[r] - n_pref[l]
            # if y_cnt / (y_cnt + n_cnt) >= p / q:
            if y_cnt * q >= p * (y_cnt + n_cnt):
                # print(l, r)
                visited = r
                ans += 1
                break
    return ans


n, c, p, q = MII()
s = input()
print(solve(n, c, p, q, s))
