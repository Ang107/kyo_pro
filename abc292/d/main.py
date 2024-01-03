import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


n, m = MII()
dd = defaultdict(list)
for i in range(m):
    u, v = MII()
    dd[u].append(v)
    dd[v].append(u)
visited = set()
dd_groupe_v = defaultdict(list)


def dfs(x, num):
    deq = deque([x])
    dd_groupe_v[num].append(x)
    visited.add(x)
    while deq:
        x = deq.pop()
        for i in dd[x]:
            if i not in visited:
                deq.append(i)
                visited.add(i)
                dd_groupe_v[num].append(i)


groupe_num = 1
for i in range(1, n+1):
    if i not in visited:
        dfs(i, groupe_num)
        groupe_num += 1

for i, j in dd_groupe_v.items():
    temp = 0
    for k in j:
        temp += len(dd[k])
    if temp / 2 == len(j):
        pass
    else:
        print("No")
        exit()

print("Yes")
