# インポート
import numpy as np

a = np.array([1, 5, 10, 3, 4, 25, 30])


# !!WRITE ME!!に処理を記入する（homework関数を提出することに注意）
def homework(a):
    return a[a % 5 == 0 & a % 2 == 1]


print(homework(a))
