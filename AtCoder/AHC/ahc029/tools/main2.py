import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from pprint import pprint
from heapq import heapify,heappop,heappush
import scipy.stats as stats
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1)) #上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
mod = 998244353

Pr = lambda x : print(x)
PY = lambda : print("Yes")
PN = lambda : print("No")
I = lambda : input()
II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照


def First_input():
    global N,M,K,T,L,cards,projects,projects_cospa,max_change_card,card_0_count,card_4_count,hosei,st,card_4_limit,exit_flag
    N,M,K,T = MII()
    cards = [LMII() for _ in range(N)]
    projects = [LMII() for _ in range(M)]
    projects_cospa = list(map(lambda x:x[1]/x[0],projects))
    card_0_count = 0
    card_4_count = 0
    hosei = 1
    card_4_limit = 800
    exit_flag = False
    st = 1.4
    if N <= 3:
        max_change_card = 1

    else:
        max_change_card = N - 2

def Mid_input(bef_c):
    global N,M,K,T,cards,projects,projects_cospa,money,hosei,card_4_limit
    projects = [LMII() for _ in range(M)]
    money = II()
    add_cards = [LMII() for _ in range(K)]
    index,c,m = Choice_in(cards,add_cards,projects)
    cards[bef_c] = [c,m]
    print(index)
    projects_cospa = list(map(lambda x:x[1]/x[0],projects))
    money -= add_cards[index][2]
    # if Tarn == 250:
    #     hosei = calc_hosei()
    # print(f"#{hosei}")
    # if Tarn != 0:
    #     card_4_limit = calc_hosei4()


def calc_hosei0():

    temp = 1 - (1 - clamp(card_0_count/Tarn,0.4,1.4)) * 0.1
    # print(f"#{temp}")
    return temp

def calc_hosei4():
    if card_4_count/Tarn > 0.3:
        return -500* clamp(card_4_count/Tarn,0.3,1.4) +728
    else:
        return 900


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def Choice_in(cards,add_cards,projects):
    global card_0_count,card_4_count
    if Tarn == 999:
        return 0,0,0
    global L
    card_kind = defaultdict(int)
    card_choice = []
    for i,j in cards:
        card_kind[i] += 1
    
    need_work = projects[Pick_pro(projects)][0]
    pro_cospa_max = clamp(max(projects_cospa),0.7,1) **0.5
    pro_cospa_men = clamp(sum(projects_cospa) / M,0.8,1.2) ** 0.3
    next_r = max([j for i,j in projects])
    # print(f"#{card_0_count/(Tarn+1)}")
    for i,j,k in add_cards:
        if exit_flag:
            return 0,0,2**L
        if k <= money:
            if i == 0:
                
                if k == 0:
                    card_choice.append(st*hosei)
                else:
                    card_0_count += 1
                    # print(f"#{pro_cospa_max*j*1.01**L/k,(pro_cospa_max*j*1.01**L/k + 0.5*pro_cospa_max)*2/3,pro_cospa_max}")

                    card_0_count += 1
                    if  money  > 400 * 2**L and  money - k < 300 * 2**L and  Tarn < 950:
                        # card_choice.append(j*1.01**(L+2)/k)
                        card_choice.append(0.95*j*1.01**L/k)
                    else:
                        card_choice.append(j*1.01**L/k)
  


                        # card_choice.append(pro_cospa_max*j*1.01**L/k)


            elif i == 1:
                    temp = 0.8 * ((sum(projects_cospa) - max(projects_cospa))  / (M-1)) ** 0.5
                    # print(f"#{temp}")
                    if  money  > 400 * 2**L and  money - k < 300 * 2**L and  Tarn < 950:
                        # card_choice.append(j*M*temp*1.01**(L+2)/k)
                        card_choice.append(0.9*j*M*temp*1.01**L/k)
                    else:
                        card_choice.append(j*M*temp*1.01**L/k)

                 
            elif i == 2:
                change_card = All_bad(projects,2)
                if   card_kind[2]+card_kind[3] < max_change_card and k == 0 :
                    card_choice.append((st+0.01)*hosei)
                else:
                    card_choice.append(0)
            elif i == 3:
                change_card = All_bad(projects,3)
                if   card_kind[2]+card_kind[3] < max_change_card and k == 0 :
                    card_choice.append((st+0.02)*hosei)
                else:
                    card_choice.append(0)
            elif i == 4 :
                    card_4_count += 1
                    if 20 > L and Tarn < 950 and  k < 2 ** L * (1000-Tarn) * 1.4 and k / 2**L <= card_4_limit and 1.3 * k < money:
                        card_choice.append(100000*2**L/k)
                    else:
                        card_choice.append(0)
            else:
                card_choice.append(0)
        else:
            if i == 0:
                card_0_count += 1
            elif i == 4:
                card_4_count += 1
            card_choice.append(0)
    # print(f"#{card_choice,L}")
    index = card_choice.index(max(card_choice))
    return index,add_cards[index][0],add_cards[index][1]

            





