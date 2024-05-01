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


x = II()
cnd = list(range(10))

# 桁数
for i in range(2, 19):
    # 変化なし
    # 左端の数字
    for j in range(1, 10):
        tmp = []
        for l in range(i):
            tmp.append(str(j))
        cnd.append(int("".join(tmp)))

    # 増加
    # 左端の数字
    for j in range(1, 11 - i):
        # 等差
        for k in range(1, (9 - j) // (i - 1) + 1):
            tmp = []
            # print(i, j, k)
            for l in range(i):
                tmp.append(str(j + k * l))
            cnd.append(int("".join(tmp)))

    # 減少
    # 左端の数字
    for j in range(i - 1, 10):
        # 等差
        for k in range(1, j // (i - 1) + 1):
            tmp = []
            # print(i, j, k)
            for l in range(i):
                tmp.append(str(j - k * l))
            cnd.append(int("".join(tmp)))
cnd.sort()
idx = bisect_left(cnd, x)
print(cnd[idx])
