import copy
n,m,h,k = map(int,input().split())
s = input()
kail = set()
usedkail =[]
pointx = 0
pointy = 0
for i in range(m):
    a = frozenset(map(int,input().split()))
    kail.add(a)
life = True

def idou(nu):

    global pointx,pointy
    if nu == "R":
        pointx += 1 
    elif nu == "L":
        pointx -= 1 

    
    elif nu == "U":
        pointy += 1 

    elif nu == "D":
        pointy -= 1 

for i in s:
    h -= 1
    if h < 0:
        life = False
        break
    else:
        idou(i)
        if  h < k :
            
            
            if {pointx,pointy} in kail:
                h = k
                kail.remove({pointx,pointy})

            
if life:
    print("Yes")
else:
    print("No")

