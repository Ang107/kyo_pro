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
import inspect
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
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


def solve(n, m, xy):
    rslt = [[0] * n for _ in range(n)]
    stands = (n - 1) // 2
    win_cnt = [0] * n
    lose_cnt = [0] * n
    for x, y in xy:
        win_cnt[x] += 1
        lose_cnt[y] += 1
        rslt[x][y] = 1
        rslt[y][x] = -1

    play = []
    for i in range(n):
        for j in range(i + 1, n):
            if rslt[i][j] == 0:
                play.append((i, j))

    if max(win_cnt) > stands:
        return 0
    if max(lose_cnt) > stands:
        return 0

    def dfs(win_cnt, lose_cnt, play):
        if not play:
            return 1
        ans = 0

        x, y = play[-1]

        for _ in range(2):
            x, y = y, x
            if win_cnt[x] + 1 > stands:
                continue
            if lose_cnt[y] + 1 > stands:
                continue
            win_cnt_n = win_cnt[:]
            lose_cnt_n = lose_cnt[:]
            win_cnt_n[x] += 1
            lose_cnt_n[y] += 1
            play_n = play[:-1]
            ans += dfs(win_cnt_n, lose_cnt_n, play_n)

        return ans

    return dfs(win_cnt, lose_cnt, play)


ans = []

while 1:
    n = II()
    if n == 0:
        break
    m = II()
    xy = []
    for _ in range(m):
        x, y = MII()
        x -= 1
        y -= 1
        xy.append((x, y))
    ans.append(solve(n, m, xy))


for i in ans:
    print(i)
