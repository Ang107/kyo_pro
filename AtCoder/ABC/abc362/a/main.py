# import sys
# from collections import deque, defaultdict
# from itertools import (
#     accumulate,  # 累積和
#     product,  # bit全探索 product(range(2),repeat=n)
#     permutations,  # permutations : 順列全探索
#     combinations,  # 組み合わせ（重複無し）
#     combinations_with_replacement,  # 組み合わせ（重複可）
# )
# import math
# from bisect import bisect_left, bisect_right
# from heapq import heapify, heappop, heappush
# import string

# # 外部ライブラリ
# # from sortedcontainers import SortedSet, SortedList, SortedDict
# sys.setrecursionlimit(10**7)
# alph_s = tuple(string.ascii_lowercase)
# alph_l = tuple(string.ascii_uppercase)
# around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
# around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
# inf = float("inf")
# mod = 998244353
# input = lambda: sys.stdin.readline().rstrip()
# pritn = lambda *x: print(*x)
# PY = lambda: print("Yes")
# PN = lambda: print("No")
# SI = lambda: input()
# IS = lambda: input().split()
# II = lambda: int(input())
MII = lambda: map(int, input().split())
# LMII = lambda: list(map(int, input().split()))

r, g, b = MII()
c = input()
if c == "Blue":
    print(min(r, g))
if c == "Green":
    print(min(b, r))
if c == "Red":
    print(min(b, g))

# 入力の受取
R, G, B = map(int, input().split())
l = list(map(int, input().split()))

R, G, B = input().split()
# 整数型への変換
R = int(R)
G = int(G)
B = int(B)
# 辞書の作成
d = {"Red": R, "Green": G, "Blue": B}
C = input()
del d[C]
ans = min(d.values())
print(ans)