#使用するカードの種類を選択
def Choice_out(cards,projects):
    global L
    temp = 0
    for i,j in enumerate(cards):
        if j[0] == 4:
            L += 1
            return i,0
        elif j[0] == 2 or j[0] == 3:
            temp += 1
            bol,index = All_bad(projects,j[0])
            if bol:
                return i,index
            else:
                a,b = i,index
        elif j[0] == 1:
            temp += 1
            # print(f"#{(sum(projects_cospa)-max(projects_cospa)) / (M-1) }")
            if True or (sum(projects_cospa)-max(projects_cospa)) / (M-1) > 0.8:
                return i,0
            else:
                a,b = i,0
        
    if temp == N:
        return a,b
    # print(f"#{cards}")
    project_index = Pick_pro(projects)
    return Pick_card(cards,projects[project_index][0]),project_index
    


#交代カードを使うべきか選択
def All_bad(projects,card):

    cost_paf = [i[1] / i[0] for i in projects]
    index = cost_paf.index(min(cost_paf))
    s_cospa = sorted(cost_paf,reverse=True)
    if card == 2:
        if s_cospa[-1] <= 0.85 and s_cospa[0] < 1.5: 
            return True,index
        else:
            return False,index
    elif card == 3:
        if max(cost_paf) > 1.2*1.02**M:
            return False,0
        else:
            return True,0


#最も仕事量の大きいカードを選択
#超過しないように工夫
def Pick_card(cards,work):
    #このターンで一つの仕事を終わらせられる場合
    # temp = [j for i,j in cards]
    # max_card = max(temp)
    # index = temp.index(max_card)
    # # print(max_card,cards,index,work)
    # if work * 1.25 > max_card > work:
    #     for i,j in enumerate(cards):
    #         # print(f"#{work,j[1],max_card,temp,cards}")
    #         if work <= j[1] < max_card:
    #             max_card = j[1]
    #             index = i

    #無駄遣いする場合はキープする選択を持つ
    can_exit = {}
    not_can_exit = {}
    over = {}
    for i,j in enumerate(cards):
        if j[0] == 0:
            if work * 1.5 > j[1] >= work :
                can_exit[i] = j[1]
            elif work > j[1] :
                not_can_exit[i] = j[1]
            else:
                over[i] = j[1]
    # print(f"#{can_exit,not_can_exit,over}")
    if can_exit :
        temp = inf
        ans = 0
        for i,j in can_exit.items():
            if j < temp:
                ans = i
                temp = j
        return ans
    elif not_can_exit:
        temp = 0
        ans = 0
        for i,j in not_can_exit.items():
            if j > temp:
                ans = i
                temp = j   
        return ans
    else:
        temp = inf
        ans = 0
        for i,j in over.items():
            if j < temp:
                ans = i
                temp = j   
        return ans

def calc_persent(mean,std,num):
    
    probability = stats.norm.cdf(num, loc=mean, scale=std)
    return probability     

#最もコスパの良いプロジェクトを選択
def Pick_pro(projects):
    global exit_flag
    #mode==1 -> 労力を注ぐプロジェクト,#mode==-1 -> 捨てるプロジェクト,
    max_cospa = 0
    index = 0
    projects_cospa = [0] * M
    num = 1
    
    for i,(p,q) in enumerate(projects):
        if q/p < 0.9:
            projects_cospa[i] = (q/2**L) / (p/2**L)**num
        else:
            projects_cospa[i] = q / p

    if Tarn < 750:
        
        for i,j in enumerate(projects_cospa):
            if j > max_cospa:
                max_cospa = j 
                index = i
    else:
        temp = math.log(1.4/1.01**L,2)
        temp = 1 - calc_persent(0,0.5,temp)
        print(f"#{temp}")
        count_can_exit = 0
        for i,j in enumerate(projects):
            count_can_exit += 1
            if j[0] <= min(money/2**L,(1000 -Tarn) * temp * (card_0_count/Tarn)) * 2**L  * 32 + sum([j for i,j in cards]):
                if projects_cospa[i] > max_cospa:
                    max_cospa = projects_cospa[i] 
                    index = i
        if count_can_exit == 0:
            exit_flag = True

    return index

    # else:
    #     cost_paf = inf
    #     index = -1
    #     for i,j in enumerate(projects_cospa):
    #         if cost_paf > j:
    #             cost_paf = j
    #             index = i
    # return index





def make_glaph():
    glaph_x.append(Tarn)
    glaph_y.append(money)

def plot_glaph():
    import numpy as np
    import matplotlib.pyplot as plt
    left = np.array(glaph_x)
    height = np.array(glaph_y)
    plt.plot(left, height)
    plt.savefig(f'glaph/{File_num}a.jpg')

def Output_score():
    # print(f"#{hosei}")
    print(f"#card_4_limit{card_4_limit,card_4_count/1000}")
    
    print(f"#Score = {int(money**0.5)}")

#開発用
def main():
    global Tarn,money,L
    global glaph_x,glaph_y,File_num
    glaph_x,glaph_y = [],[]
    L = 0
    money = 0
    File_num = sys.argv[1]
    First_input()
    for Tarn in range(T):
        c,m = Choice_out(cards,projects)
        print(c,m)
        Mid_input(c)
        make_glaph()
    
    Output_score()
    plot_glaph()

#提出用      
# def main():
#     global Tarn,money,L
#     global glaph_x,glaph_y,File_num
#     glaph_x,glaph_y = [],[]
#     L = 0
#     money = 0
#     First_input()
#     for Tarn in range(T):
#         c,m = Choice_out(cards,projects)
#         print(c,m)
#         Mid_input(c)

                    




if __name__ == "__main__":
    main()
