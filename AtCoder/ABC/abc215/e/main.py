import sys

import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
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

from functools import cache


# @cache
# def f(idx, visited, prv):
#     if idx >= n:
#         return 0
#     result = 1
#     result += f(idx + 1, visited, prv)
#     result %= mod

#     num = ord(s[idx]) - ord("A")
#     if num != prv and (visited >> num) & 1:
#         pass
#     else:
#         result += f(idx + 1, visited | (1 << num), num)
#         result %= mod
#     # for i in range(idx, n):
#     #     num = ord(s[i]) - ord("A")
#     #     if num != prv and (visited >> num) & 1:
#     #         pass
#     #     else:
#     #         result += f(i + 1, visited | (1 << num), num) + 1
#     #         result %= mod
#     # print(idx, bin(visited), prv, result)
#     return result


# print(f(0, 0, -1))
# i文字目までで到達済みがjで最後の文字がkの通り数
dp = [[[0] * 11 for _ in range(2**10)] for _ in range(n + 1)]
dp[0][0][10] = 1
for i in range(n):
    for j in range(2**10):
        for k in range(11):

            # not use
            dp[i + 1][j][k] += dp[i][j][k]
            dp[i + 1][j][k] %= mod
            # use
            num = ord(s[i]) - ord("A")
            if num != k and j >> num & 1:
                pass
            else:
                dp[i + 1][j | (1 << num)][num] += dp[i][j][k]
                dp[i + 1][j | (1 << num)][num] %= mod
ans = 0
for j in range(2**10):
    for k in range(10):
        ans += dp[n][j][k]
        ans %= mod

print(ans)
