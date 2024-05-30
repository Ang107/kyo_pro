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

n = II()
str_n = str(n)
size = len(str(n))
ans = 0
for s in range(1,127):
    dp = [[[[0] * 2 for _ in range(s)] for _ in range(s+1)] for _ in range(size + 1)]
    dp[0][0][0][1] = 1
    for i in range(size):
        for j in range(s+1):
            for k in range(s):
                for l in range(2):
                    for m in range(10):
                        if j + m >s:
                            continue
                        if l and int(str_n[i]) < m:
                            continue
                        dp[i+1][j + m][(10 * k + m) % s][l and int(str_n[i]) == m] += dp[i][j][k][l]
    ans += dp[size][s][0][0] + dp[size][s][0][1]
print(ans)
                
                