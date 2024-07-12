ans = 0
for i in range(2, 10**5 + 1):
    tmp = 0
    for j in range(1, int(i**0.5)):
        if i % j == 0:
            tmp += 1
    if int(i**0.5) ** 2 == i:
        tmp += 1
    ans = max(ans, tmp)
print(ans)
