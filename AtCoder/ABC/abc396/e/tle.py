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
inf = float("inf")
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

n, m = MII()
g = [[[] for _ in range(n)] for _ in range(40)]
gg = [[] for _ in range(n)]
for _ in range(m):
    x, y, z = MII()
    x -= 1
    y -= 1
    gg[x].append((y, z))
    gg[y].append((x, z))
    for i in range(31):
        g[i][x].append((y, z >> i & 1))
        g[i][y].append((x, z >> i & 1))
ans = [-1] * n

# for i in range(31):
visited = [-1] * n
for s in range(n):
    if visited[s] != -1:
        continue
    deq = deque()
    deq.append(s)
    visited[s] = 0
    a = []
    while deq:
        v = deq.popleft()
        a.append((v, visited[v]))
        for next, b in gg[v]:
            if visited[next] == -1:
                deq.append(next)
                visited[next] = visited[v] ^ b
            elif visited[next] != visited[v] ^ b:
                print(-1)
                exit()
    for i, num in a:
        ans[i] = num
    for bit in range(30):
        cnt = [0, 0]
        for _, num in a:
            cnt[num >> bit & 1] += 1
        if cnt[0] > cnt[1]:
            pass
        else:
            for i, _ in a:
                ans[i] ^= 1 << bit


print(*ans)
