import collections
h,w = map(int,input().split())
l = []
co = 0
ltate = collections.defaultdict(int)
lyoko= collections.defaultdict(int)
maxtate,maxyoko = 0,0
se = set()
for i in range(h):
    k = input()
    l.append(k)
for i in range(h):
    for p in range(w):
        if l[i][p] == "#" :
            ltate[i + 1] += 1
            lyoko[p + 1] += 1
            se.add((i+1,p+1))

tmax,tmin = max(ltate.keys()),min(ltate.keys())
ymax,ymin = max(lyoko.keys()),min(lyoko.keys())
for i in range(tmin,tmax + 1):
    for p in range(ymin,ymax + 1):
        if not (i,p) in se:
            t,y = i,p
            break




            


print(t,y)
# print(se)
# print(tmin,tmax,ymin,ymax)
# print(ltate,lyoko)




            
        
