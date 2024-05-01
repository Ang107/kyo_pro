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


# ed=隣接リスト[(next, weight)], 初期ノード
def dijkstra(ed, st):
    # 初期化
    n = len(ed)
    visited = [False] * (n + 1)
    distance = [inf] * (n + 1)
    distance[st] = 0
    heap = [(0, st)]
    # ダイクストラ
    while heap:
        dis, v = heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        for next, weight in ed[v]:
            if not visited[next]:
                new_distance = distance[v] + weight
                if new_distance < distance[next]:
                    distance[next] = new_distance
                    heappush(heap, (new_distance, next))
    return distance


n = II()
ed = defaultdict(list)
for i in range(n - 1):
    a, b, x = LMII()
    ed[i].append((i + 1, a))
    ed[i].append((x - 1, b))

dis = dijkstra(ed, 0)

print(dis[n - 1])
