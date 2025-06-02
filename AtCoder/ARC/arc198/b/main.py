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


def f(x, y, z):
    if z == 0 and y % 2 == 1:
        return False
    elif y <= x * 2 and z <= x:
        return True
    else:
        return False


t = II()
for _ in range(t):
    x, y, z = MII()
    if f(x, y, z):
        PY()
    else:
        PN()
# # 1を消化するには0が-(-y // 2)個以上必要
# if -(-y // 2) > x:
#     PN()
# else:
#     if z <= x:
#         PY()
#         exit()
#     if z <=
#     if 0 < z and x < z:
#         PN()
#     else:
#         PY()


def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False


def isok(l):
    n = len(l)
    for i in range(n):
        cnt = 0
        if l[(i - 1) % n] < l[i]:
            cnt += 1
        if l[(i + 1) % n] < l[i]:
            cnt += 1
        if cnt == l[i]:
            pass
        else:
            return False
    return True


for i in range(6):
    for j in range(6):
        for k in range(6):
            ok = False
            if i + j + k < 3:
                continue
            tmp = []
            tmp.extend([0] * i)
            tmp.extend([1] * j)
            tmp.extend([2] * k)
            res = False
            while True:
                ok |= isok(tmp)
                if ok:
                    break
                if not next_permutation(tmp):
                    break
            if ok != f(i, j, k):
                print(i, j, k, isok(tmp), f(i, j, k))
                exit()
