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
tmp = []
for i in range(n):
    a, b = MII()
    tmp.append([a, 1])
    tmp.append([a + b, -1])
tmp.sort()
tmp_n = []
for i in tmp:
    if not tmp_n:
        tmp_n.append(i)
    else:
        if tmp_n[-1][0] == i[0]:
            tmp_n[-1][1] += i[1]
        else:
            tmp_n.append(i)

ans = [0] * n
num = 0
for i in range(len(tmp_n) - 1):
    num += tmp_n[i][1]
    if num != 0:
        ans[num - 1] += tmp_n[i + 1][0] - tmp_n[i][0]

print(*ans)

# dd = defaultdict(int)
# for i in range(n):
#     a, b = MII()
#     dd[a] += 1
#     dd[a + b] -= 1

# dd_sorted = sorted(dd.items(), key=lambda x: x[0])
# # print(dd_sorted)
# dd_acc = []
# for idx, (i, j) in enumerate(dd_sorted):
#     if idx == 0:
#         dd_acc.append([i, j])
#     else:
#         tmp = dd_acc[-1][:]
#         tmp[0] = i
#         tmp[1] += j
#         dd_acc.append(tmp)
# # print(dd_acc)

# ans = [0] * n
# for i in range(len(dd_acc) - 1):
#     day, num = dd_acc[i]
#     if num - 1 in range(n):
#         ans[num - 1] += dd_acc[i + 1][0] - day

# print(*ans)
