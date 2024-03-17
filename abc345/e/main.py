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
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n, k = MII()
cv = [LMII() for _ in range(n)]
need_del = 0
assyuku = []
for i in range(n - 1):
    if cv[i][0] == cv[i + 1][0]:
        need_del += 1

# print(need_del)
if need_del > k:
    print(-1)
    exit()


for i in range(n):
    if not assyuku or assyuku[-1][0] != cv[i][0]:
        assyuku.append([cv[i][0], cv[i][1]])
    else:
        assyuku[-1][1] = max(assyuku[-1][1], cv[i][1])

# i個目まででランプでj個消すときの総和の最大値
dp = [[-inf] * (k - need_del + 1) for _ in range(len(assyuku) + 1)]
dp[0][0] = 0
for i in range(1, len(assyuku) + 1):
    for j in range(k - need_del + 1):
        # del
        if j + 1 < k - need_del + 1:
            dp[i][j + 1] = max(dp[i - 1][j], dp[i][j + 1])
        # not del
        dp[i][j] = max(dp[i][j], dp[i - 1][j] + assyuku[i - 1][1])
print(dp[len(assyuku)][-1])
# assyuku = [i for _, i in assyuku]
# assyuku.sort(reverse=True)

# assyuku.extend([0] * need_del)
# print(sum(assyuku[:-k]))
# # print(assyuku)
