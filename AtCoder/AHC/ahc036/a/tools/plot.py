import matplotlib.pyplot as plt

input()
l = []
while 1:
    tmp = input()
    if tmp[0] != "#":
        break
    tmp = int(tmp.split()[2])
    l.append(tmp)

plt.figure(figsize=(10, 10))
plt.bar(range(len(l)), l)

# グラフの表示
plt.tight_layout()
plt.show()
