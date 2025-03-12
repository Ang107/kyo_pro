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

n = II()
a = []
# s = [[] for _ in range(10**5 + 1)]
l = []
for _ in range(n):
    tmp = LMII()[1:]
    l.append(len(tmp))
    dd = defaultdict(int)
    for i in tmp:
        dd[i] += 1
    a.append(dd)
    # for i, j in dd.items():
    #     s[i].append((j, len(tmp)))
# ans = 0
# for i in range(10**5 + 1):
#     s[i].sort(key=lambda x: x[0] / x[1], reverse=True)
#     if s[i]:
#         print(i, s[i])
#     if len(s[i]) >= 2:
#         ans = max(ans, s[i][0][0] * s[i][1][0] / (s[i][0][1] * s[i][1][1]))
# print(ans)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        tmp = 0
        for k in a[i]:
            if k in a[j]:
                tmp += a[i][k] * a[j][k] / (l[i] * l[j])
        ans = max(ans, tmp)
print(ans)
