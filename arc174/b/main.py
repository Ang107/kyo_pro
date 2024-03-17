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


# def dlist(*l, fill=0):
#     if len(l) == 1:
#         return [fill] * l[0]
#     ll = l[1:]
#     return [dlist(*ll, fill=fill) for _ in range(l[0])]


# def isOK_bunbo(mid,a_score,a_sum):
#     if (a_score + mid * 5) / (a_sum + mid) >= 3:
#         return True
#     else:
#         return False


# def megur_bunbo(ng, ok,a_score,a_sum):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if isOK_bunbo(mid,a_score,a_sum):
#             ok = mid
#         else:
#             ng = mid
#     return ok

# def isOK_bunsi(mid,a_score,a_sum,bunbo):
#     if (a_score + mid) / (a_sum + bunbo) >= 3:
#         return True
#     else:
#         return False


# def megur_bunsi(ng, ok,a_score,a_sum,bunbo):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if isOK_bunbo(mid,a_score,a_sum,bunbo):
#             ok = mid
#         else:
#             ng = mid
#     return ok


# t = II()
# for _ in range(t):
#     a = LMII()
#     p = LMII()
#     a_score = sum([(i+1)*j for i,j in enumerate(a)])
#     # 既にされたレビューの回数
#     a_sum = sum(a)
#     if a_score / a_sum >= 3:
#         print(0)
#         continue

#     bunbo = megur_bunbo(-1,10**18,a_score,a_sum)
#     bunsi = megur_bunsi(-1, 10**18, a_score, a_sum,bunbo)
#     rslt = 0
#     if bunbo > 60:
#         tmp = bunbo - 60
#         rslt = min()


# # コスパ
# p_cosp = [j/(i+1) for i,j in enumerate(p)]

# # dp
# # 星3にするための

t = II()
ans = []
# import pulp


# def findMinimumCost(costA, costB, N):
#     # 問題のインスタンスを作成
#     prob = pulp.LpProblem("MinimumCost", pulp.LpMinimize)

#     # 変数を定義（0から無限大、整数）
#     x = pulp.LpVariable("x", lowBound=0, cat="Integer")
#     y = pulp.LpVariable("y", lowBound=0, cat="Integer")

#     # 目的関数を追加
#     prob += costA * x + costB * y

#     # 制約条件を追加
#     prob += x + 2 * y >= N

#     # 問題を解く
#     prob.solve(pulp.PULP_CBC_CMD(msg=False))

#     # 解が見つかったかどうかをチェック
#     if pulp.LpStatus[prob.status] == "Optimal":
#         return pulp.value(prob.objective)
#     else:
#         return "No solution found", None, None


for _ in range(t):
    a = LMII()
    p = LMII()
    a_score = sum([(i + 1) * j for i, j in enumerate(a)])
    # 既にされたレビューの回数
    a_sum = sum(a)
    if a_score / a_sum >= 3:
        ans.append(0)
        continue
    score = 0
    # ans.append(min())
    for i in range(5):
        score += a[i] * (-2 + i)
    score = -score
    if p[3] < p[4] / 2:
        ans.append(score * p[3])
    else:
        if score % 2 == 0:
            ans.append(score // 2 * p[4])
        else:
            ans.append(score // 2 * p[4] + min(p[4], p[3]))
    # ans.append(int( zfindMinimumCost(p[3], p[4], score)))
    # scoreを稼ぐための4,5の使う回数を微分を用いて見つける
    # print(score)
    # l = -1
    # r = -(-score // 1) + 1
    # while r - l > 1:
    #     # 4の数
    #     add1 = (l + r) // 2
    #     add1_l = max(0, add1 - 1)
    #     add1_r = add1 + 1
    #     # 5の数
    #     add2 = -(-max(0, score - add1) // 2)
    #     add2_l = -(-max(0, score - add1_l) // 2)
    #     add2_r = -(-max(0, score - add1_r) // 2)
    #     cost = add1 * p[3] + add2 * p[4]
    #     cost_l = add1_l * p[3] + add2_l * p[4]
    #     cost_r = add1_r * p[3] + add2_r * p[4]

    #     if cost_l <= cost <= cost_r:
    #         r = add1
    #     elif cost_l >= cost >= cost_r:
    #         l = add1
    #     else:
    #         break
    #     # print(l, r, add1, add2, cost_l, cost, cost_r)
    # ans.append(min(cost, cost_l, cost_r))

for i in ans:
    print(i)
