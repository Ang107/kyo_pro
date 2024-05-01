import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
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
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
mod = 998244353
def input(): return sys.stdin.readline().rstrip()
def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill]*l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n, k, d = MII()
a = LMII()
# tmp = []
# for i in combinations(a,k):
#     tmp.append(sum(i))
# # print(tmp)
# tmp.sort(reverse=True)
# for i in tmp:
#     if i % d == 0:
#         print(i)
#         exit()
# print(-1)
dp = [[[-1] * d for _ in range(k+10)]for _ in range(n+10)]
dp[0][0][0] = 0
# pprint(dp)
# print(n,k,d)
for i in range(n):
    for j in range(k+1):
        for l in range(d):
            # if (dp[i][j][l] == -1): continue
            # print(i,j,l,(l+a[i]) % d)
            dp[i+1][j][l] = max(dp[i+1][j][l], dp[i][j][l])
            if (dp[i][j][l] != -1): 
                dp[i+1][j+1][(l+a[i]) % d] = max(dp[i+1][j+1][(l+a[i]) % d], dp[i][j][l]+a[i])

# pprint(dp)
print(dp[n][k][0])