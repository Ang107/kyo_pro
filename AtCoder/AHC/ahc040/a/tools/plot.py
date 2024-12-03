import matplotlib.pyplot as plt

for i in range(100):
    data = []
    with open(f"err/{i:04}.txt", "r") as file:
        for line in file:
            try:
                x, y, z = map(int, line.split())  # 空白で区切られた値を取得
                data.append((x, y, z))
            except:
                pass
    # x, y座標に分解
    x, y, z = zip(*data)

    # 散布図を作成
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, alpha=0.7)
    plt.title("Scatter Plot of Input Data", fontsize=16)
    plt.xlabel("predicted_score", fontsize=12)
    plt.ylabel("actual_score", fontsize=12)
    plt.grid(True)
    plt.savefig(f"plot/{i:04}.png")
    plt.close()  # プロットを閉じる
