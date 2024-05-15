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


n, k = MII()
a = LMII()


def isOK(mid):
    # mid以上のものに乗った時の搭乗回数
    tmp = 0
    for i in a:
        tmp += max(0, i - mid + 1)
    return tmp <= k
    pass


def meguru(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = 0
num = meguru(0, 10**10)
for i in a:
    if num <= i:
        ans += (num + i) * (i - num + 1) // 2
        k -= i - num + 1
ans += k * (num - 1)
print(ans)


# a.sort()
# d = defaultdict(int)
# d[0] = 0
# for i in a:
#     d[i] += 1
# ans = 0
# h_and_num = list(list(i) for i in d.items())
# while k > 0 and len(h_and_num) > 1:
#     h, num = h_and_num.pop()

#     if k >= num * (h - h_and_num[-1][0]):
#         k -= num * (h - h_and_num[-1][0])
#         ans += num * (h - h_and_num[-1][0]) * (h + h_and_num[-1][0] + 1) // 2
#         h_and_num[-1][1] += num

#     else:
#         tmp = k // num
#         k -= num * (tmp)
#         ans += num * tmp * (h + h - tmp + 1) // 2
#         ans += k * (h - tmp)
#         k = 0

# print(ans)
