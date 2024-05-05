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

T = II()
ans = []


for _ in range(T):
    n, k, pb, ps = MII()
    pb -= 1
    ps -= 1
    p = LMII()
    p = [i - 1 for i in p]
    a = LMII()
    # たどり着くまでのターン数, そこまでのスコア
    dp_b = [[10**18, -1] for _ in range(n)]
    dp_s = [[10**18, -1] for _ in range(n)]

    deq = deque()
    deq.append(pb)
    dp_b[pb] = [1, a[pb]]
    while deq:
        x = deq.pop()
        next = p[x]
        if dp_b[next] != [10**18, -1]:
            break

        dp_b[next] = [dp_b[x][0] + 1, dp_b[x][1] + a[next]]
        deq.append(next)

    deq = deque()
    deq.append(ps)
    dp_s[ps] = [1, a[ps]]
    while deq:
        x = deq.pop()
        next = p[x]
        if dp_s[next] != [10**18, -1]:
            break

        dp_s[next] = [dp_s[x][0] + 1, dp_s[x][1] + a[next]]
        deq.append(next)
    # print("b", dp_b)
    # print("s", dp_s)
    max_b = 0
    max_s = 0
    for (turn, score), s in zip(dp_b, a):
        if turn <= k:
            max_b = max(max_b, score + s * (k - turn))

    for (turn, score), s in zip(dp_s, a):
        if turn <= k:
            max_s = max(max_s, score + s * (k - turn))
    # print("score", max_b, max_s)
    if max_b == max_s:
        ans.append("Draw")
    elif max_b < max_s:
        ans.append("Sasha")
    elif max_b > max_s:
        ans.append("Bodya")

for i in ans:
    print(i)
