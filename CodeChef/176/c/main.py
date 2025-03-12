from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
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
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

t = II()
anss = []
for _ in range(t):
    n = II()
    a = list(map(int, input()))
    b = list(map(int, input()))
    # cnt_a = [0, 0]
    # cnt_b = [0, 0]
    # can_swap = -1
    # index = 0
    # for i, j in zip(a, b):
    #     cnt_a[int(i)] += 1
    #     cnt_b[int(j)] += 1
    #     if i != j:
    #         can_swap = index
    #     index += 1
    # ans = "Yes"
    # # print(a)
    # # print(cnt_a[0] == cnt_a[1] and cnt_b[0] == cnt_b[1] and cnt_a[0] != cnt_b[0],)
    # # print(
    # #     a,
    # #     b,
    # #     cnt_a[0] % 2 == cnt_a[1] % 2
    # #     and cnt_b[0] % 2 == cnt_b[1] % 2
    # #     and cnt_a[0] % 2 != cnt_b[0] % 2,
    # #     can_swap == -1
    # #     and (
    # #         (cnt_a[0] % 2 == cnt_a[1] % 2 == 1) and (cnt_b[0] % 2 == cnt_b[1] % 2 == 1)
    # #     ),
    # # )
    # # print(cnt_a, cnt_b)
    # if (
    #     cnt_a[0] % 2 == cnt_a[1] % 2
    #     and cnt_b[0] % 2 == cnt_b[1] % 2
    #     and cnt_a[0] % 2 != cnt_b[0] % 2
    # ):
    #     ans = "No"
    #     anss.append(ans)
    #     continue
    # if can_swap == -1 and (
    #     (cnt_a[0] % 2 == cnt_a[1] % 2 == 1) and (cnt_b[0] % 2 == cnt_b[1] % 2 == 1)
    # ):
    #     ans = "No"
    #     anss.append(ans)
    #     continue
    # elif can_swap != -1 and (
    #     (cnt_a[0] % 2 == cnt_a[1] % 2 == 1) and (cnt_b[0] % 2 == cnt_b[1] % 2 == 1)
    # ):
    #     a[can_swap], b[can_swap] = b[can_swap], a[can_swap]
    # # print(a, b)
    # # if all(i == j for i, j in zip(a, b)) or all(i != j for i, j in zip(a, b)):
    # #     pass
    # # else:
    # #     ans = "No"

    # # cnt_a = [0, 0]
    # # cnt_b = [0, 0]
    # # for i, j in zip(a, b):
    # #     cnt_a[int(i)] += 1
    # #     cnt_b[int(j)] += 1
    # # a_index = [deque(), deque()]
    # # b_index = [deque(), deque()]
    # # for i in range(n):
    # #     a_index[a[i]].append(i)
    # #     b_index[b[i]].append(i)
    # # print(a, b)
    # # print(a, cnt_a, a_index)
    # # if cnt_a[0] % 2 == 0:
    # #     # goal = [[], []]
    # #     g = [-1] * n
    # #     for i in range(cnt_a[0] // 2):
    # #         # goal[0].append(i)
    # #         # goal[0].append(n - i - 1)
    # #         g[i] = 0
    # #         g[n - i - 1] = 0
    # #     for j in range(n):
    # #         # goal[1].append(j)
    # #         if g[j] == -1:
    # #             g[j] = 1
    # #     # goal[0].sort()
    # # else:
    # #     # goal = [[], []]
    # #     g = [-1] * n
    # #     for i in range(cnt_a[1] // 2):
    # #         # goal[0].append(i)
    # #         # goal[0].append(n - i - 1)
    # #         g[i] = 1
    # #         g[n - i - 1] = 1
    # #     for j in range(n):
    # #         # goal[1].append(j)
    # #         if g[j] == -1:
    # #             g[j] = 0
    # #     # goal[0].sort()
    # # # print(a, cnt_a, g)
    # # # print(goal)
    # # # print(a_index)
    # # print(g, a_index)
    # # for index, (i, j) in enumerate(zip(a, g)):
    # #     if i == j:
    # #         a_index[i].popleft()
    # #         continue
    # #     if j == 0:
    # #         tmp = a_index[0].popleft()
    # #         a_index[1].appendleft(tmp)
    # #         a[index], a[tmp] = a[tmp], a[index]
    # #         b[index], b[tmp] = b[tmp], b[index]
    # #     else:
    # #         tmp = a_index[1].popleft()
    # #         a_index[0].appendleft(tmp)
    # #         a[index], a[tmp] = a[tmp], a[index]
    # #         b[index], b[tmp] = b[tmp], b[index]
    # # print(a)
    # # print(b)
    # ab = [(i, j) for i, j in zip(a, b)]
    # ab.sort()
    # na = []
    # nb = []
    # for i, j in ab:
    #     na.append(i)
    #     nb.append(j)
    # if nb != sorted(nb):
    #     ans = "No"
    # anss.append(ans)
for i in anss:
    print(i)
