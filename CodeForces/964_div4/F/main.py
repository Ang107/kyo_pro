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
mod = 10**9 + 7
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
kaizyou = [1]
inv = [1]
for i in range(1, 2 * 10**5 + 1):
    kaizyou.append(kaizyou[-1] * i % mod)
    inv.append(pow(kaizyou[-1], -1, mod))


def comb(a, b):
    if a < b:
        return 0
    return kaizyou[a] * inv[b] * inv[a - b] % mod


for _ in range(t):
    n, k = MII()
    a = LMII()
    rslt = 0
    mod = 10**9 + 7
    # for i in range(k//2,n-k//2):
    #     rslt +=
    cnt = [0, 0]
    for i in a:
        cnt[i] += 1
    for i in range(k // 2 + 1):
        rslt += comb(cnt[1], k - i) * comb(cnt[0], i) % mod
        rslt %= mod
    ans.append(rslt)
    pass
for i in ans:
    print(i)
