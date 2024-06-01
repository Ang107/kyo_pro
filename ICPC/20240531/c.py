ans = []
while 1:
    h,w = map(int,input().split())
    if h == 0:
        break
    added = False
    l = []
    for i in range(1,151):
        for j in range(i+1,151):
            l.append((i ** 2 + j ** 2,i,j))
    l.sort()
    # print(l[:100])
    ans.append(l[l.index((h ** 2 + w ** 2,h,w))+1])

for i in ans:
    print(*i[1:])