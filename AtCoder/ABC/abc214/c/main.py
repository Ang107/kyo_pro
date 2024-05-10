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
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
s = LMII()
t = LMII()
ans = [10**18] * n
# 円上なので二週分考える(Nが1に渡す等の場合を考慮)
for i in range(10 * n):
    if i == 0:
        # 左端は左がいないので、ans[(i - 1) % n] + s[(i - 1) % n]を省略
        ans[i % n] = min(ans[i % n], t[i % n])
    else:
        # ans[i % n]: 元の答え
        # t[i % n]: 高橋君に渡される時間
        # ans[(i - 1) % n] + s[(i - 1) % n]:
        # 左の人が宝石を受け取る最小値+左の人が持っている時間 = 左の人に渡される時間
        ans[i % n] = min(ans[i % n], t[i % n], ans[(i - 1) % n] + s[(i - 1) % n])

for i in ans:
    print(i)
