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
alph_s = set(list(string.ascii_lowercase))
# 大文字アルファベットのリスト
alph_l = set(list(string.ascii_uppercase))

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

x, y, z = MII()
s = input()

from functools import cache


@cache
def f(i, caps):
    if i == len(s):
        return 0
    result = inf
    if caps == 0:
        if s[i] == "a":
            result = min(result, x + f(i + 1, caps))
            result = min(result, z + y + f(i + 1, caps ^ 1))

        else:
            result = min(result, y + f(i + 1, caps))
            result = min(result, z + x + f(i + 1, caps ^ 1))
    else:
        if s[i] == "A":
            result = min(result, x + f(i + 1, caps))
            result = min(result, z + y + f(i + 1, caps ^ 1))
        else:
            result = min(result, y + f(i + 1, caps))
            result = min(result, z + x + f(i + 1, caps ^ 1))
    return result


print(f(0, 0))
