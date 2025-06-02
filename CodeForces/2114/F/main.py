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

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
# setrecursionlimit(10**7)
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


t = II()
ans = []


# 素因数分解
# 戻り値は(素因数、指数)のタプル)
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


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


for _ in range(t):
    x, y, k = MII()
    k = min(max(x, y), k)
    cnt = 0
    # まず最大公約数になるまで割る
    # そのあと良い感じに書ける
    gcd_ = gcd(x, y)
    tmp = x // gcd_
    # k以下の整数の積でtmpを作る
    # 約数列挙して大きい方から貪欲に
    div = make_divisors(tmp)[1:]
    now = x
    for i in div[::-1]:
        if i <= k:
            while tmp % i == 0:
                # print("/", i, now, now // tmp)
                # now //= tmp
                cnt += 1
                tmp //= i
    if tmp != 1:
        ans.append(-1)
        continue
    tmp = y // gcd_

    div = make_divisors(tmp)[1:]
    div = div[: bisect_right(div, k)]

    for i in div[::-1]:
        if i <= k:
            while tmp % i == 0:
                tmp //= i
    if tmp != 1:
        ans.append(-1)
        continue

    tmp = y // gcd_
    edge = [[] for _ in range(tmp + 1)]
    for i in div:
        for j in range(1, tmp + 1):
            if i * j <= tmp:
                edge[j].append(i * j)
            else:
                break
        for j in range(1, tmp + 1):
            if i * (j + 1) <= tmp:
                edge[i * (j + 1)].append(i * j)
    deq = deque([1])
    cnts = [-1] * (tmp + 1)
    cnts[1] = 0
    while deq:
        v = deq.popleft()
        for next in edge[v]:
            if cnts[next] == -1:
                deq.append(next)
                cnts[next] = cnts[v] + 1
    if cnts[tmp] == -1:
        ans.append(-1)
    else:
        cnt += cnts[tmp]
        ans.append(cnt)

    # dp = [1 << 60] * (tmp + 1)

    # dp[1] = 0
    # for i in range(1, tmp):
    #     if dp[i] == 1 << 60:
    #         continue
    #     for j in div:
    #         if i % j == 0:
    #             dp[i // j] = min(dp[i // j], dp[i] + 1)
    #         if i * j <= tmp:
    #             dp[i * j] = min(dp[i * j], dp[i] + 1)
    #         else:
    #             break

    # for i in range(1, tmp):
    #     if dp[i] == 1 << 60:
    #         continue
    #     for j in div:
    #         if i * j <= tmp:
    #             dp[i * j] = min(dp[i * j], dp[i] + 1)
    #         else:
    #             break

    # cnt += dp[tmp]

    # if cnt == 1 << 60:
    #     cnt = -1
    # ans.append(cnt)
    pass
for i in ans:
    print(i)
