ans_l = []
while True:
    n, m, p, q = list(map(int, input().split()))
    if (n, m, p, q) == (0, 0, 0, 0):
        break
    f = True
    x = list(map(int, input().split()))
    x = [i - 1 for i in x]
    p -= 1
    p_n = p
    q -= 1
    # OKか判定
    for i in x:
        if p_n - 1 == i:
            p_n -= 1
        elif p_n == i:
            p_n += 1
    if p_n == q:
        f = False
        ans_l.append(["OK"])
        continue
    p_n = p
    q_n = q
    l = [p_n]
    r = [q_n]
    for i in x:
        if p_n - 1 == i:
            p_n -= 1
        elif p_n == i:
            p_n += 1
        l.append(p_n)

    for i in x[::-1]:
        if q_n - 1 == i:
            q_n -= 1
        elif q_n == i:
            q_n += 1
        r.append(q_n)

    r = r[::-1]

    for i in range(m + 1):
        if abs(l[i] - r[i]) == 1:
            ans_l.append((min(l[i], r[i]) + 1, i))
            f = False
            break
    if f:
        ans_l.append(["NG"])
for i in ans_l:
    print(*i)
