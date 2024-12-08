from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
ans = 0


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


primes = get_primes(int(n**0.5) + 1)
# print(primes)
for i in primes:
    if i**8 <= n:
        ans += 1
primes_ = [i**2 for i in primes]
for index, i in enumerate(primes_):
    for j in range(index + 1, len(primes_)):
        if i * primes_[j] <= n:
            ans += 1
        else:
            break

print(ans)
