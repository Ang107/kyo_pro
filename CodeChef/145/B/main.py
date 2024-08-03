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

T = II()
ans = []


def solve(n, s):
    cnt = 0
    if all(i == "1" for i in s):
        return 0
    elif all(i == "0" for i in s):
        return min(n, 2)
    else:
        cnt = (s[0] == "0") + (s[-1] == "0")
        return cnt
    # else:
    #     cnt = 0
    #     for i in s:
    #         if i == "1":
    #             break
    #         else:
    #             cnt += 1
    #     for i in s[::-1]:
    #         if i == "1":
    #             break
    #         else:
    #             cnt += 1
    #     return cnt


# def native(n,s):


for _ in range(T):
    n = II()
    s = input()

    # print(ans)
    ans.append(solve(n, s))
    pass

for i in ans:
    print(i)
