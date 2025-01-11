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


k = II()
s = input()
t = input()

if abs(len(s) - len(t)) > k:
    PN()
    exit()


# 編集距離（片方の文字列を置換、削除、挿入を繰り返し、もう片方に一致させる最小の回数）を取得
def get_Levenshtein(s, t):
    n, m = len(s), len(t)

    dp = [[inf] * (2 * k + 1) for i in range(n + 1)]
    # dp[i][j] == Sのi文字目まで、Tのj文字目までの部分列の距離
    for i in range(n + 1):
        for dj in range(-k, k + 1):
            j = i + dj
            if j < 0 or m < j:
                continue
            if j == 0:
                dp[i][dj] = i
            elif i == 0:
                dp[i][dj] = j
            else:
                if s[i - 1] == t[j - 1]:
                    if dj > -k:
                        dp[i][dj] = min(dp[i][dj], dp[i - 1][dj - 1], dp[i][dj - 1] + 1)

                    dp[i][dj] = min(
                        dp[i][dj],
                        dp[i - 1][dj] + 1,
                    )
                else:
                    if dj > -k:
                        dp[i][dj] = min(
                            dp[i][dj], dp[i - 1][dj - 1] + 1, dp[i][dj - 1] + 1
                        )

                    dp[i][dj] = min(
                        dp[i][dj],
                        dp[i - 1][dj] + 1,
                    )
    print(dp)
    return dp[n][m - n]


ans = get_Levenshtein(s, t)
if ans <= k:
    PY()
else:
    PN()

# if len(s) > len(t):
#     s, t = t, s
# n = len(s)
# m = len(t)
# d = [[] for _ in range(26)]
# for i in range(m):
#     d[t[i]].append(i)
# # sのi番目の文字列までをj回の操作で揃える時、tに割り当てたindexの最小値
# dp = [[-(1 << 60)] * (k + 1) for _ in range(n + 1)]
# dp[0][0] = -1
# for i in range(n):
#     for j in range(k + 1):
#         # 等しいものを選ぶ
#         l = bisect_left(d[s[i]], dp[i][j] + 1)
#         if l < len(d[s[i]]):
#             l = d[s[i]][l]
#             if j + (l - dp[i][j] - 1) <= k:
#                 dp[i + 1][j + (l - dp[i][j] - 1)] = max(
#                     dp[i + 1][j + (l - dp[i][j] - 1)], l
#                 )
#         # 異なるものを選ぶ
#         l = dp[i][j] + 1

#         if j + 1 <= k:
#             dp[i + 1][j + 1] = max(dp[i + 1][j + 1], l)
# for j in range(n + 1):
#     for i in range(k + 1):
#         if dp[j][i] == -(1 << 60):
#             continue
#         # print(j, i, dp[j][i], i + max(0, m - dp[j][i] - 1))

#         if i + max(0, m - dp[j][i] - 1) <= k:
#             PY()
#             exit()
# PN()
