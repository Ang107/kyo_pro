# import matplotlib.pyplot as plt

# input()
# l = []
# while 1:
#     tmp = input()
#     if tmp[0] != "#":
#         break
#     tmp = int(tmp.split()[2])
#     l.append(tmp)

# plt.figure(figsize=(10, 10))
# plt.bar(range(len(l)), l)

# # グラフの表示
# plt.tight_layout()
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# サンプルの座標データ
points = []
while 1:
    tmp = input().split()
    if tmp[0] == "#":
        points.append((int(tmp[1]), int(tmp[2])))
    else:
        break
print(points)

# x座標とy座標に分解
x, y = zip(*points)

# グラデーション用の色データを生成
colors = np.linspace(0, 1, len(points))

# プロットの準備
plt.figure()
scatter = plt.scatter(x, y, c=colors, cmap="viridis", edgecolor="black")

# 各点を順番に結ぶ
for i in range(len(points) - 1):
    plt.plot(x[i : i + 2], y[i : i + 2], color=plt.cm.viridis(colors[i]))

# カラーバーを追加して時系列の色を分かりやすくする
plt.colorbar(scatter, label="Time")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Coordinates with Time-based Gradient")
plt.show()
