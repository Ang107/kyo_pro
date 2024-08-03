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
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x):
    return print(x)


def PY():
    return print("Yes")


def PN():
    return print("No")


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


def solve(n, k, a):
    # 当選に必要な最低票数がmidの時に、何人が当選するか
    def isOK1(mid):
        # def isOK2(mid2):
        #     tmp = mid
        #     tmp /= 10**8
        #     if i >= tmp * mid2:
        #         return True
        #     else:
        #         return False
        #     pass

        # def meguru2(ng, ok):
        #     while abs(ok - ng) > 1:
        #         mid = (ok + ng) // 2
        #         if isOK2(mid):
        #             ok = mid
        #         else:
        #             ng = mid
        #     return ok

        rslt = 0
        for i in a:
            rslt += i // mid
        return rslt >= k

        pass

    def meguru1(ng, ok):
        # print(ng, ok)
        while abs(ok - ng) > 0.000001:
            # print(ng, ok)
            mid = (ok + ng) / 2
            if isOK1(mid):
                ok = mid
            else:
                ng = mid
        return ok

    tmp = meguru1(10**9, 1)

    # print(tmp)
    def f(mid):
        # def isOK2(mid2):
        #     tmp = mid
        #     tmp /= 10**8

        #     if i >= tmp * mid2:
        #         return True
        #     else:
        #         return False

        # def meguru2(ng, ok):
        #     while abs(ok - ng) > 1:
        #         mid = (ok + ng) // 2
        #         if isOK2(mid):
        #             ok = mid
        #         else:
        #             ng = mid
        #     return ok

        rslt = []
        for i in a:
            rslt.append(i // mid)
        return rslt

        pass

    ans = f(tmp)
    return ans


def native(n, k, a):
    for i in range(max(a) + 1):
        cnt_sum = 0
        ans = []
        for j in a:
            cnt = 0
            for k in range(1, j + 1):
                if j / k >= i:
                    cnt += 1
            cnt_sum += cnt
            ans.append(cnt)

        if cnt_sum == k:
            return ans

    pass


if 0:
    while True:
        import random

        n = 10
        a = [random.randrange(1, 100) for _ in range(n)]
        k = random.randrange(1, 20)
        r1, r2 = solve(n, k, a), native(n, k, a)
        print(r1, r2)
        if r1 != r2:
            print(n, k, a)
            exit()
else:
    n, k = MII()
    a = LMII()
    print(*map(int, solve(n, k, a)))
