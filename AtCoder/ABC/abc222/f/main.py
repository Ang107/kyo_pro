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


def get_dis(s: int, g: list[list[int]]) -> list[int]:
    """
    s: スタートの頂点
    g: グラフ
    s からの全頂点への距離のリストを返す。
    """
    from collections import deque

    n = len(g)
    deq = deque([s])
    dis = [-1] * n
    dis[s] = 0
    while deq:
        v = deq.popleft()
        for next, w in g[v]:
            if dis[next] == -1:
                deq.append(next)
                dis[next] = dis[v] + w
    return dis


def get_diameter(g: list[list[int]]):
    """
    g: グラフ
    木の直径の長さ，及び直径の端点を返す。
    """
    d = get_dis(0, g)
    u = d.index(max(d))
    d = get_dis(u, g)
    v = d.index(max(d))
    return (d[v], u, v)


n = II()
g = [[] for _ in range(n * 2)]
for _ in range(n - 1):
    a, b, c = MII()
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))
d = LMII()
for i in range(n):
    g[i].append((n + i, d[i]))
    g[n + i].append((i, d[i]))

l, s, t = get_diameter(g)
ds = get_dis(s, g)
dt = get_dis(t, g)
s -= n
t -= n
for i in range(n):
    if i == s:
        print(ds[t + n] - d[s])
    elif i == t:
        print(dt[s + n] - d[t])
    else:
        print(max(ds[i], dt[i]))
