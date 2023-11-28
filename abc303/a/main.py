n = int(input())
s = input()
t = input()
m = 0
for i in range(n):
    if s[i] != t[i] :
        if (s[i] == "1" and t[i] == "l") or  (s[i] == "l" and t[i] == "1") or  (t[i] == "0" and s[i] == "o") or  (t[i] == "o" and s[i] == "0"):
            pass
        else:
            m += 1
            break
if m == 0:
    print("Yes")
else:
    print("No")

