n, m, k = map(int, input().split())
a = list(map(int, input().split()))


def f(a):
    return sum(i for i in a if i >= k)


def g(a):
    return sum(i for i in a if i <= m)


F, G = 0, 0
for i in range(n):
    F += f(a[: i + 1])
    G += g(a[: i + 1])
print(F, G, F - G)
