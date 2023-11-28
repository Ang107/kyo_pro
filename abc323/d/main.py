import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

def array2(i,j,element):
    return [[element] * j for _ in range(i)]

def sinnsuu(s,c):
    l = []
    binc = bin(c)
    for i in range(-1,-len(str(binc))-1,-1):
        if i == "1":
            l.append(dic[s*(-i)])
    return(l)
    
def for_input(n):
    dd = collections.defaultdict(int)
    for _ in range(n):
        s,c = map(int,input().split())
        
        for i in range(sinnsuu(s,c)):
            dd[i] += 1

    return 

n = int(input())

sc = for_input(n)
#a,b = map(int,input().split())
sl_sum = sum(sc.values())

sc = dict(sorted(sc.items(), key=lambda x: x[0]))
def gattai(s,c):
    if c % 2 == 0:
        return(s*2,c//2,0)
    else:
        return(s*2,c//2,1)
tuika = {}
while True:
    prev = sl_sum
    for s,c in sc.items():
        if c > 1:
            saizu,hetta,nokotta = gattai(s,c)
            sl_sum -= hetta
            if saizu in sc.keys():
                sc[saizu] += hetta
            else:
                tuika[saizu] = hetta
            sc[s] = nokotta
    new = sl_sum
    if new == prev:
        print(sl_sum)
        exit()
    for s,c in tuika.items():
        sc[s] = c

    

    
    


