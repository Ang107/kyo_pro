import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
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
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


c = []
for i in range(3):
    c.extend(LMII())

temp = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],]

tyn = [None for _ in range(8)]
tyn[0], tyn[1], tyn[2] = c[0:3], c[3:6], c[6:9]
tyn[3], tyn[4], tyn[5] = [c[i] for i in range(9) if i % 3 == 0], [
    c[i] for i in range(9) if i % 3 == 1], [c[i] for i in range(9) if i % 3 == 2]
tyn[6] = [c[0], c[4], c[8]]
tyn[7] = [c[2], c[4], c[6]]

out = []
out_list = []
for i, j in enumerate(tyn):
    if len(set(j)) == 2:
        p, q, r = temp[i]
        out_list.extend((p, q, r))
        if c[p] == c[q]:
            out.append((p, q, r))
        elif c[p] == c[r]:
            out.append((p, r, q))
        elif c[q] == c[r]:
            out.append((q, r, p))

# print(tyn)
# print(out)
# print(out_list)


def judge(x):
    d = {}
    for i in out_list:
        d[i] = x.index(i)
    for i, j, k in out:
        if d[i] < d[k] and d[j] < d[k]:
            return False
    return True


# def judge(x):
#     temp = [-1] * 9
#     for j in x:
#         temp[j] = c[j]
#         for p in range(8):
#             open_num = set()
#             for q in range(3):
#                 # print(temp[tyn[p][q]])
#                 if temp[tyn[p][q]] != -1:
#                     if temp[tyn[p][q]] not in open_num:
#                         open_num.add(temp[tyn[p][q]])
#                     else:
#                         return False
#     return True
ans = 0
for i in permutations(range(9)):
    if judge(i):
        ans += 1

print(ans/(9*8*7*6*5*4*3*2))
