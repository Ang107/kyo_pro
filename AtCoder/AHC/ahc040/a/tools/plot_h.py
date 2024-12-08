import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import os
from itertools import combinations

# データの準備 (ここではランダムデータを使用しています。実際のデータを適用する場合は読み込み部分を修正してください)
# データリストの準備
hs = []
hps = []
ns = []
ts = []
sigs = []

# データ読み込み処理
for i in range(100):
    with open(f"err/{i:04}.txt", "r") as file:
        for line in file:
            if line[:2] == "!h":
                _, h, hp, n, t, sig = line.split()

                h = int(h)
                hp = int(hp)
                n = int(n)
                t = int(t)
                if h == 0:
                    print(i)
                sig = int(sig)
                hs.append(h)
                hps.append(hp)
                ns.append(n)
                ts.append(t)
                sigs.append(sig)
print(sorted(hs)[:10])
# numpy配列に変換
hs = np.array(hs)
hps = np.array(hps)
ns = np.array(ns)
ts = np.array(ts)
sigs = np.array(sigs)

# 特徴量セット
feature_names = ["sigma", "n", "t"]
all_features = {"sigma": sigs, "n": ns, "t": ts}

# 特徴量のすべての非空組み合わせを生成
feature_combinations = []
for r in range(1, len(feature_names) + 1):
    feature_combinations.extend(combinations(feature_names, r))

# 結果を保存するディレクトリの作成
os.makedirs("results_all_combinations_h", exist_ok=True)

# モデル学習と評価
results = []
for combination in feature_combinations:
    # 使用する特徴量を準備
    selected_features = [all_features[name] for name in combination]
    features = np.column_stack([hs] + selected_features)  # 常に "h" を含む

    # モデルの学習
    model = LinearRegression()
    model.fit(features, hps)

    # 予測
    hps_pred = model.predict(features)

    # 性能評価
    mse = mean_squared_error(hps, hps_pred)
    rmse = np.sqrt(mse)

    # モデル式を生成
    coefficients = model.coef_
    intercept = model.intercept_
    feature_set = ["h"] + list(combination)
    formula = f"hp = {intercept:.4f} + " + " + ".join(
        [
            f"{coeff:.4f} * {feature}"
            for coeff, feature in zip(coefficients, feature_set)
        ]
    )
    print(f"Using {combination}: RMSE = {rmse:.4f}")
    print(f"Model formula: {formula}")

    # 結果リストに追加
    results.append((combination, rmse, formula))

    # 可視化
    plt.figure(figsize=(10, 6))
    plt.scatter(hs, hps, label="Actual hp", color="blue", alpha=0.6)
    plt.scatter(hs, hps_pred, label="Predicted hp", color="red", alpha=0.6)
    plt.title(
        f"Prediction of hp using {', '.join(['h'] + list(combination))}", fontsize=14
    )
    plt.xlabel("h", fontsize=12)
    plt.ylabel("hp", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)

    # プロットを保存
    feature_set_name = "_".join(combination)
    plt.savefig(f"results_all_combinations_h/prediction_h_{feature_set_name}.png")
    plt.close()

# h = hp の仮定モデルを評価
hps_pred_identity = hs  # 予測値として単純に h を仮定

# 性能評価
mse_identity = mean_squared_error(hps, hps_pred_identity)
rmse_identity = np.sqrt(mse_identity)
print(f"Using h = hp assumption: RMSE = {rmse_identity:.4f}")

# プロット
plt.figure(figsize=(10, 6))
plt.scatter(hs, hps, label="Actual hp", color="blue", alpha=0.6)
plt.plot(
    hs, hps_pred_identity, label="h = hp (Identity Model)", color="green", linewidth=2
)
plt.title("Prediction of hp using h = hp assumption", fontsize=14)
plt.xlabel("h", fontsize=12)
plt.ylabel("hp", fontsize=12)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)

# プロットを保存
plt.savefig("results_all_combinations_h/prediction_h_identity_model.png")
plt.close()

# ファイルに結果を保存
results.sort(key=lambda x: x[1])  # RMSEでソート
with open("results_all_combinations_h/performance_summary.txt", "w") as f:
    for combination, rmse, formula in results:
        f.write(f"Using {', '.join(['h'] + list(combination))}: RMSE = {rmse:.4f}\n")
        f.write(f"Model formula: {formula}\n\n")
    f.write(f"\nUsing h = hp assumption: RMSE = {rmse_identity:.4f}\n")

print("すべての結果が 'results_all_combinations/' フォルダに保存されました。")
