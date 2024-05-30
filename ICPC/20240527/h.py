ans = []
while True:
    x, y, s = map(int, input().split())
    if x == y == s == 0:
        break
    mx = 0
    for i in range(1, s):
        j = s - i
        #概算
        nukia_near = (i * 100 / (100 + x))
        nukib_near = (j * 100 / (100 + x))
        
        nukia_just = None
        nukib_just = None
        #厳密な値を求める
        for k in range(int(nukia_near)-5,int(nukia_near)+5):
            if k * (100 + x) // 100 == i:
                nukia_just = k
                
        for k in range(int(nukib_near)-5,int(nukib_near)+5):
            if k * (100 + x) // 100 == j:
                nukib_just = k
        
        #場合によっては条件を満たす税抜き価格が無いため、その場合に対応
        if nukia_just == None or nukib_just == None:
            continue
             
        #厳密な値を用いて変化後の税込みの値段をそれぞれ求める
        cnta = nukia_just * (100 + y) // 100
        cntb = nukib_just * (100 + y) // 100
        
        wa = cnta + cntb
        #答えの更新
        mx = max(mx, wa)
    ans.append(mx)
    
for i in ans:
    print(i)
