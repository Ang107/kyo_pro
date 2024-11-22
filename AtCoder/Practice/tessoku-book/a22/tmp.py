n = 100000
a = list(range(2, n + 1))
b = list(reversed(range(2, n + 1)))[: n // 2] + list(range(2, n + 1))[n // 2 :]
print(n)
print(*a)
print(*b)
