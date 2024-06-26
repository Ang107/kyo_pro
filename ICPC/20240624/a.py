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


def solve(n, s):
    # s.sort()
    ans = 0
    for i in range(n):
        l_max = -inf
        r_min = inf

        for j in range(n):
            if i == j:
                continue
            if len(s[i]) == len(s[j]) and s[i][0] == s[j][0] and s[i][-1] == s[j][-1]:
                for k in range(1, len(s[i]) - 1):
                    if s[i][k] != s[j][k]:
                        l = k
                        break
                for k in reversed(range(1, len(s[i]) - 1)):
                    if s[i][k] != s[j][k]:
                        r = k
                        break

                l_max = max(l_max, l)
                r_min = min(r_min, r)

        tmp = max(len(s[i]) - l_max - 2, r_min - 1)
        if tmp == inf:
            ans += len(s[i]) - 2
        else:
            ans += tmp

    return ans


ans = []

while 1:
    # 入力を記入
    n = II()
    if n == 0:
        break
    s = [input() for _ in range(n)]
    ans.append(solve(n, s))
    pass

for i in ans:
    print(i)
