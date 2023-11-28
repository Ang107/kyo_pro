n,m = map(int,input().split())
c = input().split()
d = input().split()
p = list(map(int,input().split()))
dic = {}
for i in range(len(p)-1):
    dic[d[i]] = p[i+1]
ans = 0
for i in c:
    if i in dic:
        ans += dic[i]
    else:
        ans += p[0]

print(ans)
     