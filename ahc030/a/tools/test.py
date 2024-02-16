for i in range(2, 10):
    for j in range(1, 20):
        e = j * 0.01
        tmp = (i * e * (1 - e)) ** 0.5
        print(
            f"k : {i}, e : {e}, tmp : {tmp} 68 : {tmp < 1.5}, 95 : {2 * tmp  < 1.5}, 99 : {3 * tmp < 1.5}"
        )
