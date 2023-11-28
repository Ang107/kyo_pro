 
import numpy as np 
n,k,q = map(int,input().split())
lis = []
ans = 0
for i in range(q):
    lis.append(tuple(map(int,input().split())))
dic= {}
for i in lis:
    p = 0
    dic[i[0]] = i[1]
 
    a = np.array(dic.values())
    b = np.sort(a)
    for i in b:
        p += 1
        if p <= k:
 
 
            ans += i
    print(ans)
    ans = 0
    
    
