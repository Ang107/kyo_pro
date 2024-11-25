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
# setrecursionlimit(10**7)
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


# 約数列挙
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


t = II()
for _ in range(t):
    x, m = MII()
    div = make_divisors(x)
    ans = []
    for i in div:
        y = x ^ i
        if 1 <= y <= m:
            ans.append(y)
    l = len(bin(x)[2:])
    tmp = 1 << len(bin(x)[2:])

    for y in range(1, 2 * x + 1):
        tmp = x ^ y
        if tmp == 0:
            continue
        if 1 <= y <= m and (y % tmp == 0 or x % tmp == 0):
            # ans += 1
            # print(y, m, y <= m)
            # print(y, tmp)
            ans.append(y)
    ans.sort()
    cnt = 0
    for i in range(len(ans)):
        if i == 0:
            cnt += 1
        else:
            if ans[i] != ans[i - 1]:
                cnt += 1
    # print(ans)
    print(cnt)


# for i in range(20):
#     print(i, bin(i)[2:])
