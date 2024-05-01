import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照

n = II()
h = LMII()

#dpテーブル初期化
dp = [inf] * n
dp[0] = 0
#一個前の地点を保存
pre = [None] * n

#dpテーブル埋め
for i in range(1,n):
    if dp[i] > dp[i-1] + abs(h[i] - h[i-1]):
        dp[i] = dp[i-1] + abs(h[i] - h[i-1])
        pre[i] = i-1
    if i > 1:
        if dp[i] > dp[i-2] + abs(h[i] - h[i-2]):
            dp[i] = dp[i-2] + abs(h[i] - h[i-2])
            pre[i] = i-2

ans = [n]
#経路復元
while ans[-1] != 1:
    ans.append(pre[ans[-1]-1]+1)
ans = ans[::-1]

print(len(ans))
print(*ans)