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

n = int(input())
s = input()

abc = ("A","B","C")
abc = set(abc)

for i in range(n):
    if s[i] in abc:
        abc.remove(s[i])
    if len(abc) == 0:
        print(i + 1)
        exit()

#a,b = map(int,input().split())
    

    
    


