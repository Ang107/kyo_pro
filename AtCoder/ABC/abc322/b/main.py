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

#n = int(input())

n,m = map(int,input().split())
s = input()
t = input()

def settou():
    if s == t[:n]:
        return True
    else:
        return False

def setubi():
    if s == t[m-n:]:
        return True
    else:
        return False
    
if settou() and setubi():
    print("0")
elif settou() and not setubi():
    print("1")
elif not settou() and setubi():
    print("2")
elif not settou() and not setubi():
    print("3")

    

    
    


