import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
mod = 998244353
def input(): return sys.stdin.readline().rstrip()
def Pr(*x): return print(*x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill]*l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]

def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
n,m = MII()
a = LMII()
dd = defaultdict(list)
for i in range(m):
    u,v = MII()
    if a[v-1] >= a[u-1]:
        dd[u].append((v,a[v-1]))
    if a[u-1] >= a[v-1]:
        dd[v].append((u,a[u-1]))
    
import heapq
def dijkstra(edges, num_node):
    node = [0] * num_node    
    node[0] = 1     

    node_name = []
    #頂点の値、場所、種類数
    heapq.heappush(node_name, [a[0],1,1])

    while len(node_name) > 0:
        print(node_name)
        #ヒープから取り出し
        val, pos,num = heapq.heappop(node_name)

        if num < node[pos-1]:
            continue
        for factor in edges[pos]:
            goal = factor[0]   #次の頂点
            cost  = factor[1]   #頂点の値
            #更新条件
            if val < cost and node[goal-1] <= num  :
                node[goal-1] = num + 1     #更新
                #ヒープに登録
                heapq.heappush(node_name, [a[goal-1], goal,num+1])
            elif val == cost and node[goal-1] < num:
                node[goal-1] = num
                heapq.heappush(node_name, [a[goal-1], goal,num])
    return node

print(dijkstra(dd,n)[-1])