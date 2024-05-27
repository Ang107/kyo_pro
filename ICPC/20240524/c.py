ans = []
while True:
    n, l, r = map(int, input().split())
    if n == 0:
        break
    a = [int(input()) for _ in range(n)]
    rslt = 0
    for i in range(l, r + 1):
        breaked = False
        for idx, j in enumerate(a):
            if i % j == 0:
                breaked = True
                if idx % 2 == 0:
                    rslt += 1
                break
        if not breaked:
            if n % 2 == 0:
                rslt += 1

    ans.append(rslt)

for i in ans:
    print(i)
