s = list(map(int,input().split()))
flag = True
if s[1] >= 100 and s[len(s)-1] <= 675:
    pass
else:
    flag = False

for i in range(len(s)):
    if i == 0:
        if s[i] % 25 != 0:
            flag = False
    else:
        if s[i] % 25 != 0 or s[i-1] > s[i] :
            flag = False
            
if flag :
    print("Yes")
else:
    print("No")

