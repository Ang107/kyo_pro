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

sx, sy = MII()
tx, ty = MII()
if tx < sx:
    sx, sy, tx, ty = (tx, ty, sx, sy)
ans = 0
ans += abs(ty - sy)
# if sy % 2 == 0:
#     lsx = sx // 2
# else:
#     ltx = sx // 2
# 近くに寄せる

# print(abs(tx - sx), abs(ty - sy))
# print(sx, sy, tx, ty)
if ty % 2 == 0:
    tx = max(sx, tx // 2 * 2)
else:
    if tx % 2 == 0:
        tx = max(sx, tx - 1)
# print(sx, sy, tx, ty)
if sy % 2 == 0:
    sx = min(tx, sx // 2 * 2 + 1)
else:
    if sx % 2 == 1:
        sx = min(tx, sx + 1)

# print(sx, sy, tx, ty)
lim = sx + abs(ty - sy)
if tx <= lim:
    pass
else:
    ans += -(-abs(lim - tx) // 2)
# ans +=
# if sx % 2 == tx % 2:
#     ans += max((abs(tx - sx) // 2) - abs(ty - sy), 0)
# else:
#     ans += max(-(-abs(tx - sx) // 2) - abs(ty - sy), 0)

# ans += max(-(-abs(tx - sx) // 2) - abs(ty - sy), 0)
# if ty % 2 == sy % 2:
#     ans += max(abs(tx - sx) - abs(ty - sy), 0)
# else:
#     ans += max(abs(tx - sx) - abs(ty - sy), 0)

print(ans)
