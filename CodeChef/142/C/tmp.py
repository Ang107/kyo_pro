def f(l):

    return sum(l) & 1


def native(n, m):
    nm = n * m
    min_rslt = [1000000] * (nm + 1)

    for bit in range(1 << nm):
        a = [0] * nm
        c = 0
        for j in range(nm):
            if bit >> j & 1:
                c += 1
                a[j] = 1
        a_n = []
        for j in range(0, nm, m):
            a_n.append(a[j : j + m])
        a = a_n
        a_rev = list(zip(*a))
        rslt = 0
        for j in a:
            rslt += f(j)
        for j in a_rev:
            rslt += f(j)
        min_rslt[c] = min(min_rslt[c], rslt)
    return min_rslt[1:]


for i in range(2, 14, 2):
    for j in range(i, 14, 2):
        if i * j <= 24:
            ans = native(i, j)
            print(i, j, sum(ans))
