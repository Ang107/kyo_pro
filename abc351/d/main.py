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

h, w = MII()
s = [input() for _ in range(h)]

no_move = set()
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        flag = False
        for x, y in around4:
            if x + i in range(h) and y + j in range(w):
                if s[x + i][y + j] == "#":
                    flag = True
        if flag:
            no_move.add((i, j))


def dfs(x, y):
    result = 0
    deq = deque()
    visited = set()

    deq.append((x, y))
    visited.add((x, y))
    result += 1
    visited_list = []
    while deq:
        x, y = deq.pop()
        # 動けないなら
        if (x, y) in no_move:
            continue
        # 動けるなら
        visited_list.append((x, y))

        for i, j in around4:
            if (
                x + i in range(h)
                and y + j in range(w)
                and (x + i, y + j) not in visited
                and s[x + i][y + j] != "#"
            ):
                result += 1
                deq.append((x + i, y + j))
                visited.add((x + i, y + j))
    return result, visited_list


ans = 1
visited = set()
for i in range(h):
    for j in range(w):
        if (i, j) not in visited and s[i][j] != "#":
            result, visited_list = dfs(i, j)
            for k in visited_list:
                visited.add(k)
            ans = max(ans, result)

            # print([(i + 1, j + 1) for i, j in visited])
print(ans)
