import collections
n = int(input())
a = list(map(int,input().split()))
dic = collections.defaultdict(int)
lis =[]
for i in a:
    dic[i] += 1
    if dic[i] == 2:
        
        print(i,end=' ')





