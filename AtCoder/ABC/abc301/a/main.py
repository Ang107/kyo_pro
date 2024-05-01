N = int(input())
S = input()
a = 0
t = 0
for i in S:
    if i == "A":
        a += 1
    else:
        t += 1
if a < t:
    print("T")
elif t < a:
    print("A")
else:
    if S[-1] == "T":
        print("A")
    else:
        print("T")
