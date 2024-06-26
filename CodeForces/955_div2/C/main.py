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

t = II()
ans = []

for _ in range(t):
    n, l, r = MII()
    a = LMII()
    rslt = 0
    # dp =
    tmp = deque()
    tmp_sum = 0
    for i in a:
        # print(tmp, rslt)
        tmp_sum += i
        tmp.append(i)
        if l <= tmp_sum:
            while True:
                if l <= tmp_sum <= r:
                    tmp = deque()
                    tmp_sum = 0
                    rslt += 1
                    break
                if tmp_sum < l:
                    break
                if not tmp:
                    break
                tmp_sum -= tmp.popleft()

    ans.append(rslt)

    pass
for i in ans:
    print(i)
