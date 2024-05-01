a = list(map(int,input().split()))
k = 0
ans = 0
for i in a:
    if i == 1:
        ans += i * (2 ** k)
    k += 1
print(ans)


