import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

T = II()
ans = []


for _ in range(T):
    n, q = MII()
    a = LMII()
    cnt = [[] for _ in range(25)]
    bit01 = [[] for _ in range(25)]
    runlength = [[] for _ in range(25)]
    pref_0 = []
    pref_1 = []
    for b in range(25):
        cnt[b].append(a[0] >> b & 1)
        for i in range(1, n):
            if a[i - 1] >> b & 1 != a[i] >> b & 1:
                cnt[b].append(a[i] >> b & 1)
    for b in range(25):
        for i in range(n):
            bit01[b].append(a[i] >> b & 1)
            if not runlength[b] or runlength[b][-1][0] != a[i] >> b & 1:
                runlength[b].append([a[i] >> b & 1, i, i])
            else:
                runlength[b][-1][2] = i

    for i in range(25):
        pref_1.append([0] + list(accumulate(bit01[i])))
        tmp = []
        for i in range(n + 1):
            tmp.append(i - pref_1[-1][i])
        pref_0.append(tmp)

    # print(pref_0)
    # print(pref_1)
    # print(bit01)
    # print(runlength)

    ncnt = [-1] * 25
    for i in range(25):
        ncnt[i] = cnt[i].count(0)
    # iの0の部分にxをあてたときに、change[i][j]がオール1になるのに必要なx >> j
    change_1 = [[-1] * 25 for _ in range(25)]
    for i in range(25):
        for j in range(i):
            rslt = -1
            for b, l, r in runlength[i]:
                if b == 1:
                    if pref_1[j][r + 1] - pref_1[j][l] == r - l + 1:
                        pass
                    else:
                        rslt = -1
                        break
                else:
                    if pref_1[j][r + 1] - pref_1[j][l] == r - l + 1:
                        if rslt == -1:
                            rslt = 0
                        elif rslt == 0:
                            pass
                        elif rslt == 1:
                            rslt = -1
                            break
                    elif pref_0[j][r + 1] - pref_0[j][l] == r - l + 1:
                        if rslt == -1:
                            rslt = 1
                        elif rslt == 1:
                            pass
                        elif rslt == 0:
                            rslt = -1
                            break
                    else:
                        rslt = -1
                        break
            change_1[i][j] = rslt
    # for i in range(25):
    #     for j in range(i):
    #         print(i, j, change_1[i][j])

    init = a[0]
    for i in a:
        init &= i

    for _ in range(q):
        k, x = MII()
        # 使用する場所が確定した場合
        f = False
        c = -1
        rslt = 0
        for i in reversed(range(25)):

            if not f and init >> i & 1 and x >> i & 1:
                rslt = init
                break
            elif not f and init >> i & 1 and x >> i & 1 == 0:
                rslt |= 1 << i

            if not f:
                if x >> i & 1 == 0:
                    continue
                elif k >= ncnt[i]:
                    f = True
                    c = i
                    rslt += 1 << i
            else:
                if change_1[c][i] == x >> i & 1:
                    rslt |= 1 << i
        ans.append(rslt)

    pass


for i in ans:
    print(i)
