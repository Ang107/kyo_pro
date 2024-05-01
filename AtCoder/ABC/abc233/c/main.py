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


n, x = MII()
A = []
for i in range(n):
    tmp = LMII()
    L = tmp[0]
    a = tmp[1:]
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    A.append(d)

ans = 0


def dfs():
    global ans
    deq = deque()
    # 残りの数、通り数、次見るAのidx
    deq.append((x, 1, 0))
    while deq:
        # print(deq)
        nokori, trs, idx = deq.popleft()
        for i, j in A[idx].items():
            if idx == n - 1:
                if nokori == i:
                    ans += trs * j
            else:
                if nokori % i == 0:
                    deq.append((nokori / i, trs * j, idx + 1))


dfs()
print(ans)
