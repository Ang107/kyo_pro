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

t = II()
for _ in range(t):
    n = II()
    s = LMII()
    ss = s[0]
    sg = s[-1]
    s = sorted(set(s[1:-1]))
    ans = [ss]
    now = ss
    for idx, i in enumerate(s):
        if sg <= ans[-1] * 2:
            break
        if now * 2 < i:
            ans.append(s[idx - 1])
            now = s[idx - 1]
    if s and ans[-1] * 2 < sg:
        ans.append(s[-1])
    ans.append(sg)
    # print(ans)
    if all(ans[i + 1] <= ans[i] * 2 for i in range(len(ans) - 1)):
        print(len(ans))
    else:
        print(-1)
