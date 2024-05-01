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


n = II()
A = [LMII() for _ in range(2 * n - 1)]

ans = 0
deq = deque()
# そこまでの排他的論理和、使用済みの是非、使用済みの人の数
deq.append((0, [False] * (2 * n), 0))

while deq:
    num, used, len_used = deq.popleft()
    if len_used == 2 * n:
        ans = max(ans, num)
        continue
    for i in range(2 * n):
        if not used[i]:
            min_used = i
            break

    for i in range(2 * n):
        if not used[i] and i != min_used:
            used_n = used[:]
            used_n[min_used] = True
            used_n[i] = True
            deq.append((num ^ A[min_used][i - min_used - 1], used_n, len_used + 2))

print(ans)
