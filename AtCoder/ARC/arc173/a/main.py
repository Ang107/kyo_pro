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


# n進数->10進数
def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


# 10進数->n進数
def base_n(num_10, n):
    if num_10 == 0:
        return 0
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])


t = II()
# n桁目までのneqnumberの数
neq_num = [0] * 16
for i in range(1, 15):
    neq_num[i] = 9**i


def solve(n):
    nokori = n
    for i in range(16):
        if 1 < nokori <= neq_num[i]:
            keta = i
            break
        else:
            nokori -= neq_num[1]
    ans = ""
    for i in range(keta - 1, 0, -1):
        tmp = nokori // 9**i
        if ans and ans[-1] == str(tmp):
            ans += str(tmp + 1)
        else:
            ans += str(tmp)
        nokori -= tmp * 9**i
    return ans


for i in range(t):
    c = II()
    print(solve(c))


# # 飛ばされる回数を計算
# skip = []
# for i in range(13):
#     if i <= 1:
#         skip.append(0)
#     else:
#         skip.append((i - 1) * 9 * 10 ** (i - 2))

# t = II()
# for i in range(t):
#     c = II()
#     len_c = len(str(c))
#     # 一つ小さい桁までの飛ばされる数
#     tmp1 = sum(skip[: len_c - 1])

#     tmp2 = int(str(c)[0]) * 10**len_c
