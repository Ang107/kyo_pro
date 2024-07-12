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
a = LMII()

h = []
max_ = 2 * 10**5
for i in range(2, 1000000):
    h.append(i**2)
    if i**2 > max_:
        break


def solve(n, a):
    a_n = []
    for i in a:
        tmp = i
        for j in h:
            if j > tmp:
                break
            while tmp % j == 0:
                tmp //= j

        a_n.append(tmp)

    cnt = defaultdict(int)
    for i in a_n:
        cnt[i] += 1
    ans = 0
    # print(cnt)
    for i in cnt:
        if i == 0:
            ans += cnt[i] * (n - cnt[i])
        else:
            ans += cnt[i] * (cnt[i] - 1) // 2
        # print(ans)
    ans += cnt[0] * (cnt[0] - 1) // 2
    return ans


print(solve(n, a))
# import random

# while True:
#     n = 10
#     a = [random.randrange(100) for _ in range(10)]
#     a.sort()
#     ans = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if math.isqrt(a[i] * a[j]) ** 2 == a[i] * a[j]:
#                 ans += 1
#     tmp = solve(n, a)
#     print(ans, tmp)
#     if ans != tmp:
#         print(a)
#         print(ans, tmp)
#         exit()
