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
    global n,h,v,d,UDLR,ans,x,y,dirt,weight,weight2,visited_start,visited_goal,visited_mid,count,visited_coordinate,can_visit_list
    count = 0
    visited_coordinate = set()
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
    visited_mid = [[0] * n for _ in range(n)]
    can_visit_list = [[0] * n for _ in range(n)]

def Input_file():
    global n,h,v,d,UDLR,ans,x,y,dirt,weight,weight2,visited_start,visited_goal,visited_mid,count,visited_coordinate,can_visit_list
    visited_coordinate = set()
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
    weight2 = [[0] * n for _ in range(n)]
    #訪れた回数
    visited_start = [[0] * n for _ in range(n)]
    visited_goal = [[0] * n for _ in range(n)]
    visited_mid = [[0] * n for _ in range(n)]
    can_visit_list = [[0] * n for _ in range(n)]

def Output():
    print("".join(ans))
    # print(len(ans))

def Output_file():
    f = open(f"ahc027\\a\\out\\{Output_file_name}.txt", 'w')
    f.write("".join(ans))
    f.close()



def calc_can_visit():
    for x in range(n):
        for y in range(n):
            Up,Down,Left,Right = False,False,False,False
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
            
            can_visit_list[x][y] = (Up,Down,Left,Right)






def calc_weight():
    weight_avr = 0
    for x in range(n):
        for y in range(n):
            weight_avr += d[x][y]/(n**2)
            temp = []
            for i in range(-n//7,n//7 + 1):
                for j in range(-n//7,n//7 + 1):
                    if 0 <= x+i < n and 0 <= y+j < n:
                        temp.append(d[x+i][y+j])
            weight[x][y] = (sum(temp)/len(temp))
    for x in range(n):
        for y in range(n):
            weight[x][y] = weight[x][y] / weight_avr
    # print(weight)

def calc_weight_v2():
    for x in range(n):
        for y in range(n):
            deq = deque()
            deq.append((x,y,0))
            temp = [d[x][y]]
            visited = set()
            while deq:
                x1,y1,p = deq.pop()
                visited.add((x1,y1))
                Vec = can_visit_list[x1][y1]
                l = []
                for i,j in enumerate(Vec):
                    if j and 0 <= x1+around4[i][0] < n and 0 <= y1+around4[i][1] < n and (x1+around4[i][0],y1+around4[i][1]) not in visited:
                        l.append(d[x1+around4[i][0]][y1+around4[i][1]])
                    else:
                        l.append(0)
                # print(l)
                # print(x,y)
                # print(visited)
                temp.append(max(l))
                temp1 = l.index(max(l))
                if p <= n/6:
                    deq.append((x1+around4[temp1][0],y1+around4[temp1][1],p+1))
            gain = 0
            # print(temp)

            for i,j in enumerate(temp):
                gain +=  j * (0.9 ** i)  / len(temp)     

            weight2[x][y] = gain


def calc_around_avr(x,y):
    temp = []
    for i in range(-n//7,n//7 + 1):
        for j in range(-n//7,n//7 + 1):
            if 0 <= x+i < n and 0 <= y+j < n:
                temp.append(dirt[x+i][y+j])
    return sum(temp)/len(temp)

def calc_gain(x,y,p):
    deq = deque()
    deq.append((x,y,p))
    temp = [dirt[x][y]]
    visited = set()
    while deq:
        x,y,p = deq.pop()
        visited.add((x,y))
        Vec = can_visit_list[x][y]
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n and (x+around4[i][0],y+around4[i][1]) not in visited:
                l.append(dirt[x+around4[i][0]][y+around4[i][1]])
            else:
                l.append(0)
        # print(l)
        # print(x,y)
        # print(visited)
        temp.append(max(l))
        temp1 = l.index(max(l))
        if p <= n/5:
            deq.append((x+around4[temp1][0],y+around4[temp1][1],p+1))
    gain = 0
    # print(temp)
    for i,j in enumerate(temp):
        gain +=  j * (0.9 ** i)  / len(temp)      
    # print(gain)
    return  gain




def All_visit():
    global x,y
    visited_num = 0
    while visited_num < n ** 2  and len(visited_coordinate) < n ** 2:
        visited_coordinate.add((x,y))
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        dirt[x][y] = 0
        if visited_start[x][y] == 0:
            visited_num += 1
        visited_start[x][y] += 1
        Vec = can_visit_list[x][y]
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
    while count < 10 ** 5 - 35000:
        if count >= 60000 and x == 0 and y == 0:
            exit()
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        visited_coordinate.add((x,y))
        dirt[x][y] = 0
        count += 1
        visited_mid[x][y] += 1
        Vec = can_visit_list[x][y]
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                # print(calc_around_avr(x+around4[i][0],y+around4[i][1]),weight[x+around4[i][0]][y+around4[i][1]])
                l.append( dirt[x+around4[i][0]][y+around4[i][1]]**0.8*calc_gain(x+around4[i][0],y+around4[i][1],0)**1.3*calc_around_avr(x+around4[i][0],y+around4[i][1])**0.8 * max(0.15,1 -  100*  visited_mid[x+around4[i][0]][y+around4[i][1]] / (10000 + count))**1.7)
                # print(1 - 100 * visited_mid[x+around4[i][0]][y+around4[i][1]] / (10000 + count))
                # print((1 -  100*  visited_mid[x+around4[i][0]][y+around4[i][1]] / (10000 + count)) )
            else:
                l.append(-inf)
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
        Vec = can_visit_list[x][y]
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

#検証
def main():
    for i in range(20):
        global Input_file_name,Output_file_name
        Input_file_name = i
        Output_file_name = f"main8_{Input_file_name:04}"
        Input_file()
        calc_can_visit()
        mid()
        All_visit()
        goal()
        Output_file()
        print("finish:",i)

#提出
# def main():
#     Input()
#     calc_can_visit()
#     mid()
#     All_visit()
#     goal()
#     Output()

if __name__ == '__main__':
    main()















