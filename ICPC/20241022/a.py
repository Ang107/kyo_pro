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


def solve(w, h, l, r):
    # 処理を記入
    init_pos_LX = 0
    init_pos_LY = 0
    init_pos_RX = 0
    init_pos_RY = 0

    # syokiiti
    for i in range(h):
        for j in range(w):
            if l[i][j] == "L":
                init_pos_LX = i
                init_pos_LY = j
            if r[i][j] == "R":
                init_pos_RX = i
                init_pos_RY = j
    # ikisaki list
    deq = deque()
    # ittatokoro
    visited = [[[[False] * w for _ in range(h)] for _ in range(w)] for _ in range(h)]

    visited[init_pos_LX][init_pos_LY][init_pos_RX][init_pos_RY] = True
    deq.append((init_pos_LX, init_pos_LY, init_pos_RX, init_pos_RY))
    ans = "No"

    while deq:
        LX, LY, RX, RY = deq.popleft()
        if l[LX][LY] == r[RX][RY] == "%":
            ans = "Yes"
            break
        for i, j in around4:
            nLX = LX + i
            nLY = LY + j
            nRX = RX + i
            nRY = RY - j

            # tugino ikisaki
            if nLX in range(h) and nLY in range(w) and l[nLX][nLY] != "#":
                pass
            else:
                nLX = LX
                nLY = LY

            if nRX in range(h) and nRY in range(w) and r[nRX][nRY] != "#":
                pass
            else:
                nRX = RX
                nRY = RY

            if not visited[nLX][nLY][nRX][nRY] and (
                (l[nLX][nLY] == "%") == (r[nRX][nRY] == "%")
            ):
                visited[nLX][nLY][nRX][nRY] = True
                deq.append((nLX, nLY, nRX, nRY))
    # tmp = [[-1] * w for _ in range(h)]
    return ans
    pass


ans = []

while 1:
    # 入力を記入
    w, h = MII()
    if w == h == 0:
        break
    l = []
    r = []
    for _ in range(h):
        tmp = input().split()
        l.append(tmp[0])
        r.append(tmp[1])
    ans.append(solve(w, h, l, r))

    pass

for i in ans:
    print(i)
