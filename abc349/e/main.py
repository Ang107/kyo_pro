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


# def dlist(*l, fill=0):
#     if len(l) == 1:
#         return [fill] * l[0]
#     ll = l[1:]
#     return [dlist(*ll, fill=fill) for _ in range(l[0])]


# a = [LMII() for _ in range(3)]
# a_sum = sum([sum(i) for i in a])
# # for i in range(3):
# #     for j in range(3):
# #         a[i][j] += 10**9

# # a_n = []
# # for i in a:
# #     a_n.extend(i)
# # a_n.sort()

# # #一手目が中央の場合
# # tk = 0
# # ao = 0
# # tk += a[1][1]
# # a[1][1] = -1
# # for i in [(0,0),(0,2),(2,0),(2,2)]:


# # def isok(l):
# #     tmp = [[0] * 3 for _ in range(3)]
# #     for ij in l:
# #         i, j = ij // 3, ij % 3
# #         tmp[i][j] = 1
# #     tmp_tenti = list(zip(*tmp))
# #     # for i in tmp:
# #     #     print(i)

# #     # for i in tmp_tenti:
# #     #     print(i)

# #     for i in range(3):
# #         if tmp[i] == [1, 1, 1]:
# #             return False

# #     for i in range(3):
# #         if tmp_tenti[i] == (1, 1, 1):
# #             return False

# #     if tmp[0][0] == tmp[1][1] == tmp[2][2] == 1:
# #         return False

# #     if tmp[0][2] == tmp[1][1] == tmp[2][0] == 1:
# #         return False

# #     return True


# # for i in combinations(range(9), 5):
# #     i_other = []
# #     for j in range(9):
# #         if j not in i:
# #             i_other.append(j)
# #     # print(i, i_other)
# #     if isok(i) and isok(i_other):
# #         tk = 0
# #         ao = 0
# #         for jk in i:
# #             j, k = jk // 3, jk % 3
# #             tk += a[j][k]
# #         ao = a_sum - tk
# #         if tk > ao:
# #             print(i, tk, ao)
# #             print("Takahashi")
# #             exit()

# # print("Aoki")


# # #一手目が中央以外の場合
# for i in permutations(range(9)):
#     # 勝てるところで勝っているか
#     tmp = [[0] * 3 for _ in range(3)]
#     tk = 0
#     ao = 0
#     flag = True
#     # print(i)
#     for j in range(9):
#         x, y = i[j] // 3, i[j] % 3
#         # print(x, y)
#         if j % 2 == 0:
#             for k in range(3):
#                 if tmp[k].count("t") >= 2 and tmp[k].count(0) == 1:
#                     flag = False
#                     break
#             for k in range(3):
#                 if [tmp[0][k], tmp[1][k], tmp[2][k]].count("t") >= 2 and [
#                     tmp[0][k],
#                     tmp[1][k],
#                     tmp[2][k],
#                 ].count(0) == 1:
#                     flag = False

#                     break
#             if [tmp[0][0], tmp[1][1], tmp[2][2]].count("t") >= 2 and [
#                 tmp[0][0],
#                 tmp[1][1],
#                 tmp[2][2],
#             ].count(0) == 1:
#                 flag = False
#                 break

#             if [tmp[0][2], tmp[1][1], tmp[2][0]].count("t") >= 2 and [
#                 tmp[0][2],
#                 tmp[1][1],
#                 tmp[2][0],
#             ].count(0) >= 1:
#                 flag = False
#                 break

#             tk += a[x][y]
#             tmp[x][y] = "t"

#         else:
#             for k in range(3):
#                 if tmp[k].count("a") >= 2 and tmp[k].count(0) == 1:
#                     flag = False
#                     break
#             for k in range(3):
#                 if [tmp[0][k], tmp[1][k], tmp[2][k]].count("a") >= 2 and [
#                     tmp[0][k],
#                     tmp[1][k],
#                     tmp[2][k],
#                 ].count(0) == 1:
#                     flag = False

#                     break
#             if [tmp[0][0], tmp[1][1], tmp[2][2]].count("a") >= 2 and [
#                 tmp[0][0],
#                 tmp[1][1],
#                 tmp[2][2],
#             ].count(0) == 1:
#                 flag = False
#                 break

#             if [tmp[0][2], tmp[1][1], tmp[2][0]].count("a") >= 2 and [
#                 tmp[0][2],
#                 tmp[1][1],
#                 tmp[2][0],
#             ].count(0) >= 1:
#                 flag = False
#                 break

#             ao += a[x][y]
#             tmp[x][y] = "a"

#         if not flag:
#             break
#     # print(i)
#     # for i in tmp:
#     #     print(i)
#     if flag:
#         print(i)
#         print(tk, ao)
#         if tk > ao:
#             print("Takahashi")
#             exit()


