from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = 1 << 60
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

h, w, k = LMII()
rc = set()
# b = [["."] * w for _ in range(h)]
for _ in range(k):
    r, c = MII()
    r -= 1
    c -= 1
    # b[r][c] = "#"
    rc.add((r, c))

# h, w = 3000, 3000
# rc = set()
# import random

# while len(rc) < 3000:
#     rc.add((random.randrange(h), random.randrange(w)))

# print(*b, sep="\n")
dis = [[inf] * w for _ in range(h)]
for i in rc:
    dis[i[0]][i[1]] = 0
deq = deque(rc)
while deq:
    x, y = deq.popleft()
    for dx, dy in dxy4:
        nx = x + dx
        ny = y + dy
        if nx not in range(h) or ny not in range(w):
            continue
        # if dis[(nx, ny)] != inf:
        #     continue
        cand = []
        for dx2, dy2 in dxy4:
            if nx + dx2 not in range(h) or ny + dy2 not in range(w):
                continue
            tmp = dis[nx + dx2][ny + dy2]
            if tmp >= 0 and tmp != inf:
                cand.append(tmp)
        cand.sort()
        if len(cand) >= 2 and cand[1] + 1 < dis[nx][ny]:
            dis[nx][ny] = cand[1] + 1
            deq.append((nx, ny))
        # else:
        #     dis[(nx, ny)] = -1
ans = 0
# tmp = sorted(dis.items())
# num = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        v = dis[i][j]

        if v > 0 and v != inf:
            ans += v


# print(*num, sep="\n")
print(ans)

# for i in range(h):
#     for j in range(w):
#         if (i, j) in rc:
#             continue
#         cand = []
#         for dx, dy in dxy4:
#             nx = i + dx
#             ny = j + dy
#             if nx not in range(h) or ny not in range(w):
#                 continue
#             cand.append(dis[(nx, ny)])
#         cand.sort()

#         if len(cand) >= 2 and cand[1] != inf:
#             ans += cand[1] + 1

# b = ["".join(i) for i in b]
# print(*b, sep="\n")
# cand = []
# by_goal = []
# ans = 0
# for i in range(h):
#     for j in range(w):
#         if (i, j) in rc:
#             continue
#         cnt = 0
#         for dx, dy in dxy4:
#             cnt += (i + dx, j + dy) in rc
#         if cnt >= 2:
#             ans += 1
#             by_goal.append((i, j))
#             continue
#         cand.append((i, j))
# for i, j in cand:
#     cnt = 0
#     for dx, dy in dxy4:
#         cnt += (i + dx, j + dy) in by_goal
#     if cnt >= 2:
#         ans += 2
# print(ans)
