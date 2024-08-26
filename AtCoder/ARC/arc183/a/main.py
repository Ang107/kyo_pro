from sys import stdin, setrecursionlimit
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


# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

DEBUG = False
n, k = MII()
if not DEBUG:
    tmp = []
    for i in range(1, n + 1):
        tmp.extend([i] * k)
    if n % 2 == 0:
        index = tmp.index(n // 2)
    else:
        index = tmp.index(n // 2 + 1)

    ans = []
    if n % 2 == 0:
        ans.append(tmp[index])
        ans.extend(tmp[index + 1 :][::-1])
        ans.extend(tmp[:index][::-1])
    else:
        l = k * (n // 2)
        r = l + k
        ans.extend(tmp[l - 1 : r][::-1])
        ans.extend(tmp[r:][::-1])
        ans.extend(tmp[: l - 1][::-1])
    print(*ans)

else:

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

    import random
    import math

    # for n in range(1, 5):
    #     for k in range(1, 5):
    # n = random.randrange(1, 4)
    # k = random.randrange(1, 4)
    tmp = math.perm(n * k) // math.perm(k) ** n
    l = []
    print(f"{n=},{k=}")
    for i in range(1, n + 1):
        l.extend([i] * k)
    print(l)
    # print(tmp)
    for _ in range((tmp + 1) // 2 - 1):
        next_permutation(l)
    print(l)
