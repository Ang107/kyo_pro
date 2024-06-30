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
a = LMII()
a = [i for i in a]
# ans = set()
# for i in range(1, n + 1):
#     for j in combinations(range(n), r=i):
#         a_n = a[:]
#         tmp = 0
#         for k in j:
#             a_n[k] += tmp
#             tmp += a[k]
#         ans.add(tuple(a_n))
# for i in ans:
#     print(i)


ans = 1
s = set()
s.add(a[0])
# 長さが2の時を計算
for i in a[1:]:
    print(len(s))
    ans += len(s)
    if i != 0:
        s.add(i)

sum_ = sum(i for i in a if i > 0)
# i番目までで長さがjで総和がkの時の時の通り数
dp = [[[0] * (2010) for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][0][1000] = 1
for i in range(1, n):
    for j in range(n):
        for k in range(1010):
            # i番目の要素を採用する場合
            # 累積和が0にならないなら
            if (k != 1000 or a[i] != 1000) and k + a[i] < 2010:
                dp[i + 1][j + 1][k + a[i]] += dp[i][j][k]
                dp[i + 1][j + 1][k + a[i]] %= mod
            # しない場合
            dp[i + 1][j][k] += dp[i][j][k]
            dp[i + 1][j][k] %= mod
print(ans)

print((dp[n][0][990:1010]))
print((dp[n][1][990:1010]))
print((dp[n][2][990:1010]))
print((dp[n][3][990:1010]))
# print((dp[n][4][990:1010]))
