ans = []
while True:
    l = list(map(int, input().split()))
    if l == [0, 0, 0, 0]:
        break
    while len([i for i in l if i != 0]) > 1:
        min_ = min([i for i in l if i != 0])
        for i in range(4):
            if l[i] >= min_:
                l[i] -= min_
        l[l.index(0)] = min_
    ans.append(max(l))
for i in ans:
    print(i)
