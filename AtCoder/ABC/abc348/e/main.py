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
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n = II()
ed = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = MII()
    u -= 1
    v -= 1
    ed[u].append(v)
    ed[v].append(u)
c = LMII()
part_of_tree_sum = [0] * n
from functools import cache


def f(pearent, x):
    result = c[x]
    for i in ed[x]:
        if i != pearent:
            result += f(x, i)
    part_of_tree_sum[x] = result
    return result


def dfs(x):
    deq = deque()
    visited = [-1] * n
    deq.append(x)
    visited[x] = 0
    result = 0
    while deq:
        x = deq.popleft()
        for i in ed[x]:
            if visited[i] == -1:
                deq.append(i)
                visited[i] = visited[x] + 1
                result += visited[i] * c[i]
    return result


def dfs2(x, s):
    deq = deque()
    visited = [inf] * n
    deq.append(x)
    visited[x] = s
    while deq:
        x = deq.popleft()
        for i in ed[x]:
            if visited[i] == inf:
                deq.append(i)
                tmp = 0
                tmp -= part_of_tree_sum[i]
                tmp += part_of_tree_sum[0] - part_of_tree_sum[i]
                visited[i] = visited[x] + tmp
    return visited


f(-1, 0)
s = dfs(0)
visited = dfs2(0, s)
print(min(visited))
# print(part_of_tree_sum)
# print(visited)
