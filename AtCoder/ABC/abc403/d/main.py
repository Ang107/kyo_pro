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

n, d = MII()
a = LMII()
cnt = [0] * (10**6 + 1)
for i in a:
    cnt[i] += 1
if d == 0:
    print(len(a) - len(set(a)))
    exit()

ans = 0

for i in range(d):
    tmp = []
    for j in range(i, 10**6 + 1, d):
        tmp.append(cnt[j])
    # i番目の要素がjのとき(0のとき，0以外のとき)の削除個数の最小値
    dp = [[inf] * 2 for _ in range((len(tmp) + 1))]
    dp[0][0] = 0
    for j in range(len(tmp)):
        for k in range(2):
            if k == 0:
                # 削除する場合
                dp[j + 1][0] = min(dp[j + 1][0], dp[j][k] + tmp[j])

                # しない場合
                if tmp[j] > 0:
                    dp[j + 1][1] = min(dp[j + 1][1], dp[j][k])
            else:
                # 削除する場合
                dp[j + 1][0] = min(dp[j + 1][0], dp[j][k] + tmp[j])
    ans += min(dp[-1])

print(ans)
