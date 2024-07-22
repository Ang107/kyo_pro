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


h = None
b = None
score = 0


def deleate():
    global score
    fin = True
    for i in range(h):
        tmp = []
        for j in range(5):
            if not tmp or tmp[-1][0] != b[i][j]:
                tmp.append([b[i][j], 1])
            else:
                tmp[-1][1] += 1

        idx = 0
        for j, k in tmp:
            if k >= 3 and j > 0:
                # print(j, k)
                score += j * k
                b[i][idx : idx + k] = [0] * k
                fin = False

            idx += k
    return fin


def down():
    global b
    # n_b = [[] for _ in range(5)]
    st = [[] for _ in range(5)]
    for i in range(h):
        for j in range(5):
            if b[i][j] != 0:
                st[j].append(b[i][j])
    for i in range(5):
        st[i] = [0] * (h - len(st[i])) + st[i]

    # for i in st:
    #     print(i)
    st_tenti = list(zip(*st))
    for i in range(h):
        st_tenti[i] = list(st_tenti[i])
    #     print(st_tenti[i])
    b = st_tenti


ans = []
while 1:
    h = II()
    score = 0
    if h == 0:
        break
    b = [LMII() for _ in range(h)]
    while 1:
        # for i in b:
        #     print(i)
        # print()
        if deleate():
            break
        # for i in b:
        #     print(i)
        # print()
        down()
    ans.append(score)
for i in ans:
    print(i)
