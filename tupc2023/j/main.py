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
red = set()
blue = set()
ed_red = [[] for _ in range(n)]
ed_blue = [[] for _ in range(n)]
for i in range(1, n):
    print(f"? 1 {i+1}", flush=True)
    c = input()
    if c == "red":
        red.add(0)
        red.add(i)
        ed_red[0].append(i)
        ed_red[i].append(0)
    else:
        blue.add(0)
        blue.add(i)
        ed_blue[0].append(i)
        ed_blue[i].append(0)


for i in range(n + 1):
    if len(red) == n or len(blue) == n:
        break
    r = None
    b = None
    for i in range(n):
        if i not in red:
            r = i
        if i not in blue:
            b = i
        if r and b:
            break
    print(f"? {r+1} {b+1}", flush=True)
    c = input()
    if c == "red":
        red.add(r)
        red.add(b)
        ed_red[r].append(b)
        ed_red[b].append(r)
    else:
        blue.add(r)
        blue.add(b)
        ed_blue[r].append(b)
        ed_blue[b].append(r)


def dfs(ed):
    visited = set()
    deq = deque()
    deq.append(0)
    rslt = []
    while deq:
        v = deq.pop()
        for i in ed[v]:
            if i not in visited:
                rslt.append([v + i, i + 1])
                deq.append(i)
                visited.add(i)
    return rslt

tmp = dfs(red)
if len(tmp) == n-1:
    ans = tmp
else:
    
    
