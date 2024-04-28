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
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
a = LMII()
a_set = set(a)


def update(bit, idx, value, n):
    while idx <= n:
        bit[idx] += value
        idx += idx & -idx


def query(bit, idx):
    s = 0
    while idx > 0:
        s += bit[idx]
        idx -= idx & -idx

    return s


def count_higher(bit, idx, n):
    return query(bit, n) - query(bit, idx)


def solve(arr):
    max_val = max(arr)
    bit = [0] * (max_val + 1)
    result = 0
    n = len(arr)

    # 配列を逆順に処理
    for i in reversed(range(n)):
        # 現在の要素より小さい要素の総和を求める
        if arr[i] > 1:
            result += query(bit, arr[i] - 1)
        # ビットに現在の要素を加える
        update(bit, arr[i], arr[i], max_val)

    return result


print(solve(a))
