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
    global n,h,v,d,UDLR,ans,x,y,dirt,weight,weight2,weight3,visited_start,visited_goal,visited_mid,count,visited_coordinate,can_visit_list,score,score_list

    score = 0
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
    weight2 = [[0] * n for _ in range(n)]
    weight3 = defaultdict(list)
    #訪れた回数
    visited_start = [[0] * n for _ in range(n)]
    visited_goal = [[0] * n for _ in range(n)]
    visited_mid = [[0] * n for _ in range(n)]
    can_visit_list = [[0] * n for _ in range(n)]

def Input_file():
    global n,h,v,d,UDLR,ans,x,y,dirt,weight,weight2,weight3,visited_start,visited_goal,visited_mid,count,visited_coordinate,can_visit_list,score,score_list

    score = 0
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
    weight3 = defaultdict(list)
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

def calc_weight2():
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
                if p <= n/5:
                    deq.append((x1+around4[temp1][0],y1+around4[temp1][1],p+1))
            gain = 0
            # print(temp)

            for i,j in enumerate(temp):
                gain +=  j * (0.9 ** i)  / len(temp)     

            weight2[x][y] = gain
def avr(x):
    return sum(x)/len(x)
def calc_weight3():
    global weight3_vec
    for x in range(n):
        for y in range(n):
            if n % 3 == 0:
                tempx,tempy = (3*x // n),(3*y // n)
            
            elif n % 3 == 1:
                if 0 <= x <= (n//3 - 1):
                    tempx = 0
                elif n // 3 <= x <= 2*(n//3) :
                    tempx = 1
                elif 2*(n//3)+1 <= x <= n:
                    tempx = 2

                if 0 <= y <= (n//3 - 1):
                    tempy = 0
                elif n // 3 <= y <= 2*(n//3) :
                    tempy = 1
                elif 2*(n//3)+1 <= y <= n:
                    tempy = 2
                
            elif n % 3 == 2:
                if 0 <= x <= n//3:
                    tempx = 0
                elif n // 3 + 1<= x <= 2*(n//3) :
                    tempx = 1
                elif 2*(n//3)+1 <= x <= n:
                    tempx = 2

                if 0 <= y <= (n//3 - 1):
                    tempy = 0
                elif n // 3 <= y <= 2*(n//3) :
                    tempy = 1
                elif 2*(n//3)+1 <= y <= n:
                    tempy = 2
            weight3[(tempx,tempy)].append(d[x][y])
    for k,v in weight3.items():
        weight3[k] = sum(v)/len(v)

    weight3_vec = {}
    gensui = 0.8

    # weight3_vec[(0,0)] = [0+gensui*max(weight3[(0,1)],weight3[(1,0)]),
    #                 weight3[(1,0)]+gensui*max(weight3[(1,1)],weight3[(2,0)]),
    #                 0+gensui*max(weight3[(0,1)],weight3[(1,0)]),
    #                 weight3[(0,1)]+gensui*max(weight3[(0,2)],weight3[(1,1)])]

    # weight3_vec[(0,1)] = [0+gensui*max(weight3[(0,0)],weight3[(0,2)],weight3[(1,1)]),
    #                weight3[(1,1)]+gensui*max(weight3[(1,0)],weight3[(1,2)],weight3[(2,1)]),
    #                weight3[(0,0)]+gensui*max(weight3[(0,1)],weight3[(1,0)]),
    #                weight3[(0,2)]+gensui*weight3[(1,2)]]

    # weight3_vec[(0,2)] = [0+gensui*max(weight3[(0,1)],weight3[(1,2)]),
    #                weight3[(1,2)]+gensui*max(weight3[(1,1)],weight3[(2,2)]),
    #                weight3[(0,1)]+gensui*max(weight3[(0,0)],weight3[(1,1)]),
    #                0+gensui*max(weight3[(0,1)],weight3[(1,2)])]

    # weight3_vec[(1,0)] = [weight3[(0,0)]+gensui*weight3[(0,1)],
    #                weight3[(2,0)]+gensui*weight3[(2,1)],
    #                0+gensui*max(weight3[(0,0)],weight3[(1,1)],weight3[(2,0)]),
    #                weight3[(1,1)]+gensui*max(weight3[(0,1)],weight3[(2,1)],weight3[(1,2)])]

    # weight3_vec[(1,1)] = [weight3[(0,1)]+gensui*max(weight3[(0,0)],weight3[(0,2)]),
    #                weight3[(2,1)]+gensui*max(weight3[(2,0)],weight3[(2,2)]),
    #                weight3[(1,0)]+gensui*max(weight3[(0,0)],weight3[(2,0)]),
    #                weight3[(1,2)]+gensui*max(weight3[(0,2)],weight3[(2,2)])]

    # weight3_vec[(1,2)] = [weight3[(0,2)]+gensui*weight3[(0,1)],
    #                weight3[(2,2)]+gensui*weight3[(2,1)],
    #                weight3[(1,1)]+gensui*max(weight3[(0,1)],weight3[(1,0)],weight3[(2,1)]),
    #                0+gensui*max(weight3[(0,2)],weight3[(1,1)],weight3[(2,2)])]

    # weight3_vec[(2,0)] = [weight3[(1,0)]+gensui*max(weight3[(0,0)],weight3[(1,1)]),
    #                0+gensui*max(weight3[(1,0)],weight3[(2,1)]),
    #                0+gensui*max(weight3[(1,0)],weight3[(2,1)]),
    #                weight3[(2,1)]+gensui*max(weight3[(1,1)],weight3[(2,2)])]

    # weight3_vec[(2,1)] = [weight3[(1,1)]+gensui*max(weight3[(1,0)],weight3[(0,1)],weight3[(1,2)]),
    #                0+gensui*max(weight3[(1,1)],weight3[(2,0)],weight3[(2,2)]),
    #                weight3[(2,0)]+gensui*weight3[(1,0)],
    #                weight3[(2,2)]+gensui*weight3[(1,2)]]

    # weight3_vec[(2,2)] = [weight3[(1,2)]+gensui*max(weight3[(1,1)],weight3[(0,2)]),
    #                0+gensui*max(weight3[(1,2)],weight3[(2,1)]),
    #                weight3[(2,1)]+gensui*max(weight3[(1,1)],weight3[(2,0)]),
    #                0+gensui*max(weight3[(1,2)],weight3[(2,1)])]
    weight3_vec[(0,0)] = [weight3[(0,0)]+gensui*avr((weight3[(0,1)],weight3[(1,0)])),
                   weight3[(1,0)]+gensui*avr((weight3[(1,1)],weight3[(2,0)])),
                    weight3[(0,0)]+gensui*avr((weight3[(0,1)],weight3[(1,0)])),
                    weight3[(0,1)]+gensui*avr((weight3[(0,2)],weight3[(1,1)]))]

    weight3_vec[(0,1)] = [weight3[(0,1)]+gensui*avr((weight3[(0,0)],weight3[(0,2)],weight3[(1,1)])),
                   weight3[(1,1)]+gensui*avr((weight3[(1,0)],weight3[(1,2)],weight3[(2,1)])),
                   weight3[(0,0)]+gensui*avr((weight3[(0,1)],weight3[(1,0)])),
                   weight3[(0,2)]+gensui*weight3[(1,2)]]

    weight3_vec[(0,2)] = [weight3[(0,2)]+gensui*avr((weight3[(0,1)],weight3[(1,2)])),
                   weight3[(1,2)]+gensui*avr((weight3[(1,1)],weight3[(2,2)])),
                   weight3[(0,1)]+gensui*avr((weight3[(0,0)],weight3[(1,1)])),
                   weight3[(0,2)]+gensui*avr((weight3[(0,1)],weight3[(1,2)]))]

    weight3_vec[(1,0)] = [weight3[(0,0)]+gensui*weight3[(0,1)],
                   weight3[(2,0)]+gensui*weight3[(2,1)],
                   weight3[(1,0)]+gensui*avr((weight3[(0,0)],weight3[(1,1)],weight3[(2,0)])),
                   weight3[(1,1)]+gensui*avr((weight3[(0,1)],weight3[(2,1)],weight3[(1,2)]))]

    weight3_vec[(1,1)] = [weight3[(0,1)]+gensui*avr((weight3[(0,0)],weight3[(0,2)])),
                   weight3[(2,1)]+gensui*avr((weight3[(2,0)],weight3[(2,2)])),
                   weight3[(1,0)]+gensui*avr((weight3[(0,0)],weight3[(2,0)])),
                   weight3[(1,2)]+gensui*avr((weight3[(0,2)],weight3[(2,2)]))]

    weight3_vec[(1,2)] = [weight3[(0,2)]+gensui*weight3[(0,1)],
                   weight3[(2,2)]+gensui*weight3[(2,1)],
                   weight3[(1,1)]+gensui*avr((weight3[(0,1)],weight3[(1,0)],weight3[(2,1)])),
                   weight3[(1,2)]+gensui*avr((weight3[(0,2)],weight3[(1,1)],weight3[(2,2)]))]

    weight3_vec[(2,0)] = [weight3[(1,0)]+gensui*avr((weight3[(0,0)],weight3[(1,1)])),
                   weight3[(2,0)]+gensui*avr((weight3[(1,0)],weight3[(2,1)])),
                   weight3[(2,0)]+gensui*avr((weight3[(1,0)],weight3[(2,1)])),
                   weight3[(2,1)]+gensui*avr((weight3[(1,1)],weight3[(2,2)]))]

    weight3_vec[(2,1)] = [weight3[(1,1)]+gensui*avr((weight3[(1,0)],weight3[(0,1)],weight3[(1,2)])),
                   weight3[(2,1)]+gensui*avr((weight3[(1,1)],weight3[(2,0)],weight3[(2,2)])),
                   weight3[(2,0)]+gensui*weight3[(1,0)],
                   weight3[(2,2)]+gensui*weight3[(1,2)]]

    weight3_vec[(2,2)] = [weight3[(1,2)]+gensui*avr((weight3[(1,1)],weight3[(0,2)])),
                   weight3[(2,2)]+gensui*avr((weight3[(1,2)],weight3[(2,1)])),
                   weight3[(2,1)]+gensui*avr((weight3[(1,1)],weight3[(2,0)])),
                   weight3[(2,2)]+gensui*avr((weight3[(1,2)],weight3[(2,1)]))]

    # print(weight3)
    # print(weight3_vec)

def get_weight3(x,y,v):
    
    
    if n % 3 == 0:
        tempx,tempy = (3*x // n),(3*y // n)

    elif n % 3 == 1:
        if 0 <= x <= (n//3 - 1):
            tempx = 0
        elif n // 3 <= x <= 2*(n//3) :
            tempx = 1
        elif 2*(n//3)+1 <= x <= n:
            tempx = 2

        if 0 <= y <= (n//3 - 1):
            tempy = 0
        elif n // 3 <= y <= 2*(n//3) :
            tempy = 1
        elif 2*(n//3)+1 <= y <= n:
            tempy = 2
        
    elif n % 3 == 2:
        if 0 <= x <= n//3:
            tempx = 0
        elif n // 3 + 1<= x <= 2*(n//3) :
            tempx = 1
        elif 2*(n//3)+1 <= x <= n:
            tempx = 2

        if 0 <= y <= (n//3 - 1):
            tempy = 0
        elif n // 3 <= y <= 2*(n//3) :
            tempy = 1
        elif 2*(n//3)+1 <= y <= n:
            tempy = 2
    
    return weight3_vec[(tempx,tempy)][v]
    


def calc_around_avr(x,y):
    temp = []
    for i in range(-n//6,n//6 + 1):
        for j in range(-n//6,n//6 + 1):
            if 0 <= x+i < n and 0 <= y+j < n:
                temp.append(dirt[x+i][y+j])
    return sum(temp)/len(temp)

def calc_around_avr2(x,y):
    temp = []
    for i in range(-n//6,n//6 + 1):
        for j in range(-n//6,n//6 + 1):
            if 0 <= x+i < n and 0 <= y+j < n and abs(i) + abs(j) <= n // 6:
                temp.append(dirt[x+i][y+j] )
    return sum(temp)/len(temp)

def calc_gain(x,y):
    deq = deque()
    deq.append((x,y,0))
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

def cycle(x,y):
    z = 1
    d = {(0,0):(1,z,1,z),
         (0,1):(1,z,1,1),
         (0,2):(1,z,z,1),
         (1,0):(1,1,1,z),
         (1,1):(1,1,1,1),
         (1,2):(1,1,z,1),
         (2,0):(z,1,1,z),
         (2,1):(z,1,1,1),
         (2,2):(z,1,z,1),
         }
    if n % 3 == 0:
        tempx,tempy = (3*x // n),(3*y // n)
    
    elif n % 3 == 1:
        if 0 <= x <= (n//3 - 1):
            tempx = 0
        elif n // 3 <= x <= 2*(n//3) :
            tempx = 1
        elif 2*(n//3)+1 <= x <= n:
            tempx = 2

        if 0 <= y <= (n//3 - 1):
            tempy = 0
        elif n // 3 <= y <= 2*(n//3) :
            tempy = 1
        elif 2*(n//3)+1 <= y <= n:
            tempy = 2
        
    elif n % 3 == 2:
        if 0 <= x <= n//3:
            tempx = 0
        elif n // 3 + 1<= x <= 2*(n//3) :
            tempx = 1
        elif 2*(n//3)+1 <= x <= n:
            tempx = 2

        if 0 <= y <= (n//3 - 1):
            tempy = 0
        elif n // 3 <= y <= 2*(n//3) :
            tempy = 1
        elif 2*(n//3)+1 <= y <= n:
            tempy = 2
    

    return d[(tempx,tempy)]



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
        if not sub_mode:
            calc_score()

def get_max_index():
    temp = 0
    tempx,tempy = 0,0
    for i in range(n):
        for j in range(n):
            if d[i][j] > temp:
                tempx,tempy = i,j
                temp = d[i][j]

    return tempx,tempy
            
def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def run(coe1,coe2,coe3,coe4):
    global x,y,count,clean_max_root
    # max_x,max_y = get_max_index()
    # visited_max_all = set()
    # clean_point = 0
    # clean_max_point = 0
    # clean_count = 0
    # clean_flag = False
    while count < 65000:
        if count >= 55000 and x == 0 and y == 0 :
            break
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        # if clean_flag:
        #     clean_point += dirt[x][y]

        visited_coordinate.add((x,y))
        dirt[x][y] = 0
        count += 1
        visited_mid[x][y] += 1
        Vec = can_visit_list[x][y]
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                # print(calc_around_avr(x+around4[i][0],y+around4[i][1]),weight[x+around4[i][0]][y+around4[i][1]])
                # print(int(dirt[x+around4[i][0]][y+around4[i][1]]),int(calc_gain(x+around4[i][0],y+around4[i][1])),int(calc_around_avr(x+around4[i][0],y+around4[i][1])))
                l.append(dirt[x+around4[i][0]][y+around4[i][1]]**coe1 *calc_gain(x+around4[i][0],y+around4[i][1])**coe2 *calc_around_avr(clamp(x+2*around4[i][0],0,n-1),clamp(y+2*around4[i][1],0,n-1))**coe3 * max(0.3,1 -  200*  visited_mid[x+around4[i][0]][y+around4[i][1]] /  count)**coe4 )
                # print(1 - 100 * visited_mid[x+around4[i][0]][y+around4[i][1]] / (10000 + count))
                # print((1 -  100*  visited_mid[x+around4[i][0]][y+around4[i][1]] / (10000 + count)) )
            else:
                l.append(-inf)
        temp = l.index(max(l))
        ans.append(UDLR[temp])
        # if x == max_x and y == max_y and not clean_flag:
            
        #     clean_flag = True
        #     clean_root = []
        #     clean_max_root = []
        # elif x == max_x and y == max_y and len(visited_max_all) == n**2:
        #     if clean_point // clean_count > clean_max_point:
        #         clean_max_root = clean_root
        #     # print(clean_point//clean_count)
        #     clean_root = []
        #     clean_point = 0
        #     clean_count = 0
        #     visited_max_all = set()

        # if clean_flag:
        #     visited_max_all.add((x,y))
        #     clean_count += 1
        #     clean_root.append(UDLR[temp])

        x,y = x+around4[temp][0] , y+around4[temp][1]
        # print(calc_around_avr(x+around4[i][0],y+around4[i][1]),calc_around_avr2(x+around4[i][0],y+around4[i][1]))
        if not sub_mode:
            calc_score() 
    # while True:
    #     if 90000 >= len(ans) + len(clean_max_root):
    #         ans.extend(clean_max_root)
    #     else:
    #         break
    All_visit()
    goal()



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
        if not sub_mode:
            calc_score()

def calc_score():
    global score
    for i in range(n):
        for j in range(n):
            score += dirt[i][j]

def get_last_score():
    global score_list
    score_list.append(score // (len(ans)-1))
    print(score // (len(ans)-1))
    f = open(f"ahc027\\a\\out\\{Score_file_name}.txt", 'a')
    f.write(f"{Input_file_name:04} : {score // (len(ans)-1)}\n")
    f.close()

def vertification(i,j,k):
    print(score // (len(ans)-1))
    f = open(f"ahc027\\a\\out\\{Score_file_name}.txt", 'a')
    f.write(f"{i,j,k} : {score // (len(ans)-1)}\n")
    f.close()

def end():
    print(sum(score_list)//len(score_list))

    
# calc_weight()
# Input()
# Output()

#検証1
# def main():
#     global Input_file_name,Output_file_name,Score_file_name,score_list,sub_mode
    # sub_mode = False
#     score_list = []
#     for i in range(5):
    #     Input_file_name = i
    #     Output_file_name = f"main9_{Input_file_name:04}"
    #     Score_file_name = "score_main9"
    #     a,b,c = 0.5,0.75,1.25
    #     print(a,b,c)
    #     Input_file()
    #     calc_can_visit()
    #     run(a,b,c)
    #     get_last_score()
    #     Output_file()
    #     print("finish:",i)
    # end()

#検証2
# def main():
#     global Input_file_name,Output_file_name,Score_file_name,score_list,sub_mode
#     sub_mode = False
#     score_list = []
#     for j in range(10):
        
#         Input_file_name = j
#         Output_file_name = f"main10_{Input_file_name:04}"
#         Score_file_name = "score_main9"
#         a,b,c,d = 0.5,0.75,1.25,2
#         print(a,b,c,d)
#         Input_file()
#         calc_weight3()
#         calc_can_visit()
#         run(a,b,c,d)
#         get_last_score()
#         Output_file()
#         # print("finish:",j)
#     end()
        

#提出
def main():
    global sub_mode 
    sub_mode = True
    a,b,c,d = 0.5,0.75,1.25,2
    Input()
    calc_can_visit()
    run(a,b,c,d)
    Output()

if __name__ == '__main__':
    main()















