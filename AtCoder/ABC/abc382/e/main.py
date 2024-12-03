from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, x = MII()
p = LMII()
np = [i * 0.01 for i in p]
tmp = 0
# i枚目までにj枚でる確率
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        dp[i + 1][j] += dp[i][j] * (1 - np[i])
        dp[i + 1][j + 1] += dp[i][j] * np[i]

# print(dp[n])


# 残りn枚以上のカードを出すのに必要なパックの数の期待値
@cache
def f(m):
    res = 0
    if m <= 0:
        return res
    for i in range(1, n + 1):
        res += (1 / (1 - dp[n][0]) + f(m - i)) * dp[n][i] / (1 - dp[n][0])
    return res


ans = f(x)


print(ans)
# for i in range(10):
#     print(i, f(i))
