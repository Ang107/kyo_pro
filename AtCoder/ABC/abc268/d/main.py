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

n, m = MII()
s = [input() for _ in range(n)]
sum_s_len = sum(len(i) for i in s)
under_bar_len = 16 - sum_s_len - (n - 1)
t = {input() for _ in range(m)}

for i in permutations(s):
    tmp = []
    for idx, j in enumerate(i):
        if idx == n - 1:
            tmp.append(j)
        else:
            tmp.append(j + "_")
    tmp_len = len("".join(tmp))
    # print(tmp)
    for j in product(range(under_bar_len + 1), repeat=n - 1):
        result = []
        if not 3 <= sum(j) + tmp_len <= 16:
            continue
        for idx, k in enumerate(j):
            result.append(tmp[idx])
            result.append("_" * k)

        result.append(tmp[-1])
        result = "".join(result)
        if result not in t:
            print(result)
            exit()

print(-1)
