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


n, x = MII()
AB = [LMII() for _ in range(n)]

min_time = [sum(AB[0])]
idx = 0
for i, j in AB:
    tmp = j
    tmp = min(tmp, min_time[-1])
    if idx < n - 1:
        tmp = min(tmp, sum(AB[idx + 1]))
    min_time.append(tmp)
    idx += 1

tmp = list(accumulate([sum(i) for i in AB]))

ans = inf
# print(min_time)
# print(tmp)
for i in range(n):
    # print(tmp[i] + (x - i) * min_time[i + 1])
    ans = min(ans, tmp[i] + (x - i - 1) * min_time[i + 1])

print(ans)
# dp = [[inf] * (n + 1) for _ in range(n + 1)]

# 最大クリア数jでi回目のクリアをしたときの最短経過時間
# dp[0][0] = 0
# # print(min_time)
# for i in range(1, n + 1):
#     for j in range(n + 1):
#         # 既クリア
#         if j > 0:
#             dp[i][j] = dp[i - 1][j] + min_time[j]
#         # 未クリア
#         if 0 < j:
#             dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + sum(AB[j - 1]))

# # print(dp)
# if x <= n:
#     print(min(dp[x]))
#     exit()
# ans = [inf] * (n + 1)
# for i, j in enumerate(dp[n]):
#     ans[i] = j + min_time[i] * (x - n)
# print(min(ans))
