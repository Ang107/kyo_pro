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


def to_num(l):
    min_x, min_y = inf, inf
    result = []
    for i in range(4):
        for j in range(4):
            if l[i][j] == "#":
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                result.append((i, j))
    result = [(i - min_x, j - min_y) for i, j in result]
    return result


a = [input() for _ in range(4)]
b = [input() for _ in range(4)]
c = [input() for _ in range(4)]

if len(to_num(a)) + len(to_num(b)) + len(to_num(c)) != 16:
    PN()
    exit()


# 90度右回転させたリストを返す
def list_rotate_R90(l):
    return list(zip(*l[::-1]))


a_kaiten, b_kaiten, c_kaiten = [], [], []
for i in range(4):
    a_kaiten.append(to_num(a))
    b_kaiten.append(to_num(b))
    c_kaiten.append(to_num(c))
    a = list_rotate_R90(a)
    b = list_rotate_R90(b)
    c = list_rotate_R90(c)


def get_xy(l, p):
    for i in range(4):
        for j in range(4):
            flag = True
            for x, y in p:
                if i + x in range(4) and j + y in range(4) and l[i + x][j + y] == ".":
                    pass
                else:
                    flag = False
            if flag:
                return i, j
    return -1, -1


# print(a_kaiten, b_kaiten, c_kaiten)

for i in product(a_kaiten, b_kaiten, c_kaiten):
    for j in permutations(i):
        flag = True
        b = [["."] * 4 for _ in range(4)]
        for k in j:
            x, y = get_xy(b, k)
            if x == -1:
                flag = False
                break
            for l in k:
                b[x + l[0]][y + l[1]] = "#"

        if flag:
            PY()
            exit()

PN()
