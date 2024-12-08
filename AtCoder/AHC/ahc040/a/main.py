n = 10
sig = 0
t = 1
wh = []
import random

for _ in range(n):
    wh.append((random.randrange(10**4, 10**5), random.randrange(10**4, 10**5)))
print(n, t, sig)
for i in wh:
    print(*i)
for i in wh:
    print(*i)
for _ in range(t):
    print(0, 0)
