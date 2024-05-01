import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
import math
sys.setrecursionlimit(10**7)
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

def array2(i,j,element):
    return [[element] * j for _ in range(i)]

def for_input(n):
    L = []
    for _ in range(n):
        L.append(tuple(map(int,input().split())))
    return L

n = int(input())
A =list(map(int,input().split()))

count = 0
while True:
    #リストの要素が偶数か確認
    for i in range(n):
        #奇数ならばcountを出力し終了
        if A[i] % 2 != 0:
            print(count)
            exit()
        #2で割った値を上書き
        A[i] = A[i] / 2
    #ここに到達できている時点でリストの中身は全て偶数なのでカウントを増やす
    count += 1



#各要素の2で割り切ることのできる回数を保存するAns
Ans = []
#全ての要素を走査
for i in A:
    #2で割り切れる回数を保存する変数count
    count = 0
    #２で割り切れる間繰り返す
    while i % 2 == 0:
        i = i / 2
        #カウントを増やす
        count += 1
    #要素の2で割り切ることのできる回数をAnsに追加
    Ans.append(count)
    #各要素のうち、2で割り切ることのできる最低回数を出力
print(min(Ans))


    






    
    


