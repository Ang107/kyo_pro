# 90度右回転させたリストを返す
def list_rotate_R90(l):
    return list(zip(*reversed(l)))


# 転置
def tenti(l):
    l = list(zip(*l))
    return l
