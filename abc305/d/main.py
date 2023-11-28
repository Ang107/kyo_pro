import numpy as np
n = int(input())
A = list(map(int,input().split()))    
q = int(input())
se = []
npA = np.array(A)

for i in range(q):
    se.append(tuple(map(int,input().split())))
ans = []
for i in se:
    sl = 0
    npA = np.append(npA,[i[0],i[1]])

    newA = np.sort(npA)
    for p in range(len(newA)):
        if newA[p] == i[0]:
            if p % 2 == 0:
                s = p
            else:
                s = p + 1
        if newA[p] == i[1]:
            if p % 2 != 0:
                g = p
            else:
                g = p - 1
    for r in range(s,g+1,2):
        sl += newA[r+1] - newA[r] 
    ans.append(sl)
for i in ans:

    print(i)
    




