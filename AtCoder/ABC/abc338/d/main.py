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


# 入力
n, m = MII()
x = LMII()

# 0-indexに変換
x = [i - 1 for i in x]

tmp = [0] * (n)

for i in range(1, m):
    # 移動前後の島
    a, b = x[i], x[i - 1]

    # 順番を昇順に統一
    a, b = min(a, b), max(a, b)

    # 時計回り、反時計回りで移動したときの移動距離
    p, q = b - a, n - b + a

    # 時計回り、反時計回りの移動距離の差
    num = abs(p - q)

    # 時計周りで移動した方が距離が短い場合
    if p < q:
        # a ~ b に含まれる区間を切断した時、反時計周りで移動することになり、移動距離がnum増加する
        # indexをa ~ b全て更新するとTLEするため、区間の端の差分のみを保存
        tmp[a] += num
        tmp[b] -= num

    # 反時計周りで移動した方が距離が短い場合
    elif p > q:
        # b ~ n,0 ~ a に含まれる区間を切断した時、時計周りで移動することになり、移動距離がnum増加する
        tmp[0] += num
        tmp[a] -= num
        tmp[b] += num

# 累積和(各区間を切ることにより生じる、移動距離の増加分)
prf = list(accumulate(tmp))

# 切断前の最短の移動距離を計算
dis = 0
for i in range(1, m):
    a, b = x[i], x[i - 1]
    a, b = min(a, b), max(a, b)
    p, q = b - a, n - b + a
    dis += min(p, q)

# 切断前の最短の移動距離と、最適に切断したときに生じる移動距離の増加分の和を出力
print(dis + min(prf))
