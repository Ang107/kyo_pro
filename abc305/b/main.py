dix = {}
dix["A"] = 0
dix["B"]  = 3
dix["C"]  = 4
dix["D"]  = 8
dix["E"]  = 9
dix["F"]  = 14
dix["G"]  = 23

n,m = input().split()

dis = dix[n] - dix[m]
if dis > 0:
    print(dis)
else:
    print(-dis)
