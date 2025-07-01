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


# https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a#%E3%83%9D%E3%83%A9%E3%83%BC%E3%83%89%E3%83%AD%E3%83%BC%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3%E6%B3%95%E3%81%AE%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0
def gcd(a, b):
    while a:
        a, b = b % a, a
    return b


def is_prime(n):
    if n == 2:
        return 1
    if n == 1 or n % 2 == 0:
        return 0

    m = n - 1
    lsb = m & -m
    s = lsb.bit_length() - 1
    d = m // lsb

    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in test_numbers:
        if a == n:
            continue
        x = pow(a, d, n)
        r = 0
        if x == 1:
            continue
        while x != m:
            x = pow(x, 2, n)
            r += 1
            if x == 1 or r == s:
                return 0
    return 1


def find_prime_factor(n):
    if n % 2 == 0:
        return 2

    m = int(n**0.125) + 1

    for c in range(1, n):
        f = lambda a: (pow(a, 2, n) + c) % n
        y = 0
        g = q = r = 1
        k = 0
        while g == 1:
            x = y
            while k < 3 * r // 4:
                y = f(y)
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            k = r
            r *= 2
        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = gcd(abs(x - y), n)
        if g == n:
            continue
        if is_prime(g):
            return g
        elif is_prime(n // g):
            return n // g
        else:
            return find_prime_factor(g)


def factorize(n):
    res = {}
    while not is_prime(n) and n > 1:  # nが合成数である間nの素因数の探索を繰り返す
        p = find_prime_factor(n)
        s = 0
        while n % p == 0:  # nが素因数pで割れる間割り続け、出力に追加
            n //= p
            s += 1
        res[p] = s
    if n > 1:  # n>1であればnは素数なので出力に追加
        res[n] = 1
    return res


def is_prime(n):
    if n == 2:  # 2であれば素数なので終了
        return 1
    if n == 1 or n % 2 == 0:  # 1もしくは2より大きい偶数であれば素数でないので終了
        return 0

    m = n - 1
    lsb = m & -m  # LSB. m-1をビット列で表した時立っているビットのうち最も小さいもの
    s = (
        lsb.bit_length() - 1
    )  # 上述のs. LSB以上のビットの部分をdとし、2^s = LSBとすると上述のp-1 = 2^sdを満たす
    d = m // lsb

    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in test_numbers:
        if a == n:  # a = n -> 任意の自然数kについてa^k ≡ 0(mod n)なので無視
            continue
        x = pow(a, d, n)  # x ≡ a^d(mod n)で初期化
        r = 0
        if x == 1:  # a^d ≡ 1(mod n)なので無視
            continue
        while x != m:  # r = 0からsまで順にx ≡ a^(2^rd) ≡ -1(mod n)を検証
            x = pow(x, 2, n)
            r += 1
            if (
                x == 1 or r == s
            ):  # x ≡ 1(mod n) -> x^2 ≡ 1(mod n)で-1になり得ないので合成数
                return 0
    return 1  # すべてのテストを通過したら素数であるとして終了


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


l, r = MII()
primes = get_primes(10**7)

s = [False] * (r - l + 1)
for p in primes:
    tmp = p
    while True:
        tmp *= p
        if l <= tmp <= r:
            s[tmp - l] = True
        if r < tmp:
            break

ans = 1
# print(s)
for i in range(l + 1, r + 1):
    # f = factorize(i)
    # if len(f) == 1:
    #     ans += 1
    if is_prime(i) or s[i - l]:
        # print(i)
        ans += 1
print(ans)
