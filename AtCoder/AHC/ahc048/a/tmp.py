tmp = []
for i in range(1, 40):
    for j in range(1, i + 1):
        tmp.append(j / i)
tmp = sorted(set(tmp))
res = 0
for i in range(len(tmp) - 1):
    res += tmp[i + 1] - tmp[i]

res /= len(tmp) - 1
print(res)
print(len(tmp))
tmp = []
for i in range(1, 20):
    for j in range(1, i + 1):
        tmp.append(j / i)
tmp = sorted(set(tmp))
ttmp = []
for i in tmp:
    for j in tmp:
        if i + j <= 1:
            ttmp.append(i + j)
ttmp = sorted(set(ttmp))

for i in range(len(ttmp) - 1):
    res += ttmp[i + 1] - ttmp[i]

res /= len(ttmp) - 1
print(res)
print(len(ttmp))
