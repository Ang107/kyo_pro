ans = []
while True:
    x, y, s = map(int, input().split())
    if x == y == s == 0:
        break
    mx = 0
    for i in range(1, s):
        j = s - i
        nukia = -(-i * 100 // (100 + x))
        nukib = -(-j * 100 // (100 + x))
        cnta = nukia * (100 + y) // 100
        cntb = nukib * (100 + y) // 100
        wa = cnta + cntb
        mx = max(mx, wa)
    ans.append(mx)
for i in ans:
    print(i)
