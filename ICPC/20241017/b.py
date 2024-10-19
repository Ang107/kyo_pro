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
import inspect

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
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


def solve(s: string, p: list[int]):
    def hash(p):
        l = []
        for i in s:
            if i == "[":
                pass
            elif i == "]":
                a, b = l.pop(), l.pop()

                op = l.pop()
                if op == "+":
                    l.append(a | b)
                elif op == "*":
                    l.append(a & b)
                else:
                    l.append(a ^ b)
            elif i in "abcd":
                l.append(p[ord(i) - ord("a")])
            else:
                l.append(i)
        return l[0]

    hashed_p = hash(p)
    cnt = 0
    for i in range(10000):
        j = f"{i:04}"
        # print(j)
        if hashed_p == hash(list(map(int, j))):
            cnt += 1
    ans.append((hashed_p, cnt))
    # ans.append(cnt)


ans = []

while 1:
    s = input()
    if s == ".":
        break
    p = list(map(int, input()))
    solve(s, p)
    pass


for i in ans:
    print(*i)
