from sys import stdin, setrecursionlimit
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
ans = []
while True:
    lines = int(input())
    if lines == 0:
        break
    level = []
    operator_stack = []

    for line in range(lines):
        x = SI()
        if x[-1] == "*" or x[-1] == "+":
            level.append((len(x), x[-1]))
        else:
            level.append((len(x) - 1, int(x[-1])))
    # print(level)
    for lv, num in level:

        while (operator_stack and operator_stack[-1][0] > lv) or (
            operator_stack
            and operator_stack[-1][0] == lv
            and (num == "*" or num == "+")
        ):
            # print(operator_stack)
            current_lv = operator_stack[-1][0]
            tmp = []
            while operator_stack and operator_stack[-1][0] == current_lv:
                tmp.append(operator_stack.pop())
            # print(f"{tmp=}")
            if tmp[-1][1] == "*":
                caluculated = 1
                for _, n in tmp[:-1]:
                    caluculated *= n
                current_lv -= 1
                operator_stack.append((current_lv, caluculated))

            else:
                caluculated = 0
                for _, n in tmp[:-1]:
                    caluculated += n
                current_lv -= 1
                operator_stack.append((current_lv, caluculated))

        operator_stack.append((lv, num))

    while len(operator_stack) > 1:
        current_lv = operator_stack[-1][0]
        tmp = []
        while operator_stack and operator_stack[-1][0] == current_lv:
            tmp.append(operator_stack.pop())

        if tmp[-1][1] == "*":
            caluculated = 1
            for _, n in tmp[:-1]:
                caluculated *= n
            current_lv -= 1
            operator_stack.append((current_lv, caluculated))

        else:
            caluculated = 0
            for _, n in tmp[:-1]:
                caluculated += n
            current_lv -= 1
            operator_stack.append((current_lv, caluculated))
    ans.append(operator_stack[0][1])

for i in ans:
    print(i)
