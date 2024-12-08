import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import os
from itertools import combinations

# データの準備 (ここではランダムデータを使用しています。実際のデータを適用する場合は読み込み部分を修正してください)
# データリストの準備
ws = []
wps = []
ns = []
ts = []
sigs = []

# データ読み込み処理
for i in range(100):
    with open(f"err/{i:04}.txt", "r") as file:
        for line in file:
            if line[:2] == "!w":
                _, w, wp, n, t, sig = line.split()

                w = int(w)
                wp = int(wp)
                n = int(n)
                t = int(t)
                if w == 0:
                    print(i)
                sig = int(sig)
                ws.append(w)
                wps.append(wp)
                ns.append(n)
                ts.append(t)
                sigs.append(sig)
print(sorted(ws)[:10])
# numpy配列に変換
ws = np.array(ws)
wps = np.array(wps)
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
os.makedirs("results_all_combinations_w", exist_ok=True)

# モデル学習と評価
results = []
for combination in feature_combinations:
    # 使用する特徴量を準備
    selected_features = [all_features[name] for name in combination]
    features = np.column_stack([ws] + selected_features)  # 常に "w" を含む

    # モデルの学習
    model = LinearRegression()
    model.fit(features, wps)

    # 予測
    wps_pred = model.predict(features)

    # 性能評価
    mse = mean_squared_error(wps, wps_pred)
    rmse = np.sqrt(mse)

    # モデル式を生成
    coefficients = model.coef_
    intercept = model.intercept_
    feature_set = ["w"] + list(combination)
    formula = f"wp = {intercept:.4f} + " + " + ".join(
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
    plt.scatter(ws, wps, label="Actual wp", color="blue", alpha=0.6)
    plt.scatter(ws, wps_pred, label="Predicted wp", color="red", alpha=0.6)
    plt.title(
        f"Prediction of wp using {', '.join(['w'] + list(combination))}", fontsize=14
    )
    plt.xlabel("w", fontsize=12)
    plt.ylabel("wp", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)

    # プロットを保存
    feature_set_name = "_".join(combination)
    plt.savefig(f"results_all_combinations_w/prediction_w_{feature_set_name}.png")
    plt.close()

# w = wp の仮定モデルを評価
wps_pred_identity = ws  # 予測値として単純に w を仮定

# 性能評価
mse_identity = mean_squared_error(wps, wps_pred_identity)
rmse_identity = np.sqrt(mse_identity)
print(f"Using w = wp assumption: RMSE = {rmse_identity:.4f}")

# プロット
plt.figure(figsize=(10, 6))
plt.scatter(ws, wps, label="Actual wp", color="blue", alpha=0.6)
plt.plot(
    ws, wps_pred_identity, label="w = wp (Identity Model)", color="green", linewidth=2
)
plt.title("Prediction of wp using w = wp assumption", fontsize=14)
plt.xlabel("w", fontsize=12)
plt.ylabel("wp", fontsize=12)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)

# プロットを保存
plt.savefig("results_all_combinations_w/prediction_w_identity_model.png")
plt.close()

# ファイルに結果を保存
results.sort(key=lambda x: x[1])  # RMSEでソート
with open("results_all_combinations_w/performance_summary.txt", "w") as f:
    for combination, rmse, formula in results:
        f.write(f"Using {', '.join(['w'] + list(combination))}: RMSE = {rmse:.4f}\n")
        f.write(f"Model formula: {formula}\n\n")
    f.write(f"\nUsing w = wp assumption: RMSE = {rmse_identity:.4f}\n")

print("すべての結果が 'results_all_combinations/' フォルダに保存されました。")