# print("Aoki")
# def minimax(grid, turn, scores, alpha, beta):
#     winner = check_winner(grid)
#     if winner is not None:
#         return scores[winner] - scores[1 - winner]

#     if turn == 0:  # Maximizing player: Takahashi
#         max_eval = float("-inf")
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] == 0:
#                     grid[i][j] = 1
#                     scores[0] += A[i][j]
#                     eval = minimax(grid, 1 - turn, scores, alpha, beta)
#                     grid[i][j] = 0
#                     scores[0] -= A[i][j]
#                     max_eval = max(max_eval, eval)
#                     alpha = max(alpha, eval)
#                     if beta <= alpha:
#                         break
#             if beta <= alpha:
#                 break
#         return max_eval
#     else:  # Minimizing player: Aoki
#         min_eval = float("inf")
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] == 0:
#                     grid[i][j] = -1
#                     scores[1] += A[i][j]
#                     eval = minimax(grid, 1 - turn, scores, alpha, beta)
#                     grid[i][j] = 0
#                     scores[1] -= A[i][j]
#                     min_eval = min(min_eval, eval)
#                     beta = min(beta, eval)
#                     if beta <= alpha:
#                         break
#             if beta <= alpha:
#                 break
#         return min_eval


# def check_winner(grid):
#     lines = [
#         grid[0],
#         grid[1],
#         grid[2],  # Horizontal
#         [grid[0][0], grid[1][0], grid[2][0]],
#         [grid[0][1], grid[1][1], grid[2][1]],
#         [grid[0][2], grid[1][2], grid[2][2]],  # Vertical
#         [grid[0][0], grid[1][1], grid[2][2]],
#         [grid[0][2], grid[1][1], grid[2][0]],  # Diagonal
#     ]
#     for line in lines:
#         if sum(line) == 3:
#             return 0  # Takahashi wins
#         if sum(line) == -3:
#             return 1  # Aoki wins
#     return None


# # Reading input
# A = []
# for _ in range(3):
#     A.append(list(map(int, input().split())))

# # Initial game state
# grid = [[0] * 3 for _ in range(3)]
# scores = [0, 0]  # Scores for Takahashi and Aoki

# result = minimax(grid, 0, scores, float("-inf"), float("inf"))
# if result > 0:
#     print("Takahashi")
# elif result < 0:
#     print("Aoki")
# else:
#     print(
#         "Draw"
#     )  # This scenario is possible only if scores are equal and no winner by lines

LMII = lambda: list(map(int, input().split()))
# 入力
a = [LMII() for _ in range(3)]

# aを一次元に変換
tmp = []
for i in a:
    tmp.extend(i)
a = tmp

# 縦横斜めになるindexの組
line = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


# ターン数と盤面を受け取り、先手(高橋君）にとって勝ち盤面なら1、負け盤面なら-1を返す。
def f(turn, s):
    # 縦横斜めのラインになっているものがあるか判定
    for i in line:
        if s[i[0]] == s[i[1]] == s[i[2]] == 1:
            return 1
        elif s[i[0]] == s[i[1]] == s[i[2]] == 2:
            return -1

    # 盤面がすべて埋まっている場合は塗ったマスの値の総和を比較
    if turn == 9:
        tk, ao = 0, 0
        for idx, i in enumerate(s):
            if i == 1:
                tk += a[idx]
            else:
                ao += a[idx]

        if tk - ao > 0:
            return 1
        else:
            return -1

    # 高橋君の手番において、一手で遷移な盤面を全探索し、
    # もっとも良い手を打ったとするとき、高橋君にとっての勝ち盤面に遷移可能か
    # (一手で遷移な盤面のうち、一つでも高橋君にとっての勝ち盤面に遷移可能なら1,そうでないなら-1)
    if turn % 2 == 0:
        rslt = -1
        for i in range(9):
            # 空きマスなら
            if s[i] == 0:
                # 盤面のコピー
                s_n = s[:]
                # 盤面の更新
                s_n[i] = 1
                rslt = max(rslt, f(turn + 1, s_n))

    # 青木君の手番において、一手で遷移な盤面を全探索し、
    # もっとも良い手を打ったとするとき、青木君にとっての勝ち盤面に遷移可能か
    # (一手で遷移な盤面うのち、一つでも青木君にとっての勝ち盤面に遷移可能なら-1,そうでないなら1)
    else:
        rslt = 1
        for i in range(9):
            if s[i] == 0:
                s_n = s[:]
                s_n[i] = 2
                rslt = min(rslt, f(turn + 1, s_n))

    return rslt


# 盤面の初期化
s = [0] * 9

# 出力
if f(0, s) == 1:
    print("Takahashi")
else:
    print("Aoki")


