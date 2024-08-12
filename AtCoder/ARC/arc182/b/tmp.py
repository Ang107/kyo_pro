n, k = map(int, input().split())
l = list(map(int, input().split()))
tmp = set()
for i in l:
    for j in range(k + 1):
        tmp.add(i // 2**j)
print(len(tmp))
