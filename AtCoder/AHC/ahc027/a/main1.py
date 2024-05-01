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

def Input():
    global n,h,v,d,UDLR,ans,x,y,dirt,weight,visited_start,visited_goal,count
    count = 0
    n = II()
    h = [input() for _ in range(n-1)]
    v = [input() for _ in range(n)]
    d = [LMII() for _ in range(n)]
    UDLR = ["U","D","L","R"]
    ans = []
    x,y = 0,0
    #現在の汚れ 
    dirt = [[0] * n for _ in range(n)]
    #重みづけ
    weight = [[0] * n for _ in range(n)]
    #訪れた回数
    visited_start = [[0] * n for _ in range(n)]
    visited_goal = [[0] * n for _ in range(n)]

def Input_file():
    
    global n,h,v,d,UDLR,ans,x,y,dirt,weight,visited_start,visited_goal,count
    count = 0
    f = open(f"ahc027\\a\\in\\{Input_file_name:04}.txt", 'r')
    data = f.read()
    f.close()
    
    h = []
    v = []
    data = data.split()
    n = int(data[0])
    d = [[None] * n for _ in range(n)]
    for i,j in enumerate(data):
        if 1 <= i <= n-1:
            h.append(j)
        elif 1 <= i <= 2*n -1:
            v.append(j)
        elif 1 <= i:
            d[(i-2*n)//n][(i-2*n)%n] = int(j)
 

    UDLR = ["U","D","L","R"]
    ans = []
    x,y = 0,0
    #現在の汚れ 
    dirt = [[0] * n for _ in range(n)]
    #重みづけ
    weight = [[0] * n for _ in range(n)]
    #訪れた回数
    visited_start = [[0] * n for _ in range(n)]
    visited_goal = [[0] * n for _ in range(n)]

def Output():
    print("".join(ans))
    # print(len(ans))
def Output_file():
    f = open(f"ahc027\\a\\out\\{Output_file_name}.txt", 'w')
    f.write("".join(ans))
    f.close()



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



def calc_weight():
    for x in range(n):
        for y in range(n):
            temp = []
            for i in range(-n//5,n//5 + 1):
                for j in range(-n//5,n//5 + 1):
                    if 0 <= x+i < n and 0 <= y+j < n:
                        temp.append(d[x+i][y+j])
            weight[x][y] = sum(temp)/len(temp)

def calc_around_avr(x,y):
    temp = []
    for i in range(-n//6,n//6 + 1):
        for j in range(-n//7,n//7 + 1):
            if 0 <= x+i < n and 0 <= y+j < n:
                temp.append(dirt[x+i][y+j])
    return sum(temp)/len(temp)



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
    while count < 10 ** 5 - 50000:
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        dirt[x][y] = 0
        count += 1
        Vec = can_visit(x,y)
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                # print(calc_around_avr(x+around4[i][0],y+around4[i][1]),weight[x+around4[i][0]][y+around4[i][1]])
                l.append( dirt[x+around4[i][0]][y+around4[i][1]]*calc_around_avr(x+around4[i][0],y+around4[i][1]))
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


# calc_weight()
# Input()
# Output()
for i in range(20):
    Input_file_name = i
    Output_file_name = f"main1_{Input_file_name:04}"
    Input_file()
    start()
    mid()
    goal()
    Output_file()













