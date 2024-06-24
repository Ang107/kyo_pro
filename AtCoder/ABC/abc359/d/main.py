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


def is_Kaibun(s1: str) -> bool:
    for i in range(len(s1) // 2):
        if s1[i] == s1[-i - 1]:
            pass
        else:
            return False
    return True


dp = [[0] * (1 << k) for _ in range(n + 1)]
s_n = []
for i in s:
    if i == "?":
        s_n.append("-1")
    elif i == "A":
        s_n.append("0")
    elif i == "B":
        s_n.append("1")

s = s_n
# print(s)


# 最初のk-1文字の配置
def is_match(cand, part_of_s):
    for i, j in zip(cand, part_of_s):
        if j == "?" or i == j:
            pass
        else:
            return False
    return True


cand = [""]
for i in range(k - 1):
    # print(cand)
    new_cand = []
    for c in cand:
        if s[i] == "-1":
            new_cand.append(c + "0")
            new_cand.append(c + "1")
        else:
            new_cand.append(c + s[i])
    cand = new_cand

dp = defaultdict(int)
for i in cand:
    dp[i] += 1
# pritn(cand)

for i in range(k - 1, n):
    # pritn(dp)
    n_dp = defaultdict(int)
    for key, val in dp.items():
        if s[i] == "-1":
            if not is_Kaibun(key + "0"):
                n_dp[key[1:] + "0"] += dp[key]
                n_dp[key[1:] + "0"] %= mod
            if not is_Kaibun(key + "1"):
                n_dp[key[1:] + "1"] += dp[key]
                n_dp[key[1:] + "1"] %= mod

        else:
            if not is_Kaibun(key + s[i]):
                n_dp[key[1:] + s[i]] += dp[key]
                n_dp[key[1:] + s[i]] %= mod

    dp = n_dp

print(sum(dp.values()) % mod)
