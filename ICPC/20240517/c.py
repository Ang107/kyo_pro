ans_l = []
while True:
    y, c, r = map(int, input().split())
    if y == c == r == 0:
        break
    need = 0
    for i in range(y):
        need = -(-(need * 100) // (100 + r)) + c
        # print(need)
    ans_l.append(need)
for i in ans_l:
    print(i)
