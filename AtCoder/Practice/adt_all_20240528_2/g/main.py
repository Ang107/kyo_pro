import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
def get_primes(n):
    # n以下のすべての数について素数かどうかを記録する配列
    is_prime = [True] * (n + 1)
    is_prime[0] = False  # 0は素数ではない
    is_prime[1] = False  # 1は素数ではない
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            # iの倍数を素数ではないとマーク
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    return primes
n = II()
# print(int(n ** 0.2) + 10)
sosuu = get_primes(int(n ** 0.5) + 15)
sosuu_set = set(sosuu)
# print(sosuu)
ans = 0
# print(len(sosuu))
for i in range(len(sosuu)):
    for j in range(i+1,len(sosuu)):
        tmp =  sosuu[i] ** 2 * sosuu[j]
        if bisect_right(sosuu,int((n // tmp) ** 0.5)) - j <= 0:
            break
        ans += bisect_right(sosuu,int((n // tmp) ** 0.5)) - j - 1
    #     for k in range(j+1,len(sosuu)):
    #         # print(i ** 2 * j * k ** 2)
    #         if i in sosuu and j in sosuu and k in sosuu and 1 <= i ** 2 * j * k ** 2 <= n:
    #             ans += 1
    #         if i ** 2 * j * k ** 2 > n:
    #             break
    #     if i ** 2 * j * k ** 2 > n:
    #             break
    # if i ** 2 * j * k ** 2 > n:
    #             break
pritn(ans)
                
    