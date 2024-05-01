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
from sortedcontainers import SortedSet, SortedList, SortedDict

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
s = input()
t = input()
ans = 0
a_stock = 0
b = 0
a = 0
tmp = 0
aa = 0
bb = 0
ba = 0

abba_num = 0
aa_num, bb_num = 0, 0

bb_idx = -1
aa_idx = inf
idx = 0
ab = SortedList()
ba = SortedList()
for i, j in zip(s, t):
    if i != j:
        if i == "A":
            ab.add(idx)
        elif i == "B":
            ba.add(idx)
    idx += 1

idx = 0
for i, j in zip(s, t):
    if i == j and i == "A":
        aa_idx = idx
        break
    idx += 1

idx = n - 1
for i, j in zip(s, t):
    if i == j and i == "A":
        bb_idx = idx
        break
    idx -= 1
ans = 0
# print(aa_idx, bb_idx)
# print(ab, ba)
ab_new = deque()
while ba:
    i = ba[0]
    ba.remove(ba[0])
    if len(ab) > 0:
        idx = bisect_left(ab, i)
        if idx < len(ab):
            idx = ab[idx]
            ab.remove(ab[idx])
            ans += 1
            bb_idx = max(bb_idx, idx)
            aa_idx = min(aa_idx, i)
            continue

        # while ab and i > ab[0]:
        #     tmp = ab.popleft()
        #     ab_new.append(tmp)
        # if len(ab) > 0:
        #     idx = ab.popleft()
        #     bb_idx = max(bb_idx, idx)
        #     aa_idx = min(aa_idx, i)
        #     ans += 1
        #     continue
    if i < bb_idx:
        aa_idx = min(aa_idx, i)
        ans += 1
    else:
        print(-1)
        exit()


for i in ab:
    if aa_idx < i:
        ans += 1
    else:
        print(-1)
        exit()
print(ans)


# idx = 0
# ba = 0
# for i, j in zip(s, t):
#     if i != j:
#         if i == "B" and idx < bb_idx:
#             ba += 1
#             ans += 1
#         elif i == "A":
#             if ba > 0:
#                 ba -= 1
#             elif aa_idx < idx:
#                 ans += 1
# for i, j in zip(s, t):
#     if i == j:
#         if i == "A":
#             aa += 1
#         elif i == "B":
#             bb += 1

#     if i != j:
#         if i == "A":
#             if ba > 0:
#                 ba -= 1
#                 abba_num += 1
#             elif aa > 0:
#                 aa -= 1
#                 aa_num += 1
#             else:
#                 print(-1)
#                 exit()
#         if i == "B":
#             ba += 1
# aa = 0
# bb = 0
# ba = 0
# ab = 0
# for i, j in zip(s[::-1], t[::-1]):
#     if i == j:
#         if i == "A":
#             aa += 1
#         elif i == "B":
#             bb += 1

#     if i != j:
#         if i == "B":
#             if ab > 0:
#                 ab -= 1
#                 abba_num += 1
#             elif bb > 0:
#                 aa -= 1
#                 aa_num += 1
#             else:
#                 print(-1)
#                 exit()
#         if i == "A":
#             ab += 1

# if b > 0:
#     print(-1)
# else:
#     print(ans)
