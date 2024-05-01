def max_dishes(N, Q, A, B):
    # 各材料で作れる最大の料理数を計算
    dishes_A = [q // a for q, a in zip(Q, A)]
    dishes_B = [q // b for q, b in zip(Q, B)]

    # 各料理で作れる最小の料理数を計算
    min_dishes_A = min(dishes_A)
    min_dishes_B = min(dishes_B)

    # 各料理で作れる最大の料理数を計算
    max_dishes_A = sum(dishes_A) - min_dishes_A
    max_dishes_B = sum(dishes_B) - min_dishes_B

    # 合計で作れる最大の料理数を返す
    return max(max_dishes_A, max_dishes_B)


# 入力例1
N = 2
Q = [800, 300]
A = [100, 100]
B = [200, 10]
print(max_dishes(N, Q, A, B))  # 5

# 入力例2
N = 2
Q = [800, 300]
A = [100, 0]
B = [0, 10]
print(max_dishes(N, Q, A, B))  # 38

# 入力例3
N = 2
Q = [800, 300]
A = [801, 300]
B = [800, 301]
print(max_dishes(N, Q, A, B))  # 0
