from fractions import Fraction

n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    m = Fraction(a,a+b)
    l.append((i+1,m))
    

l.sort(key=lambda x:x[1],reverse=True)


for i in l:


    print(i[0],end=" ") 
        


