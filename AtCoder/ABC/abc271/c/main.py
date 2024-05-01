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
a = LMII()
kaburi = len(a) - len(set(a))
st = deque(sorted(set(a)))
ans = 0
while True:
    if st and st[0] == ans + 1:
        st.popleft()
        ans += 1
    else:
        if kaburi >= 2:
            kaburi -= 2
            tmp = 0
        elif kaburi == 1:
            kaburi -= 1
            tmp = 1
        else:
            tmp = 2
        if tmp > len(st):
            break
        for i in range(tmp):
            st.pop()
        ans += 1

print(ans)
# stock = SortedList(a)
# ans = 0
# readed = 0
# while len(stock) + readed > 1:
#     while stock and stock[0] <= ans:
#         stock.pop(0)
#         readed += 1
#     if stock and stock[0] == ans + 1:
#         stock.pop(0)
#         ans += 1
#         readed += 1
#     else:
#         if readed >= 2:
#             readed -= 2
#             tmp = 0
#         elif readed == 1:
#             readed = 0
#             tmp = 1
#         elif readed == 0:
#             tmp = 2
#         if len(stock) < tmp:
#             break
#         for i in range(tmp):
#             stock.pop()
#         ans += 1
#         readed += 1
#     print(readed, stock)
# print(ans)

# kaburi = len(a) - len(set(a))
# stock = SortedList(set(a))
# ans = 0
# while len(stock) + kaburi > 1:
#     if stock and stock[0] == ans + 1:
#         stock.pop(0)
#         ans += 1
#     else:
#         if kaburi >= 2:
#             kaburi -= 2
#             tmp = 0
#         elif kaburi == 1:
#             kaburi -= 1
#             tmp = 1
#         elif kaburi == 0:
#             kaburi = 0
#             tmp = 2
#         for i in range(tmp):
#             stock.pop()
#         ans += 1
#     # print(kaburi, stock)
# print(ans)
