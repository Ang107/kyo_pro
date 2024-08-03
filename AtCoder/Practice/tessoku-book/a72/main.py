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

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x):
    return print(x)


def PY():
    return print("Yes")


def PN():
    return print("No")


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


h, w, k = MII()

c = [list(input()) for _ in range(h)]
# 行を全探索して決め打ち
max_ans = 0
for i in range(1 << h):
    tmp = []
    for j in range(h):
        if i >> j & 1:
            tmp.append(j)
    if len(tmp) > k:
        continue
    nc = [l[:] for l in c]
    for l in tmp:
        nc[l] = ["#"] * w
    cnt = [0] * w
    for j in range(h):
        for l in range(w):
            if nc[j][l] == ".":
                cnt[l] += 1
    cnt.sort(reverse=True)
    # print(tmp)
    # print(tmp[: k - len(tmp)])
    ans = sum(j.count("#") for j in nc)
    ans += sum(cnt[: k - len(tmp)])
    max_ans = max(ans, max_ans)
print(max_ans)
