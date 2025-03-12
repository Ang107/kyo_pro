n, m = map(int, input().split())
print(min(100, n), m)

for _ in range(min(100, n)):
    tmp = list(map(int, input().split()))
    print(*tmp)
