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
import inspect


# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
def deb(*vars):
    try:
        frame = inspect.currentframe().f_back
        names = {id(value): name for name, value in frame.f_locals.items()}
        for var in vars:
            var_id = id(var)
            var_name = names.get(var_id, "<unknown>")
            sys.stderr.write(f"{var_name}: {var}\n")
    except Exception as e:
        sys.stderr.write(f"Error in deb function: {e}\n")


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


def is_Kaibun(s1: str) -> bool:
    for i in range(len(s1) // 2):
        if s1[i] == s1[-i - 1]:
            pass
        else:
            return False
    return True


n, k = MII()
s = input()
tmp = {"A": 0, "B": 1}
# i文字目までで回文完成までj文字使用しているの時の通り数
# dp = [[0, 0] for _ in range(n + 1)]
# dp[0][0] = 1
# for i in range(n):
#     for j in range(2):
#         if i + 1 < k:
#             if s[i] == "A":
#                 dp[i + 1][0] += s[i][j]
#                 dp[i + 1][0] %= mod
#             elif s[i] == "B":
#                 dp[i + 1][1] += s[i][j]
#                 dp[i + 1][1] %= mod

#             else:
#                 dp[i + 1][0] += s[i][j]
#                 dp[i + 1][0] %= mod

#                 dp[i + 1][1] += s[i][j]
#                 dp[i + 1][1] %= mod
#         else:
#             if s[i] == "A":
#                 if not is_Kaibun(s[i - k : i + 1]):
#                     dp[i + 1][0] += s[i][j]
#                     dp[i + 1][0] %= mod
#             elif s[i] == "B":
#                 if not is_Kaibun(s[i - k : i + 1]):
#                     dp[i + 1][1] += s[i][j]
#                     dp[i + 1][1] %= mod

#             else:
#                 dp[i + 1][0] += s[i][j]
#                 dp[i + 1][0] %= mod

#                 dp[i + 1][1] += s[i][j]
#                 dp[i + 1][1] %= mod


dp = [[0] * (k) for _ in range(n + 1)]
dp[0][0] = 1


def is_Kaibun(s1: str) -> bool:
    for i in range(len(s1) // 2):
        if s1[i] == s1[-i - 1]:
            pass
        else:
            return False
    return True


for i in range(n):
    for j in range(k):
        if s[i] == "?":
            # Aの場合
            if j + 1 <= (k + 1) // 2 or "A" == s[i - k + j]:
                if j < k - 1:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= mod
            else:
                dp[i + 1][0] += dp[i][j]
                dp[i + 1][0] %= mod

            # Bの場合
            if j + 1 <= (k + 1) // 2 or "B" == s[i - k + j]:
                if j < k - 1:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= mod

            else:
                dp[i + 1][0] += dp[i][j]
                dp[i + 1][0] %= mod

        else:
            # 回文になるか
            print(
                dp[i][j],
                s[i],
                i - k + j,
                s[i - k + j],
                j + 1 <= (k + 1) // 2 or s[i] == s[i - k + j],
            )
            if j + 1 <= (k + 1) // 2 or s[i] == s[i - k + j]:
                if j < k - 1:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= mod
            else:
                dp[i + 1][0] += dp[i][j]
                dp[i + 1][0] %= mod

print(dp)
print(sum(dp[n]) % mod)
