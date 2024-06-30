ans = []
from string import ascii_lowercase

while 1:
    s = input()
    num = []
    alp_s = []
    alp_l = []
    for i in s:
        if i in [str(j) for j in range(10)]:
            num.append(i)
        elif i in ascii_lowercase:
            alp_s.append(i)
        else:
            alp_l.append(i)

    if s == "#":
        break
    ans.append("".join(sorted(alp_s)) + "".join(sorted(alp_l)) + "".join(sorted(num)))
for i in ans:
    print(i)
