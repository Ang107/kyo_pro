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

n, k = MII()
s = input()
ans = ["?"] * n
for i in range(n):
    if s[i] != "?":
        ans[i] = s[i]
        if s[i] == "o":
            for j in [-1, 1]:
                if i + j in range(n):
                    ans[i + j] = "."
tmp = []
cnt = 0
for i in range(n):
    if ans[i] == "?":
        cnt += 1
    else:
        tmp.append(cnt)
        cnt = 0
tmp.append(cnt)
o_cnt = ans.count("o")
need = k - o_cnt
can_put = 0
for i in tmp:
    can_put += i // 2 + i % 2
run = []
for i in ans:
    if run and run[-1][0] == i:
        run[-1][1] += 1
    else:
        run.append([i, 1])
if can_put == need:
    idx = 0
    for i, j in run:
        if i == "?":
            if j % 2 == 1:
                for l in range(j):
                    if l % 2 == 0:
                        ans[idx + l] = "o"
                    else:
                        ans[idx + l] = "."
        idx += j
if need == 0:
    for i in range(n):
        if ans[i] == "?":
            ans[i] = "."
print("".join(ans))
