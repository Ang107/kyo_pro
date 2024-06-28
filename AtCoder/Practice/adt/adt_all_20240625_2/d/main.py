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

n, k = MII()
a = set([i - 1 for i in LMII()])
light = []
non_light = []
for i in range(n):
    x, y = MII()
    if i in a:
        light.append((x, y))
    else:
        non_light.append((x, y))
ans = -1


def dis(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


for i in non_light:
    tmp_min = inf
    for j in light:
        tmp_min = min(tmp_min, dis(i, j))
    ans = max(ans, tmp_min)
print(ans)
