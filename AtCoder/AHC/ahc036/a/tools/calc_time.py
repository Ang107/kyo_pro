from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# データの準備（入力されたデータを使用）
times = []
param = []
for _ in range(500):
    tmp = input().split()
    times.append(float(tmp[0]))
    param.append(list(map(int, tmp[1:])))

# データをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(
    param, times, test_size=0.2, random_state=42
)

# 線形回帰モデルの訓練
model = LinearRegression()
model.fit(X_train, y_train)

# テストセットでの予測
y_pred = model.predict(X_test)

# モデルの評価
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"R² Score: {r2}")

# 係数と切片の出力
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
