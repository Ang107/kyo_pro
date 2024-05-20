ans = []
while True:
    n = int(input())
    if n == 0:
        break
    l = list(map(int, input().split()))
    tmp = 0
    for i in range(1, n - 1):
        if l[i - 1] < l[i] and l[i] > l[i + 1]:
            tmp += 1
    ans.append(tmp)

for i in ans:
    print(i)
