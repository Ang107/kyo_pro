from sys import stdin, setrecursionlimit
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
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = MII()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
ans = 0
visited = [False] * n


def dfs(s):
    # if len(g[s]) != 3:
    #     return []
    res = [s]
    st = [s]
    visited[s] = True
    while st:
        v = st.pop()
        for next in g[v]:
            if not visited[next] and len(g[next]) == 3:
                st.append(next)
                visited[next] = True
                res.append(next)
    return res


for i in range(n):
    if not visited[i] and len(g[i]) == 3:
        tmp = dfs(i)
        # print(tmp)
        cnt = 0
        for j in tmp:
            for k in g[j]:
                if len(g[k]) == 2:
                    cnt += 1
        ans += cnt * (cnt - 1) // 2
print(ans)

# for i in range(n):
#     if len(g[i]) == 3:
#         tmp = 0
#         for j in g[i]:
#             if len(g[j]) == 2:
#                 tmp += 1
#         ans += tmp * (tmp - 1) // 2
# print(ans)
