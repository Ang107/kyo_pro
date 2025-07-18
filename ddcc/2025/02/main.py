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


# 各入力に対する処理
def main(s):
    ns = []
    for _ in range(len(s)):

        for i in s:
            # print(s)
            # print(ns)
            # print(i)
            ns.append(i)
            if len(ns) >= 2:
                if ns[-1] in ABC and ns[-1] == ns[-2]:
                    ns.pop()
                    ns.pop()
            if len(ns) >= 3:
                if ns[-1] in abc and ns[-1] == ns[-2] == ns[-3]:
                    ns.pop()
                    ns.pop()
                    ns.pop()
        s = ns
        s.append(s.pop(0))
        ns = []
        # print(s)

    return '"' + "".join(s) + '"'
    pass


if __name__ == "__main__":
    # 入力をここに追加
    Input = [
        "zzvvJJaOkuIPPIQQhodakSSjjjXXaFyyyujiKitvz",
        "AAKKAyyyuummmuFFTuvpppvvuuuIIpppRtAALUUeooonHLLHnnfffPPNNkknnnkjjjkAmeA",
        "zzDDfBBsGGkJrrrJpppZZhryyyrrISSInnntWWmXxxxjjjFFXrrDODDODNNrhhhaaWztttzzWTTaNgmNkkkDDNmAAmLLmeeeKlllOTSYoDDfPPkkkAPPAffjjjSSamvvnnnlHHllvz",
    ]

    Output = []
    for i in Input:
        Output.append(main(i))
    print(f"{Output[0]},{Output[1]},{Output[2]}")
