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
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

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
XY = [LMII() for _ in range(n)]
ittyokusen = []

max_ans = n // 3
hizyuu = [[0, i] for i in range(n)]
for i in range(n):
    x1, y1 = XY[i]
    for j in range(i + 1, n):
        x2, y2 = XY[j]
        tmp = {i, j}
        for k in range(j + 1, n):
            x3, y3 = XY[k]
            if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0:
                tmp.add(k)
        if len(tmp) > 2:
            ittyokusen.append(tmp)
            for k in tmp:
                hizyuu[k][0] -= 1


def is_ittyokusen(a, b, c):
    x1, y1 = XY[a]
    x2, y2 = XY[b]
    x3, y3 = XY[c]
    if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0:
        return True
    else:
        return False


ans = 0
heapify(hizyuu)
# print(hizyuu)
while len(hizyuu) >= 3:
    c1, v1 = heappop(hizyuu)
    c2, v2 = heappop(hizyuu)
    tmp = []
    while hizyuu:
        i, j = heappop(hizyuu)
        if not is_ittyokusen(v1, v2, j):
            ans += 1
            for k in tmp:
                heappush(hizyuu, k)
            break
        else:
            tmp.append([i, j])


print(ans)

# use = set(range(n))
# used = set()

# for i in ittyokusen:
#     for j in i:
#         if i not in used:


# print(ittyokusen)
