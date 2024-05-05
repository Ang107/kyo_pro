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

n, m = MII()
ed = [[] for _ in range(n)]
for _ in range(m):
    u, v = MII()
    u -= 1
    v -= 1
    ed[u].append(v)
    ed[v].append(u)
k = II()
pd = []
for _ in range(k):
    p, d = MII()
    p -= 1
    pd.append((p, d))
w = set()
b = []


def bfs(v, dis):
    deq = deque([v])
    visited = [-1] * n
    visited[v] = 0
    kouho = []
    if visited[v] < d:
        w.add(v)
    elif visited[v] == d:
        kouho.append(v)

    while deq:
        v = deq.popleft()

        for next in ed[v]:
            if visited[next] == -1:
                visited[next] = visited[v] + 1
                deq.append(next)

                if visited[next] < d:
                    w.add(next)
                elif visited[next] == d:
                    kouho.append(next)
    return kouho


for p, d in pd:
    b.append(bfs(p, d))

ans = ["0"] * n
for i in b:
    tmp = [j for j in i if j not in w]
    if tmp:
        ans[tmp[0]] = "1"
    else:
        PN()
        exit()
PY()
if k == 0:
    print("1" * n)
else:
    print("".join(ans))
