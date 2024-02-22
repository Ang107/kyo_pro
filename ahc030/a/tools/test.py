def get_hensa():
    hensa = {}
    for k in range(2, 20):
        for j in range(1, 20):
            e = j * 0.01
            tmp = (k * e * (1 - e)) ** 0.5
            hensa[(k, e)] = tmp
    return hensa
    # print(
    #     f"k : {k}, e : {e}, tmp : {tmp} 68 : {tmp < 1.5}, 95 : {2 * tmp  < 1.5}, 99 : {3 * tmp < 1.5}"
    # )


print(get_hensa())

# for k in range(2, 10):
#     for j in range(1, 20):
#         for v in range(k + 1):
#             e = j * 0.01
#             print(f"k : {k}, v : {v}, e : {e},  {(k-v)*e+v*(1-e)}")
