n,m = map(int, input().split())
a =[]
for i in range(m):
    x = list(map(int, input().split()))
    a.append(x)

peal = set()

for i in a:
    for p in range(len(i)-1):
        q = frozenset({i[p],i[p+1]})
        peal.add(q)
        
pean = n * (n-1)/2

print(int(pean-len(peal)))

        
        