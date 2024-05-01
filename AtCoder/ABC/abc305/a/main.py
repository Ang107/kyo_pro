n = +int(input())
amari = n % 5
if amari <= 2:
    amari = 0
else :
    amari = 5
syou = n // 5

print(5 * syou + amari)