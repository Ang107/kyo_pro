from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict

from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
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
edge = [LMII() for _ in range(m)]

edge = [(i - 1, j - 1, w) for i, j, w in edge]
ans = 0
g = [[] for _ in range(n)]
for u, v, w in edge:
    g[u].append((v, w))
    g[v].append((u, w))
for i in reversed(range(30)):
    visited = [False] * n
    visited[0] = True
    deq = deque([0])
    while deq:
        v = deq.popleft()
        if v == n - 1:
            break
        for next, w in g[v]:
            # print((w & ans), ans)
            if (~(ans >> i) & (w >> i)) > 0:
                continue
            if not visited[next]:
                visited[next] = True
                deq.append(next)
                if next == n - 1:
                    break
    if visited[n - 1]:
        pass
    else:
        ans += 1 << i
print(ans)
