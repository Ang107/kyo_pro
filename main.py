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


# h = II()
# max_num = 6 * h
# n以下の素数のリストを取得


# def get_Sosuu_3(n):
#     A = list(range(3, n, 6))
#     p = list()
#     print(len(A))
#     while A and A[0] ** 2 <= n:
#         tmp = A[0]
#         p.append(tmp)
#         A = [e for e in A if e % tmp != 0]
#     return p + A


# def get_Sosuu_5(n):
#     A = list(range(5, n, 6))
#     # print(A)
#     p = list()
#     print(len(A))

#     while A and A[0] ** 2 <= n:
#         tmp = A[0]
#         p.append(tmp)
#         A = [e for e in A if e % tmp != 0]
#     return p + A


# n以下の素数のリストを取得
# def get_Sosuu(n):
#     A = list(range(2, n + 1))
#     p = list()
#     while A[0] ** 2 <= n:
#         tmp = A[0]
#         p.append(tmp)
#         A = [e for e in A if e % tmp != 0]
#     return p + A


# def get_primes(n):
#     # n以下のすべての数について素数かどうかを記録する配列
#     is_prime = [True] * (n + 1)
#     is_prime[0] = False  # 0は素数ではない
#     is_prime[1] = False  # 1は素数ではない
#     primes = []

#     for i in range(2, n + 1):
#         if is_prime[i]:
#             primes.append(i)
#             # iの倍数を素数ではないとマーク
#             for j in range(i * 2, n + 1, i):
#                 is_prime[j] = False

#     return primes


# sosuu = get_primes(6 * 10**8)
# print(len(sosuu))
# umekomi = []
# for i in sosuu:
#     if i in range(3, 6 * (h - 1), 6) or i in range(5, 6 * (h - 1), 6):
#         umekomi.append(i)
# print(umekomi)
# if h < 3:
#     print(-1)
# else:
#     ans = 0
#     # for i in range(3, 6 * (h - 1), 6):
#     #     if i in sosuu:

#     #         ans = max(ans, i)
#     # for i in range(5, 6 * (h - 1), 6):
#     #     if i in sosuu:
#     #         ans = max(ans, i)

#     print(ans)
h = II()
if h < 3:
    print(-1)
    exit()
for i in range(6 * (h - 1) - 1, 4, -6):
    isSosuu = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isSosuu = False
            break
    if isSosuu:
        print(i)
        break
