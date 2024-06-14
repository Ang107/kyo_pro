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

t = II()
ans = []


def isok(s, k):
    s0, s1 = set(), set()
    for i in range(len(s)):
        if i % (2 * k) < k:
            s0.add(s[i])
        else:
            s1.add(s[i])
    return len(s0) == 1 and len(s1) == 1 and s0.pop() != s1.pop()


for _ in range(t):
    n, k = MII()
    s = input()
    pass
    l = []
    r = []
    sp = [0]
    for i in range(1, n):
        if s[i] != s[i - 1]:
            sp.append(i)
    sp.append(n)
    # print(sp)
    sp_n = []
    for i in range(len(sp) - 1):
        if sp[i + 1] - sp[i] != k:
            sp_n.append((sp[i], sp[i + 1], sp[i + 1] - sp[i], s[sp[i]]))

    if len(sp_n) == 0:
        ans.append(n)
    else:
        if sp_n[0][2] > k:
            r1 = sp_n[0][1] - k
        else:
            r1 = sp_n[0][1]
        tmp1 = s[r1:] + s[:r1][::-1]

        # r2 = sp_n[0][0] + sp_n[0][2] % k
        # tmp2 = s[r2:] + s[:r2][::-1]

        # print(r1, tmp1)
        # print(r2, tmp2)
        if isok(tmp1, k):
            ans.append(r1)
        else:
            ans.append(-1)

    # else:

    # for idx, i in enumerate(s):
    #     if not l:
    #         if i == "0":
    #             l.append(0)
    #         elif i == "1":
    #             l.append(k)
    #     else:
    #         if i == "0":
    #             if i == s[idx - 1]:
    #                 if l[-1] < k - 1:
    #                     l.append(l[-1] + 1)
    #                 else:
    #                     l.append(0)
    #             else:
    #                 l.append(0)

    #         else:
    #             if i == s[idx - 1]:
    #                 if l[-1] < k * 2 - 1:
    #                     l.append(l[-1] + 1)
    #                 else:
    #                     l.append(k)
    #             else:
    #                 l.append(k)

    # for idx, i in zip(reversed(range(n)), s[::-1]):
    #     if not r:
    #         if i == "0":
    #             r.append(k - 1)
    #         elif i == "1":
    #             r.append(k * 2 - 1)
    #     else:
    #         if i == "0":
    #             if i == s[idx + 1]:
    #                 if r[-1] > 0:
    #                     r.append(r[-1] - 1)
    #                 else:
    #                     r.append(k - 1)
    #             else:
    #                 r.append(k - 1)

    #         else:
    #             if i == s[idx + 1]:
    #                 if r[-1] > 0:
    #                     r.append(r[-1] - 1)
    #                 else:
    #                     r.append(k * 2 - 1)
    #             else:
    #                 r.append(k * 2 - 1)
    # r = r[::-1]
    # print(l)
    # print(r)
    # if

for i in ans:
    print(i)
