for i in range(2, 10):
    for j in range(1, 20):
        e = j * 0.01
        tmp = (i * e * (1 - e)) ** 0.5
        print(
            f"k : {i}, e : {e}, 68 : {tmp < 0.5}, 95 : {2 * tmp  < 0.5}, 99 : {3 * tmp < 0.5}"
        )
