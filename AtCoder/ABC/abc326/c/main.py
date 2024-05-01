n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
l = 0
r = 0
temp = 0
ans = []

while True:
    
    while a[l] + m > a[r] :
        # print(l,r)
        r += 1
        temp += 1
        if r == n:
            ans.append(temp)
            print(max(ans))
            exit()
    ans.append(temp)
    l += 1
    temp -= 1