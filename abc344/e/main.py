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
a = LMII()
q = II()
renketu = defaultdict(lambda: [None, None])
renketu["head"][1] = a[0]
renketu[a[0]][0] = "head"
renketu["tail"][0] = a[-1]
renketu[a[-1]][1] = "tail"

for i in range(n):
    if i != 0:
        renketu[a[i]][0] = a[i - 1]
    if i != n - 1:
        renketu[a[i]][1] = a[i + 1]

for i in range(q):
    tmp = LMII()
    # print(renketu)
    if len(tmp) == 3:
        x, y = tmp[1:]
        if renketu[x][1] != None:
            renketu[y][1] = renketu[x][1]
            renketu[renketu[x][1]][0] = y
            renketu[y][0] = x
            renketu[x][1] = y
        else:
            renketu[x][1] = y
            renketu[y][0] = x

    else:
        x = tmp[1]
        # if renketu[x][0]:
        renketu[renketu[x][0]][1] = renketu[x][1]
        # if renketu[x][1]:
        renketu[renketu[x][1]][0] = renketu[x][0]
        # renketu[x] = [None, None]
        del renketu[x]

# if len(renketu) > 1:
#     for k, (i, j) in renketu.items():
#         if i == None and j != None:
#             s = k
#             break
# else:
#     # print(renketu)
#     s, _ = renketu.popitem()

ans = ["head"]
while True:
    if renketu[ans[-1]][1] != None:
        ans.append(renketu[ans[-1]][1])
    else:
        break
print(*ans[1:-1])
