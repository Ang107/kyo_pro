import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

#n = int(input())

#a,b = map(int,input().split())
    
s =input()
if s =="ACE" or s =="BDF" or s =="CEG" or s =="DFA" or s =="EGB" or s =="FAC" or s =="GBD" :
    print("Yes")
else:
    print("No")
    


