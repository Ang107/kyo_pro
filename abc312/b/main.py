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

n,m = map(int,input().split())
for i in range(n):
    l.append(input())


ansl = set()

def tkrsita(i,j):
    if l[i][j] ==  "#" :
        if l[i][j-1] == "#" and l[i-1][j] == "#" and l[i-1][j-1] == "#":
            if l[i][j-2] == "#" and l[i-2][j] == "#" and l[i-1][j-2] == "#" and l[i-2][j-1] == "#" and l[i-2][j-2] == "#":
                if l[i][j-3] == "." and l[i-1][j-3] == "." and l[i-2][j-3] == "." and l[i-3][j-3] == "." and l[i-3][j-2] == "." and l[i-3][j-1] == "." and l[i-3][j] == "." :
                    ansl.add((i-7,j-7))

def   tklue(i,j):
    if l[i][j] ==  "#" :
        if l[i][j+1] == "#" and l[i+1][j] == "#" and l[i+1][j+1] == "#":
            if l[i][j+2] == "#" and l[i+2][j] == "#" and l[i+1][j+2] == "#" and l[i+2][j+1] == "#" and l[i+2][j+2] == "#":
                if l[i][j+3] == "." and l[i+1][j+3] == "." and l[i+2][j+3] == "." and l[i+3][j+3] == "." and l[i+3][j+2] == "." and l[i+3][j+1] == "." and l[i+3][j] == "." :
                    tkrsita(i+8,j+8)




for i in range(0,n-8):
    for j in range(0,m-8):

        tklue(i,j)

for i in ansl:
    print(*i)

