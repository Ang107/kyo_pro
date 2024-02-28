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


s = list(input())
q = II()
d = {"A": 0, "B": 1, "C": 2}
ABC = ["A", "B", "C"]
for _ in range(q):
    t, k = MII()
    num_1 = 0
    num_2 = 0
    k -= 1
    k_n = k
    idx = k_n
    for i in range(t):
        # print(k_n)
        k_n //= 2
        idx = k_n
        if k_n == 0:
            idx = 0
            break

    # print(k)
    for i in range(t):
        if k == 0:
            num_1 += t - i
            break
        if k % 2 == 0:
            num_1 += 1
        else:
            num_2 += 1
        k //= 2

    # print(idx, num_1, num_2)
    print(ABC[(d[s[idx]] + num_1 + num_2 * 2) % 3])


# for i in range(10):
#     tmp = []
#     print(s)
#     for j in range(len(s)):
#         if s[j] == "A":
#             tmp.extend("BC")
#         elif s[j] == "B":
#             tmp.extend("CA")
#         elif s[j] == "C":
#             tmp.extend("AB")
#     s = tmp
