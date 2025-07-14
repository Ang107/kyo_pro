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

a = II()
n = II()


def to_base_a(x, a):
    if a >= 3:
        tmp = []
        while True:
            tmp.append(str(x % a))
            x //= a
            if x == 0:
                break
        tmp.reverse()
        tmp = "".join(tmp)
        return str(int(tmp))
    else:
        return bin(x)[2:]


ans = 0
num = [str(i) for i in range(10)]
for i in range(1, 10):
    if 1 <= i <= n:
        base_a = to_base_a(i, a)
        if base_a == base_a[::-1]:
            ans += i
for p in product(num, repeat=5):
    # print(p)
    np = []
    for i in p:
        if np:
            np.append(i)
        elif i != "0":
            np.append(i)
    p = "".join(np)
    for i in num:
        if not p:
            continue
        tmp = p + i + p[::-1]
        tmp = int(tmp)

        if tmp > n or tmp < 1:
            continue
        base_a = to_base_a(tmp, a)
        if base_a == base_a[::-1]:
            ans += tmp

for p in product(num, repeat=6):
    # print(p)
    np = []
    for i in p:
        if np:
            np.append(i)
        elif i != "0":
            np.append(i)
    p = "".join(np)
    if not p:
        continue
    tmp = p + p[::-1]
    tmp = int(tmp)

    if tmp > n or tmp < 1:
        continue
    base_a = to_base_a(tmp, a)
    if base_a == base_a[::-1]:
        ans += tmp
print(ans)
