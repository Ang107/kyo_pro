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

n = II()
a = LMII()
ed = [[] for _ in range(n)]
for i, j in enumerate(a):
    ed[i].append(j - 1)
visited = [False] * n
finished = [False] * n
roop = set()
# 有向グラフの閉路に含まれる頂点列挙


def get_roop(v):
    deq = deque()
    deq.append(v)
    visited[v] = True
    roopstart = -1
    local_visited = set()
    local_visited.add(v)
    while deq:
        v = deq.pop()
        for i in ed[v]:
            if i in local_visited:
                roopstart = i
                break
            elif visited[i]:
                break
            else:
                visited[i] = True
                local_visited.add(i)
                deq.append(i)
        if roopstart != -1:
            break
    if roopstart == -1:
        return {}

    deq = deque()
    roop = {roopstart}
    deq.append(roopstart)
    visited_n = set()
    visited_n.add(roopstart)
    while deq:
        v = deq.pop()
        for i in ed[v]:
            if i not in visited_n:
                deq.append(i)
                visited_n.add(i)
                roop.add(i)
    return roop


for i in range(n):
    if not visited[i]:
        r = get_roop(i)
        for j in r:
            roop.add(j)
    # print(visited)
print(len(roop))
