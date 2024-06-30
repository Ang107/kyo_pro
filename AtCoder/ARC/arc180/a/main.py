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
mod = 10**9 + 7
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
s = input()
tmp = []
part = []
for i in s:
    if not part or part[-1] != i:
        part.append(i)
    else:
        tmp.append(len(part))
        part = [i]
    # pritn(part)
    # pritn(tmp)
tmp.append(len(part))
# pritn(part)
# pritn(tmp)
ans = 1
for i in tmp:
    if i > 2:
        # pritn((i - 1) // 2 + 1)
        ans *= (i - 1) // 2 + 1
        ans %= mod
pritn(ans)

# s_n = []
# def solve(s):
#     ans = set([s])
#     for i in range(len(s)):


# A:0,B:1

# dp = defaultdict(int)

# for i in range(1,n):
#     dp_n = defaultdict(int)
#     for l,j in dp_n:
#         if j == "AB":


# 最大何回出来るか、そのうち何回するか？
# tmp = []
# cnt = 0
# for i in s:
#     tmp.append(i)
#     while True:
#         if tmp[-3:] == ["A", "B", "A"]:
#             cnt += 1
#             for _ in range(3):
#                 tmp.pop()
#             tmp.append("A")
#         elif tmp[-3:] == ["B", "A", "B"]:
#             cnt += 1
#             for _ in range(3):
#                 tmp.pop()
#             tmp.append("B")
#         else:
#             break

# print(pow(2, cnt, mod))
