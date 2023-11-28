
n, d = map(int, input().split())
dic = {}
k = 0
for i in range(n):
    
    if k == 0:
        l = tuple(map(int, input().split()))
        dic[l] = True
        k = 1
    else:
        dic[tuple(map(int, input().split()))] = False





def kansen(x, y):
    global dic
    for i in dic.keys():
        distance = ((i[0] - x) ** 2 + (i[1] - y) ** 2) ** (1/2)
        if 0 < distance <= d and not dic[i]:
            dic[(i[0], i[1])] = True
            kansen(i[0], i[1])



kansen(l[0],l[1])

for i in dic:
    if dic[i]:
        print("Yes")
    else:
        print("No")
