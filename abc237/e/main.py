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


n, m = MII()
h = LMII()
ed = [[] for _ in range(n)]
for i in range(m):
    u, v = MII()
    ed[u - 1].append(v - 1)
    ed[v - 1].append(u - 1)

# 一周すれば楽しさは確定で負の値になる


# ed=隣接リスト[(next, weight)], 初期ノード
def dijkstra(ed, st):
    # 初期化
    n = len(ed)
    # ->各地点に行くときに考えられる楽しさの最大値をdpで求める
    happy = [inf] * n
    happy[st] = 0
    heap = [(0, st)]
    # ダイクストラ
    while heap:
        hap, v = heappop(heap)
        # -を戻す
        if happy[v] < hap:
            continue
        for next in ed[v]:
            if h[v] == h[next]:
                diff = 0
            elif h[v] < h[next]:
                diff = h[next] - h[v]
            elif h[v] > h[next]:
                diff = 0

            new_happy = happy[v] + diff
            if new_happy < happy[next]:
                happy[next] = new_happy
                heappush(heap, (new_happy, next))
    return happy


unhappy = dijkstra(ed, 0)
# print(unhappy)
ans = []
for i, j in zip(h, unhappy):
    ans.append(h[0] + j - i - 2 * j)
# print(ans)
print(max(ans))
