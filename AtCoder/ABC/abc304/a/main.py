n = int(input())
l = []
for i in range(n):
    k = input().split()

    l.append(k)
x = 0

minA =  int(l[0][1])
for i in range(1,n,1):
    
    if int(l[i][1]) < minA:
        x = i
        minA = int(l[i][1])

for i in range(x,n,1):
    print(l[i][0])

for i in range(0,x,1):
    print(l[i][0])


        

