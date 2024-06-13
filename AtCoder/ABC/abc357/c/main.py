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
ans = [None] * 7
ans[0] = ["#"]
ans[1] = [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]]
for i in range(2, 7):
    rslt = [["."] * (3**i) for _ in range(3**i)]
    for j in range(3**i):
        for k in range(3**i):
            if j // (3 ** (i - 1)) != 1 or k // (3 ** (i - 1)) != 1:
                rslt[j][k] = ans[i - 1][j % (3 ** (i - 1))][k % (3 ** (i - 1))]
    ans[i] = rslt
    # tmp = []
    # for _ in range(3):
    #     tmp.append(ans[i - 1])
    # rslt.append(tmp)

    # tmp = []
    # tmp.append(ans)
    # tmp.append("." * (3 * i))

    # ans[i]
for i in ans[n]:
    print("".join(i))
