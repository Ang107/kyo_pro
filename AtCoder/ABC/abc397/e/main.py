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

n, k = MII()
m = n * k
g = [[] for _ in range(m)]
for _ in range(m - 1):
    u, v = MII()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


def tree_dp_pretreatment(g: list[list[int]], s: int = 0):
    """
    s: 根
    g: グラフ
    木DPの前処理
    頂点sを根としたときに、子から順に頂点を並べた結果と、
    親 to 子のグラフ
    子 to 親のグラフを返す。
    """
    from collections import deque

    n = len(g)
    order = []
    deq = deque([s])
    visited = [False] * n
    visited[s] = True
    child = [[] for _ in range(n)]
    pearent = [[] for _ in range(n)]
    while deq:
        v = deq.popleft()
        order.append(v)
        for next in g[v]:
            if visited[next] == False:
                visited[next] = True
                deq.append(next)
                child[v].append(next)
                pearent[next].append(v)
    order = order[::-1]
    return order, child, pearent


order, child, parent = tree_dp_pretreatment(g, 0)
dp = [-1] * (n * k)
for i in order:
    tmp = []
    for next in child[i]:
        assert dp[next] != -1
        if dp[next] > 0:
            tmp.append(dp[next])
    if len(tmp) == 0:
        dp[i] = 1 % k
    elif len(tmp) == 1:
        dp[i] = (tmp[0] + 1) % k
    elif len(tmp) == 2 and tmp[0] + tmp[1] + 1 == k:
        dp[i] = 0
    else:
        PN()
        exit()
if dp[order[-1]] == 0:
    PY()
else:
    PN()
