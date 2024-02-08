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


s = input()
deq = deque()
# while s:
#     i = deq.popleft()
#     if i == "^":
#         tmp = deq.pop()
#         tmp *= deq.pop()
#         deq.append(tmp)

#     elif i == "*":
#         tmp = deq.pop()
#         tmp += deq.pop()
#         deq.append(tmp)

#     elif i == "(":

#     elif i == ")":


def solve(s):
    bunkatu = []
    tmp = []
    num = 0
    print("in", s)
    if len(s) == 1:
        if s == "x":
            # print("out",1)
            return 1
        else:
            # print("out", 0)
            return 0

    if s[0] == "(" and s[-1] == ")":
        return solve(s[1:-1])

    if len(s) == 3:
        a, b, c = s
        if b == "*":
            return solve(a) + solve(c)
        elif b == "^":
            return solve(a) * c
    if len(s) == 5:
        a, b, c, d, e = s

        if a == "(" and c == ")" and d == "^":
            # print(solve(b) * e)
            # print(solve(b))
            return solve(b) * e

    # print(s)
    idx = len(s)
    for i in s[::-1]:
        idx -= 1
        # print(i)
        if i == ")":
            num += 1
            tmp.append(i)
        elif i == "(":
            num -= 1
            tmp.append(i)
        elif i == "^":
            if num == 0:
                # print(tmp), s[idx + 1 :]
                # print("".join(tmp)), s[idx + 1 :]
                # print(solve(s[:idx]), "*", solve(s[idx + 1 :]))
                return int(solve(s[:idx])) * int(s[idx + 1 :])
            else:
                tmp.append(i)
        elif i == "*":
            if num == 0:
                # print("".join(tmp)), s[idx + 1 :]
                # print(solve(s[:idx]), "+", solve(s[idx + 1 :]))

                return int(solve(s[:idx])) + int(solve(s[idx + 1 :]))
            else:
                tmp.append(i)
        elif i == "x":
            tmp.append(i)
        else:
            tmp.append(i)


print(solve(s))
