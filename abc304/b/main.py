n = int(input())
if n <= 999:
    print(n)
elif n <= 9999:
    print(n // 10 * 10)
elif n <= 99999:
    print(n // 100 * 100)
elif n <= 999999:
    print(n // 1000 * 1000)
elif n <= 9999999:
    print(n // 10000 * 10000)
elif n <= 99999999:
    print(n // 100000 * 100000)
elif n <= 999999999:
    print(n // 1000000 * 1000000)