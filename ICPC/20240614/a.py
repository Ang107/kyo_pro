n,m,t = map(int,input().split())
a = list(map(int,input().split()))

tmp = [0] * (t+1)

for i in a:
    l = max(0, i - m)
    r = min(t,i+m)
    # for j in range(l,r):
    #     tmp[j] += 1
    
    tmp[l] += 1
    tmp[r] -= 1
from itertools import accumulate
tmp = list(accumulate(tmp))
# print(tmp)
print(tmp[:-1].count(0))