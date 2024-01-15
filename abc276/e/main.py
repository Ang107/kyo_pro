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
mod = 998244353
def input(): return sys.stdin.readline().rstrip()
def Pr(*x): return print(*x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill]*l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]

h,w = MII()
c = [input() for _ in range(h)]

def bfs(sx,sy):
    
    deq = deque([(sx,sy,0)])
    visited = [[0]*w for _ in range(h)]
    while deq:
        # pprint(visited)
        # for i in visited:
        #     print(i)
        # print()
        # print(deq)
        x,y,num = deq.pop()
        if visited[x][y] == 1:
            continue
        if x == sx and y == sy and num < 3:
            pass
        else:
            visited[x][y] = num
        for i,j in around4:
            # print(x+i,y+j,x+i in range(h) and y+j in range(w) and visited[x+i][y+j] == 0 and c[x+i][y+j] == ".",sx == x+i and sy == y+j and num < 3)
            if x+i in range(h) and y+j in range(w) and visited[x+i][y+j] == 0 and c[x+i][y+j] != "#":
                if sx == x+i and sy == y+j and num < 3:
                    pass
                else:
                    deq.append((x+i,y+j,num+1))
    return visited

def get_s():
    for i in range(h):
        for j in range(w):
            if c[i][j] == "S":
                return i,j
                    
x,y = get_s()
visited = bfs(x,y)
if visited[x][y] != 0:
    PY()
else:
    PN()