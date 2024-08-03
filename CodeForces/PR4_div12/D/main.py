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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

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


t = II()
ans = []


def get_primes(n):
    if n <= 1:
        return 0
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


print(2**18)
primes = get_primes(2 * 10**5)
print(len(primes))
# 辺を貼る
# ed = [[] for _ in range(2*10**5 + 1)]
# for i in primes:
#     all_1 = (1 << 18) - 1
#     all_1 ^= i
#     all_0 = 0
#     tmp = 0
#     for j in range(18):
#         if i >> j:

# for _ in range(t):
#     n = II()
#     np = []
#     for i in primes:
#         if i <= n:
#             np.append(i)
#         else:
#             break


#     pass
# for i in ans:
#     print(i)
