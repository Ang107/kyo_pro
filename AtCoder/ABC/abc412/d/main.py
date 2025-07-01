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

n, m = MII()
from math import comb, factorial

# print(factorial(8))

# ans = 1
# for i in range(2, 9):
#     ans *= comb(i, 2)
#     # print(comb(i, 2))
# print(ans)
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = MII()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ed = []
ans = inf
memo = [inf] * (1 << n)
for mask in range(1 << n):
    min_ = inf
    tmp = [i for i in range(n) if mask >> i & 1]
    if len(tmp) < 3:
        continue

    for p in permutations(tmp):
        ed = []
        for i in range(len(p)):
            ed.append((p[i], p[(i + 1) % len(p)]))
        res = 0
        used = 0
        for i, j in ed:
            if i in g[j]:
                used += 1
            else:
                res += 1
        for i in range(n):
            for j in g[i]:
                if i > j:
                    continue
                if i not in tmp or j not in tmp:
                    continue
                if (i, j) not in ed and (j, i) not in ed:
                    res += 1
        # res += m - used
        min_ = min(min_, res)
    # print(mask, tmp, min_)
    memo[mask] = min_
dp = [inf] * (1 << n)
dp[0] = 0


@cache
def f(mask: int):
    if mask == 0:
        return 0
    tmp = [i for i in range(n) if mask >> i & 1 == 1]
    new = 0
    for i in tmp:
        new |= 1 << i
    res = memo[new]
    for nmask in range(1, 1 << len(tmp) - 1):
        new = 0
        other = 0
        cnt0 = 0
        cnt1 = 0
        a = []
        b = []
        for i in range(len(tmp)):
            if nmask >> i & 1:
                new |= 1 << tmp[i]
                cnt0 += 1
                a.append(tmp[i])
            else:
                other |= 1 << tmp[i]
                cnt1 += 1
                b.append(tmp[i])
        c = 0
        for i in a:
            for j in b:
                if i in g[j]:
                    c += 1
        if cnt0 < 3 or cnt1 < 3:
            continue
        res = min(res, f(new) + f(other) + c)
    return res


# print(memo)
print(f((1 << n) - 1))
# ans = 0
# print(g)

# while True:
#     if all(len(i) <= 2 for i in g):
#         break
#     a = [(len(g[i]), i) for i in range(n)]
#     u = max(a)[1]
#     b = [(len(g[i]), i) for i in g[u]]
#     v = max(b)[1]
#     ans += 1
#     g[u].remove(v)
#     g[v].remove(u)
#     print(g)

# for i in range(n):
#     ans += max(0, 2 - len(g[i]))
# print(ans)
