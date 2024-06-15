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

def solve(s):
    cnt = set()
    cnt.add(s)
    for i in range(1, len(s)):
        l,r = s[:i], s[i:]
        cnt.add(l + r)
        cnt.add(l[::-1] + r)
        cnt.add(l + r[::-1])
        cnt.add(l[::-1] + r[::-1])
        
        cnt.add(r + l)
        cnt.add(r[::-1] + l)
        cnt.add(r + l[::-1])
        cnt.add(r[::-1] + l[::-1])
    return len(cnt)
    pass

ans = []
t = II()

for _ in range(t):
    s = input()
    ans.append(solve(s))
    pass
    
for i in ans:
    print(i)