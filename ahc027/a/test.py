d = [[float('inf'),-1,-1,-1]  for i in range(636)]
with open("ahc027\\a\\out\\coe_out.txt", 'r') as f:
    for i,line in enumerate(f):

        if i % 2 == 0:
            d[i][0] = int(line)
            # print(d[i][0])
        if i % 2 == 1:
            temp,a,b,c = line.split()  
            a = float(a)
            b = float(b)
            c = float(c)
        
            d[i-1][1],d[i-1][2],d[i-1][3], = a,b,c
       
print(d)      
d1 = sorted(d,key=lambda x:x[0])
print(d1)
for i in range(100):
    print(d1[i])