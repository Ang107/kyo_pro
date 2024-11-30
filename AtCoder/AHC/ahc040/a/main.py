import numpy as np

# 事前に標準正規分布の乱数を生成して保存
precomputed_standard_normal = np.random.normal(0, 1000, size=100000)

print(",".join(map(lambda x: str(int(x)), precomputed_standard_normal)))
