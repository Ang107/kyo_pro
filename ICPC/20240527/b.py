ans = []
while 1:
    N = int(input())
    if N == 0:
        break
    l = input().split()
    l = "".join(l)
    rslt = 0
    for i in range(N):
        if l[i : i + 4] == "2020":
            rslt += 1
    ans.append(rslt)
for i in ans:
    print(i)
