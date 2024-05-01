import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照
    
n = II()
h = [input() for _ in range(n-1)]
v = [input() for _ in range(n)]
d = [LMII() for _ in range(n)]
UDLR = ["U","D","L","R"]
ans = []

def can_visit(x,y):
    Up,Down,Left,Right = False,False,False,False
    # print(x,y)
    #上
    if 0 <= x-1 < n-1 and 0 <= y < n:
        if h[x-1][y] == "0":
            Up = True
    #下
    if 0 <= x < n-1 and 0 <= y < n:
        if h[x][y] == "0":
            Down = True
    #左
    if 0 <= y-1 < n-1 and 0 <= x < n:
        if v[x][y-1] == "0":
            Left = True
    #右
    if 0 <= y < n-1 and 0 <= x < n:
        if v[x][y] == "0":
            Right = True
    
    return Up,Down,Left,Right

x,y = 0,0
#現在の汚れ 
dirt = [[0] * n for _ in range(n)]
#訪れた回数
visited_start = [[0] * n for _ in range(n)]
visited_goal = [[0] * n for _ in range(n)]

def start():
    global x,y,count
    x,y = 0,0
    visited_num = 0
    while visited_num < n ** 2:
        count += 1
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        dirt[x][y] = 0
        if visited_start[x][y] == 0:
            visited_num += 1
        visited_start[x][y] += 1
        Vec = can_visit(x,y)
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                l.append(visited_start[x+around4[i][0]][y+around4[i][1]])
            else:
                l.append(inf)
        temp = l.index(min(l))
        ans.append(UDLR[temp])
        x,y = x+around4[temp][0] , y+around4[temp][1]


def mid():
    global x,y,count
    while count < 10 ** 5 - 10000:
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        dirt[x][y] = 0
        count += 1
        Vec = can_visit(x,y)
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                l.append(dirt[x+around4[i][0]][y+around4[i][1]])
            else:
                l.append(0)
        temp = l.index(max(l))
        ans.append(UDLR[temp])
        x,y = x+around4[temp][0] , y+around4[temp][1]


def goal():
    global x,y
    while x != 0 or y != 0:
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        dirt[x][y] = 0
        visited_goal[x][y] += 1
        Vec = can_visit(x,y)
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                l.append(visited_goal[x+around4[i][0]][y+around4[i][1]])
            else:
                l.append(inf)
        temp = l.index(min(l))
        ans.append(UDLR[temp])
        x,y = x+around4[temp][0] , y+around4[temp][1]

count = 0
start()
mid()
goal()
print("".join(ans))
# print(len(ans))
# print(x,y)











