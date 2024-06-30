ans = []
while 1:
    s1 = input()
    if s1 == "#":
        break
    s2 = input()
    if s1 < s2:
        ans.append("Yes")
    else:
        ans.append("No")
for i in ans:
    print(i)
