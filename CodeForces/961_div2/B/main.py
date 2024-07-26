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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
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

t = II()
ans = []
import random


for _ in range(t):
    xor = random.randrange(1, 1 << 61)
    n, m = MII()
    a = LMII()
    c = LMII()
    a_n = defaultdict(int)
    for i, j in zip(a, c):
        a_n[xor ^ i] = j
    rslt = 0

    for i in list(a_n):
        m_n = m
        j = i ^ xor
        tmp = a_n[i] * j + a_n[(j + 1) ^ xor] * (j + 1)
        if tmp <= m_n:
            rslt = max(rslt, tmp)
        else:
            tmp = min(-(-m_n) // (j + 1), a_n[(j + 1) ^ xor]) * (j + 1)

            if tmp > m and tmp - m <= a[i]:
                rslt = m

            tmp = min(m_n // j, a_n[i]) * j
            # print(tmp, m_n - tmp, m_n - tmp >= j + 1)
            if m_n - tmp >= j + 1:
                # print(j, a_n[i], j + 1, a_n[(j + 1) ^ xor])
                m_n -= tmp
                tmp2 = a_n[(j + 1) ^ xor]
                tmp3 = min(m_n // (j + 1), a_n[(j + 1) ^ xor])
                tmp2 -= tmp3
                tmp = tmp3 * (j + 1)
                m_n -= tmp
                # print(tmp2, tmp3, tmp, m_n)
                rslt = max(rslt, m - max(0, m_n - tmp2))

            else:
                m_n -= tmp
                rslt = max(rslt, m - max(0, m_n - a_n[(j + 1) ^ xor]))

            # herasu以上で最も小さい数を構成する方法

            # if m % 2 == 0:

            # tmp += min(m_n // j, a_n[i]) * j
            # m_n -= min(m_n // j, a_n[i]) * j
            # tmp += min(m_n, a_n[(j + 1) ^ xor]) * (j + 1)
            # m_n -= min(m_n, a_n[(j + 1) ^ xor]) * (j + 1)
            # print(tmp)
            # rslt = max(rslt, tmp)
    ans.append(rslt)

    # a = LMII()
    # a.sort()
    # tmp = []
    # d = defaultdict(list)
    # for idx, i in enumerate(a):
    #     d[i ^ xor].append(i)
    #     d[(i - 1) ^ xor].append(i)
    #     # if not tmp or tmp[-1][-1] + 1 < i:
    #     #     tmp.append([i])
    #     # else:
    #     #     tmp[-1].append(i)
    # # print(d)
    # perf = []
    # for i in d.values():
    #     perf.append([0] + list(accumulate(i)))
    # rslt = 0
    # for i in perf:
    #     for j in range(1, len(i)):
    #         idx = bisect_right(i, m + i[j - 1])
    #         rslt = max(rslt, i[idx - 1] - i[j - 1])
    # ans.append(rslt)

    pass
for i in ans:
    print(i)
