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


def solve(a: str, b: str):
    na = []
    nb = []
    for i in a:
        tmp = []
        if i == "]":
            while na and na[-1] in "0123456789":
                tmp.append(na.pop())
            tmp = "".join(tmp[::-1])
            na.append(int(tmp))
        na.append(i)
    a = na
    for i in b:
        tmp = []
        if i == "]":
            while nb and nb[-1] in "0123456789":
                tmp.append(nb.pop())
            tmp = "".join(tmp[::-1])
            nb.append(int(tmp))
        nb.append(i)
    b = nb
    # print(a)

    def decode(s):
        res = {}

        def f(s, parent_node):
            # print(s, parent_node)
            if len(s) == 7:
                return s[3]
            cnt = 0
            for i in range(len(s)):
                if s[i] == "(":
                    cnt += 1
                elif s[i] == ")":
                    cnt -= 1
                if cnt == 0:
                    res[parent_node * 2] = f(s[1:i], parent_node * 2)
                    res[parent_node * 2 + 1] = f(s[i + 5 : -1], parent_node * 2 + 1)
                    return s[i + 2]

        res[1] = f(s, 1)
        return res

    a_decode = decode(a)
    b_decode = decode(b)
    ab_decode = {}
    for i in a_decode:
        if i in b_decode and a_decode[i] != None and b_decode[i] != None:
            ab_decode[i] = int(a_decode[i]) + int(b_decode[i])
    # print(a_decode)
    # print(b_decode)
    # print(ab_decode)

    def encode(s):
        def f(node):
            if node not in s:
                return ""
            return f"({f(node*2)})[{s[node]}]({f(node*2+1)})"

        return f(1)

    # print(ab_decode)
    return encode(ab_decode)


ans = []

# while 1:
a = input()
b = input()
ans.append(solve(a, b))
pass


for i in ans:
    print(i)
