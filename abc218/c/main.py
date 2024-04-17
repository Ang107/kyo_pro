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


n = II()
s = [input() for _ in range(n)]
t = [input() for _ in range(n)]


# 90度右回転させたリストを返す
def list_rotate_R90(l):
    return list(zip(*l[::-1]))


t_x_min, t_y_min = inf, inf
t_sharp = []
for i in range(n):
    for j in range(n):
        if t[i][j] == "#":
            t_sharp.append((i, j))
            t_x_min = min(t_x_min, i)
            t_y_min = min(t_y_min, j)

for i in range(4):
    s_x_min, s_y_min = inf, inf
    s_sharp = []
    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                s_sharp.append((i, j))
                s_x_min = min(s_x_min, i)
                s_y_min = min(s_y_min, j)

    if len(s_sharp) != len(t_sharp):
        PN()
        exit()

    flag = True
    for i, j in zip(s_sharp, t_sharp):
        x1, y1 = i[0] - s_x_min, i[1] - s_y_min
        x2, y2 = j[0] - t_x_min, j[1] - t_y_min
        if x1 == x2 and y1 == y2:
            pass
        else:
            flag = False
            break

    if flag:
        PY()
        quit()

    s = list_rotate_R90(s)
PN()
