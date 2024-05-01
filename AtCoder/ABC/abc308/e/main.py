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
s = input()
d = {}
d["M"] = [[0],[0],[0]]
d["E"] = [[0],[0],[0]]
d["X"] = [[0],[0],[0]]
for i,j in zip(a,s):
    for k in "MEX":
        for l in range(3):
            d[k][l].append(d[k][l][-1])
            if k == j and l == i:
                d[k][l][-1] += 1
ans = 0
for idx,(i,j) in enumerate(zip(a,s)):
    if j == "E":
        if i == 0:
            tmp = d["M"][0][idx] * (d["X"][2][-1] - d["X"][2][idx]) + d["M"][2][idx] * (d["X"][0][-1] - d["X"][0][idx]) + d["M"][2][idx] * (d["X"][2][-1] - d["X"][2][idx]) + d["M"][0][idx] * (d["X"][0][-1] - d["X"][0][idx]) 
            ans += 1 * tmp
            tmp = d["M"][0][idx] * (d["X"][1][-1] - d["X"][1][idx]) + d["M"][1][idx] * (d["X"][0][-1] - d["X"][0][idx]) + d["M"][1][idx] * (d["X"][1][-1] - d["X"][1][idx])
            ans += 2 * tmp
            tmp = d["M"][1][idx] * (d["X"][2][-1] - d["X"][2][idx]) + d["M"][2][idx] * (d["X"][1][-1] - d["X"][1][idx]) 
            ans += 3 * tmp
            
        elif i == 1:
            tmp = d["M"][0][idx] * (d["X"][1][-1] - d["X"][1][idx]) + d["M"][1][idx] * (d["X"][0][-1] - d["X"][0][idx]) + d["M"][0][idx] * (d["X"][0][-1] - d["X"][0][idx])
            ans += 2 * tmp
            tmp = d["M"][0][idx] * (d["X"][2][-1] - d["X"][2][idx]) + d["M"][2][idx] * (d["X"][0][-1] - d["X"][0][idx]) 
            ans += 3 * tmp
            
        elif i == 2:
            tmp = d["M"][0][idx] * (d["X"][2][-1] - d["X"][2][idx]) + d["M"][2][idx] * (d["X"][0][-1] - d["X"][0][idx]) + d["M"][0][idx] * (d["X"][0][-1] - d["X"][0][idx])
            ans += 1 * tmp
            tmp = d["M"][1][idx] * (d["X"][0][-1] - d["X"][0][idx]) + d["M"][0][idx] * (d["X"][1][-1] - d["X"][1][idx]) 
            ans += 3 * tmp
            
    # print(i,j,ans)
print(ans)
            
                