import sys
from  collections import deque,defaultdict
from itertools import product
from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
deq = deque()
dic = {}
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]

    
n = II()
S = [input() for _ in range(n)]

def is_Kaibun(x):
    lx = len(x)
    x_rev = x[::-1]
    return x[0:lx//2] == x_rev[0:lx//2]

for i in range(n):
    for j in range(i+1,n):
        if is_Kaibun(S[i]+S[j]) or is_Kaibun(S[j]+S[i]):
            # print(S[i],S[j])
            print("Yes")
            exit()
print("No")



