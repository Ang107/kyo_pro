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
import pprint
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
from statistics import mean, median,variance,stdev

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

    weight3 = [[] *3 for _ in range(3)]
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
    weight3 = [[[] for _ in range(3)] for _ in range(3)]
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
                if p <= n/5:
                    deq.append((x1+around4[temp1][0],y1+around4[temp1][1],p+1))
            gain = 0
            # print(temp)

            for i,j in enumerate(temp):
                gain +=  j * (0.9 ** i)  / len(temp)     

            weight2[x][y] = gain

def calc_weight3():
    global All_weight
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
            weight3[tempx][tempy].append(d[x][y])
    All_avr = 0
    for i in range(3):
        for j in range(3):
            weight3[i][j] = sum(weight3[i][j])/len(weight3[i][j])
            All_avr += weight3[i][j]//9
    
    All_weight = [sum(weight3[0])//3/All_avr,sum(weight3[-1])//3/All_avr,(weight3[0][0]+weight3[1][0]+weight3[2][0])//3/All_avr,(weight3[0][2]*weight3[1][2]+weight3[2][2])//3/All_avr]
    # print(All_weight)

def calc_around_avr(x,y):
    temp = []
    for i in range(-n//7,n//7 + 1):
        for j in range(-n//7,n//7 + 1):
            if 0 <= x+i < n and 0 <= y+j < n:
                temp.append(dirt[x+i][y+j])
    return sum(temp)/len(temp)

def calc_around_avr3(x,y,v):
    if v == 0 :
        numx_m = n//5
        numx_p = n//8
        numy_m = n//7
        numy_p = n//7
    elif v == 1 :
        numx_m = n//8
        numx_p = n//5
        numy_m = n//7
        numy_p = n//7
    elif v == 2 :
        numx_m = n//7
        numx_p = n//7
        numy_m = n//5
        numy_p = n//8
    elif v == 3 :
        numx_m = n//7
        numx_p = n//7
        numy_m = n//8
        numy_p = n//5
    
    temp = []
    for i in range(-numx_m,numx_p + 1):
        for j in range(-numy_m,numy_p + 1):
            if 0 <= x+i < n and 0 <= y+j < n:
                temp.append(dirt[x+i][y+j])
    return sum(temp)/len(temp)

def calc_around_avr2(x,y):
    temp = []
    for i in range(-n//6,n//6 + 1):
        for j in range(-n//6,n//6 + 1):
            if 0 <= x+i < n and 0 <= y+j < n and abs(i) + abs(j) <= n // 4:
                temp.append(dirt[x+i][y+j] )
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
        if not submit:
            calc_score()


def run():
    global x,y,count,visited_mid
    
    while count < 20000 or len(visited_coordinate) < n**2:
        
        if count >= 5000 and x == 0 and y == 0 and len(visited_coordinate) == n**2:
            break
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        visited_coordinate.add((x,y))
        dirt[x][y] = 0
        count += 1
        visited_mid[x][y] += 1
        # Vec = can_visit_list[x][y]
        l = []
        # for i,j in enumerate(Vec):
        #     if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
             
        #         l.append( dirt[x+around4[i][0]][y+around4[i][1]]**coe1 *calc_gain(x+around4[i][0],y+around4[i][1],0)**coe2 *calc_around_avr3(x+around4[i][0],y+around4[i][1],i)**coe3 * max(0.3,1 -  200*  visited_mid[x+around4[i][0]][y+around4[i][1]] / count )**coe4)
    
        #     else:
        #         l.append(-inf)
        # temp = l.index(max(l))

        xy,route = beem(x,y)
        # if count == 2:
        #     exit()
        # print(temp)
        # ans.append(UDLR[temp])
        # x,y = x+around4[temp][0] , y+around4[temp][1]
        for i in range(n):
            for j in range(n):
                dirt[i][j] += len(xy) * d[i][j]

        ans.append(route)
        temp = 0
        for i,j in xy:
            visited_mid[i][j] += 1
            visited_coordinate.add((i,j))
            dirt[i][j] = (len(xy) - temp) * d[i][j]
            temp += 1
        x,y = xy[-1]
        count += len(route)-1
        if not submit:
            calc_score()

    All_visit()
    goal()

def run2(coe1,coe2,coe3,coe4):
    global x,y,count
    
    while count < 10 ** 5 - 50000 :
        
        if count >= 40000 and x == 0 and y == 0 and len(visited_coordinate) == n**2:
            break
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
             
                # l.append( dirt[x+around4[i][0]][y+around4[i][1]]**coe1 *calc_gain(x+around4[i][0],y+around4[i][1],0)**coe2 *calc_around_avr3(x+around4[i][0],y+around4[i][1],i)**coe3 * max(0.3,1 -  200*  visited_mid[x+around4[i][0]][y+around4[i][1]] / count )**coe4)
                l.append( dirt[x+around4[i][0]][y+around4[i][1]]**coe1 *(dirt[x+around4[i][0]][y+around4[i][1]]+beem(x+around4[i][0],y+around4[i][1]))**coe2 *calc_around_avr3(x+around4[i][0],y+around4[i][1],i)**coe3 * max(0.3,1 -  200*  visited_mid[x+around4[i][0]][y+around4[i][1]] / count )**coe4)
            else:
                l.append(-inf)
        temp = l.index(max(l))

       
        ans.append(UDLR[temp])
        x,y = x+around4[temp][0] , y+around4[temp][1]
        if not submit:
            calc_score()

    All_visit()
    goal()

def standard_d():
    for i in range(n):
        for j in range(n):
            dirt[i][j] = 150*d[i][j]

def beem2(x,y):
    # print(dirt)
    # print(d)
    deq = deque()
    deq.append((None,x,y,{(x,y)},0,0))
    # print(dirt)
    while deq:
        v,x,y,visited,deep,score = deq.popleft()
        Vec = can_visit_list[x][y]
        # print(v,x,y,visited,deep,score )
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                
                if (x+around4[i][0],y+around4[i][1]) in visited:
                    score_temp = score + (d[x+around4[i][0]][y+around4[i][1]]*(deep+1)/2) 
                else:
                    score_temp = score + dirt[x+around4[i][0]][y+around4[i][1]] 
                visited_2 = visited | {(x+around4[i][0],y+around4[i][1])}
                # print(score,dirt[x+around4[i][0]][y+around4[i][1]],d[x+around4[i][0]][y+around4[i][1]])
                if deep == 0:
                    deq.append((i,x+around4[i][0],y+around4[i][1],visited_2,deep+1,score_temp))
                else:
                    deq.append((v,x+around4[i][0],y+around4[i][1],visited_2,deep+1,score_temp))
            # print("bef",deq)
            if i == 3 and deq[0][4] != deep :
                if len(deq) == 1:
                    temp = deq.popleft()
                    return temp[0]

                else:
                    max1,max2,max3 = [0] * 6,[0] * 6,[0] * 6,
                    while deq: 
                        temp = deq.popleft()
                        if max1[5] < temp[5]:
                            max1,max2,max3 = temp,max1,max2
                        elif max2[5] < temp[5]:
                            max2,max3 = temp,max2,
                        elif max3[5] < temp[5]:
                            max3 = temp

                    if max1[5] != 0:
                        deq.append(max1)
                    if max2[5] != 0:
                        deq.append(max2)
                    if max3[5] != 0:
                        deq.append(max3)



                #深さの決定
                if deep == 10 or len({max1[0],max2[0],max3[0]})  == 1:
                    # print(max1,max2)
                    return max1[-1]//max1[-2]
            

def beem(x,y):
    # print(dirt)
    # print(d)
    deq = deque()
    deq.append((None,x,y,[(x,y)],0,"",0))
    # print(dirt)
    while deq:
        v,x,y,visited,deep,route,score = deq.popleft()
        Vec = can_visit_list[x][y]
        # print(v,x,y,visited,deep,score )
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                
                if (x+around4[i][0],y+around4[i][1]) in visited:
                    score_temp = score + (d[x+around4[i][0]][y+around4[i][1]]*(deep+1)/2) * max(0.3,1 -  200*  visited_mid[x+around4[i][0]][y+around4[i][1]] / (count+deep) ) **1.5
                else:
                    score_temp = score + dirt[x+around4[i][0]][y+around4[i][1]]* max(0.3,1 -  200*  visited_mid[x+around4[i][0]][y+around4[i][1]] / (count+deep) ) **1.5
                visited_2 = visited + [(x+around4[i][0],y+around4[i][1])]
                # print(score,dirt[x+around4[i][0]][y+around4[i][1]],d[x+around4[i][0]][y+around4[i][1]])
                if deep == 0:
                    deq.append((i,x+around4[i][0],y+around4[i][1],visited_2,deep+1,route+UDLR[i],score_temp))
                else:
                    deq.append((v,x+around4[i][0],y+around4[i][1],visited_2,deep+1,route+UDLR[i],score_temp))
            # print("bef",deq)
            if i == 3 and deq[0][4] != deep :


                sort_deq = sorted(deq,reverse=True,key=lambda x:x[-1])
                deq = deque()
                for i in range(min(16,len(sort_deq))):
                    deq.append(sort_deq[i])

                #深さの決定

                #まとめて返す長さ
                return_len = 8
                if deep == n*3 or len(set(map(lambda x:x[0],sort_deq)))  == 1:
                    # print(max1,max2)
                    if len(sort_deq[0][3]) >= return_len:
                        # print(sort_deq[0][3][1:return_len+1],sort_deq[0][5][:return_len])
                        return sort_deq[0][3][1:return_len+1],sort_deq[0][5][:return_len]
                        
                    else:
                        # print(sort_deq[0][3][1:len(sort_deq[0][3])+1],sort_deq[0][5][:len(sort_deq[0][3])])
                        return sort_deq[0][3][1:len(sort_deq[0][3])+1],sort_deq[0][5][:len(sort_deq[0][3])]
            
        
    
                
                    


   
    

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
        if not submit:
            calc_score()

def calc_score():
    global score
    for i in range(n):
        for j in range(n):
            score += dirt[i][j]

def get_last_score():
    global score_list
    score_list.append((score-150*sum(map(sum,d)))  // (len(ans)-1//1000))
    # print(score // (len(ans)-1))
    f = open(f"ahc027\\a\\out\\{Score_file_name}.txt", 'a')
    f.write(f"{Input_file_name:04} : {score // (len(ans)-1)}\n")
    f.close()

def vertification(i,j,k):
    print(score // (len(ans)-1//1000))
    f = open(f"ahc027\\a\\out\\{Score_file_name}.txt", 'a')
    f.write(f"{i,j,k} : {score // (len(ans)-1)}\n")
    f.close()

def end():
    print(*score_list)
    print("sum",sum(score_list)//10)
    # print("".join(ans))
    # print("s",int(stdev(score_list)//1000))
    
# calc_weight()
# Input()
# Output()

#検証1
# def main():
#     global Input_file_name,Output_file_name,Score_file_name,score_list
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
def main():
    global Input_file_name,Output_file_name,Score_file_name,score_list,submit
    submit = False
    
    # l = [2]
    # for i in l:
    score_list = []
    a,b,c,d = 0.5,0.5,0.5,2
    print(a,b,c,d)
    for j in range(3):
        print("fin:",j)
        Input_file_name = j
        Output_file_name = f"main12_{Input_file_name:04}"
        Score_file_name = "score_main11"
        
        Input_file()
        # calc_weight3()
        standard_d()
        calc_can_visit()
        run()
        get_last_score()
        Output_file()
        # print("finish:",j)
    end()
        

#提出
# def main():
#     global submit
#     submit = True
#     a,b,c,d = 0.5,0.75,1,2
#     Input()
#     standard_d()
#     calc_can_visit()
#     run()
#     Output()

if __name__ == '__main__':
    main()















