import string
ans = []
while True:
    n = int(input())
    if n == 0:
        break
    k = list(map(int, input().split()))
    s = list(input())
    alfa = string.ascii_lowercase + string.ascii_uppercase
    alfa_idx = {alfa[i]: i for i in range(52)}
    for i in range(len(s)):
        dif = k[i % n]
        s[i] = alfa[(alfa_idx[s[i]] - dif) % 52]
    ans.append(''.join(s))
for i in ans:
    print(i)