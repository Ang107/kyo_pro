def f(depth, num, tmp):
    tmp[depth].add(num)
    if depth == n:
        return
    if num % 2 == 1:
        f(depth + 1, num * 2, tmp)
    else:
        f(depth + 1, num * 2, tmp)
        if num % 3 == 1:
            f(depth + 1, num // 3, tmp)


n, s, y1, y2 = list(map(int, input().split()))
a = [set() for _ in range(n + 1)]
b = [set() for _ in range(n + 1)]
f(0, y1, a)
f(0, y2, b)
for i in range(n + 1):
    for j in a[i]:
        if s - j in b[n - i]:
            print("Yes")
            exit()
print("No")
