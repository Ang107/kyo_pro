r = 500
import math

print(r / 3**0.5, r * (2 / 3) ** 0.5, r)
a = math.pi * (r / 3**0.5) ** 2
b = math.pi * (r * (2 / 3) ** 0.5) ** 2 - a
c = math.pi * r**2 - a - b
print(a, b, c)
