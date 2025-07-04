import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from pprint import pprint
from heapq import heapify,heappop,heappush
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
    global N,M,K,T,L,cards,projects,projects_cospa
    N,M,K,T = MII()
    cards = [LMII() for _ in range(N)]
    for i,j in cards:
        if i == 4:
            L += 1
    projects = [LMII() for _ in range(M)]
    projects_cospa = list(map(lambda x:x[1]/x[0],projects))

def Mid_input(bef_c):
    global N,M,K,T,cards,projects,projects_cospa,money
    projects = [LMII() for _ in range(M)]
    money = II()
    add_cards = [LMII() for _ in range(K)]
    index,c,m = Choice_in(cards,add_cards,projects)
    cards[bef_c] = [c,m]
    print(index)
    projects_cospa = list(map(lambda x:x[1]/x[0],projects))


def Choice_in(cards,add_cards,projects):
    card_kind = defaultdict(int)
    card_choice = []
    for i,j in cards:
        card_kind[i] += 1
    change_card = All_bad(projects,3)
    temp = 2 ** L
    for i,j,k in add_cards:
        if k <= money:
            if i == 0:
                if k == 0:
                    card_choice.append(1.4)
                else:
                    card_choice.append((j*1.05**L/k))
            elif i == 1:
                card_choice.append(j*N*0.8*1.05**L/k)
            elif i == 2:
                if change_card :
                    card_choice.append((1-card_kind[2]-card_kind[3])*6/((k+1)*temp))
            elif i == 3:
                if change_card :
                    card_choice.append((1-card_kind[2]-card_kind[3])*M*6/(3*(k+1)*temp))
            elif i == 4 and 20 > L and Tarn < 950:
                # print(f"#{k,2 ** L * (1000-Tarn) * 1.4}")
                # if k < 2 ** L * (1000-Tarn)**1.5 * 1.4:
                card_choice.append(inf)
            else:
                card_choice.append(0)
        else:
            card_choice.append(0)
    print(f"#{card_choice}")
    index = card_choice.index(max(card_choice))
    return index,add_cards[index][0],add_cards[index][1]

            





#使用するカードの種類を選択
def Choice_out(cards,projects):
    temp = 0
    for i,j in enumerate(cards):
        if j[0] == 4:
                return i,0
        elif j[0] == 1:
            return i,0
        elif j[0] == 2 or j[0] == 3:
            bol,index = All_bad(projects,j[0])
            a,b = i,index
            if bol:
                return i,index
        
        else:
            temp += 1
    if temp == 0:
        return a,b
    project_index = Pick_pro(projects_cospa,1)
    return Pick_card(cards,projects[project_index][0]),project_index
    


#交代カードを使うべきか選択
def All_bad(projects,card):
    bol = True
    if card == 2:
        worst = 100
        index = 0
        for i,j in enumerate(projects):
            cost_paf = j[1] / j[0]
            if cost_paf > 1.5:
                bol = False
            if cost_paf < worst:
                worst = cost_paf
                index = i
        return bol,index
    elif card == 3:
        worst = 0
        for i,j in enumerate(projects):
            cost_paf = j[1] / j[0]
            if cost_paf > 1.5:
                bol = False
        return bol,0

#最も仕事量の大きいカードを選択
#超過しないように工夫
def Pick_card(cards,work):
    #このターンで一つの仕事を終わらせられる場合
    temp = [j for i,j in cards]
    max_card = max(temp)
    index = temp.index(max_card)
    # print(max_card,cards,index,work)
    if max_card > work:
        for i,j in enumerate(cards):
            # print(f"#{work,j[1],max_card,temp,cards}")
            if work <= j[1] < max_card:
                max_card = j[1]
                index = i
    return index

        

#最もコスパの良いプロジェクトを選択
def Pick_pro(projects_cospa,mord):
    #mode==1 -> 労力を注ぐプロジェクト,#mode==-1 -> 捨てるプロジェクト,
    if mord == 1:
        cost_paf = 0
        index = -1
        for i,j in enumerate(projects_cospa):
            if cost_paf < j:
                cost_paf = j
                index = i
    else:
        cost_paf = inf
        index = -1
        for i,j in enumerate(projects_cospa):
            if cost_paf > j:
                cost_paf = j
                index = i
    return index




def make_glaph():
    glaph_x.append(Tarn)
    glaph_y.append(money)

def plot_glaph():
    import numpy as np
    import matplotlib.pyplot as plt
    left = np.array(glaph_x)
    height = np.array(glaph_y)
    plt.plot(left, height)
    plt.savefig('figure01.jpg')
    


def main():
    global Tarn,money,L
    global glaph_x,glaph_y
    glaph_x,glaph_y = [],[]
    L = 0
    money = 0
    First_input()
    for Tarn in range(T):
        # print(f"#{cards,money}")
        c,m = Choice_out(cards,projects)
        print(c,m)
        # print(f"#{c,m}")
        Mid_input(c)
        make_glaph()
    plot_glaph()
            




if __name__ == "__main__":
    main()
