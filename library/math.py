# n以下の素数のリストを取得
def get_Sosuu(n):
    A = list(range(2, n + 1))
    p = list()
    while A[0] ** 2 <= n:
        tmp = A[0]
        p.append(tmp)
        A = [e for e in A if e % tmp != 0]
    return p + A


# 約数列挙
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# 素因数分解
# 戻り値は(素因数、指数)のタプル)
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


# n進数->10進数
def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


# 10進数->n進数
def base_n(num_10, n):
    if num_10 == 0:
        return 0
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])


import math


# 座標上の点を、原点を中心に回転（反時計回り）時計回りはdをマイナスに
def ratate(a, b, d):
    d_rad = math.radians(d)  # 角度法を弧度法に変換
    rotated = (a + b * 1j) * math.e ** (1j * d_rad)
    return rotated.real, rotated.imag
