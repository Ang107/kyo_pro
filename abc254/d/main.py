import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n = II()


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


# ans = 0
# for i in range(1, n + 1):
#     l = make_divisors(i**2)
#     r = len(l) - bisect_right(l, n)
#     num = len(l) - 2 * r
#     # print(l)
#     # print(num, math.ceil(num / 2))
#     # print(math.ceil(num / 2))
#     ans += math.ceil(num)
# print(ans)


# i < j
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


# ans = 0
# for i in range(1, n + 1):
#     if i == 1:
#         ans += 1
#         continue
#     l = factorization(i)

#     tmp = [1]
#     for j, k in l:
#         for m in range(k * 2):
#             tmp.append(j)
#     print(l)
#     print(tmp)
#     num = 1
#     j = 0
#     for k in tmp:
#         num *= k
#         if num <= n:
#             pass
#         else:
#             break
#         j += 1
#     print(j)
#     num = len(tmp) - 2 * (len(tmp) - j)

#     print(i, num)
#     ans += num
# print(ans)
s = []
ans = 0
for i in range(1, 2 * 10**5):
    s.append(i**2)
for i in range(1, n + 1):
    l = factorization(i)
    l = [j for j, k in l if k % 2 == 1]
    tmp = 1
    for j in l:
        tmp *= j

    for j in s:
        if tmp * j <= n:
            ans += 1
        else:
            break
    # print(i, ans)

    # print(ans)
# print(s[:20])
print(ans)
