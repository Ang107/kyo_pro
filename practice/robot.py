from random import randint

#各状態のQの初期値
#それぞれ上、下、左、右
s1 = [0, 0, 0, 0]
s2 = [0, 0, 0, 0]
s3 = [0, 0, 0, 0]
s4 = [0, 0, 0, 0]

#各状態における各方向に移動する場合の利得
#それぞれ上、下、左、右
r1 = [-1, 0, -1, -1]
r2 = [-1, 0, -1, -1]
r3 = [0, -1, -1, 0]
r4 = [1, -1, 0, -1]

#各状態における各方向に移動する場合の移動先地点
#それぞれ上、下、左、右
s1_next = [s1, s3, s1, s1]
s2_next = [s2, s4, s2, s2]
s3_next = [s1, s3, s3, s4]
s4_next = [s2, s4, s3, s4]

#各状態における各方向に移動する場合の移動先地点を数字で表したもの
#それぞれ上、下、左、右
s1_next_num = [1, 3, 1, 1]
s2_next_num = [2, 4, 2, 2]
s3_next_num = [1, 3, 3, 4]
s4_next_num = [2, 4, 3, 4]

#s(現在の地点)とa(移動方向)を受け取り、Q値を更新する。また、移動先地点を返す。
def Q_Calc(s,a):
    if s == 1:
        s1[a] = 0.5 * s1[a] + 0.5 * (r1[a] + 0.9 * max(s1_next[a]))
        return s1_next_num[a]
    elif s == 2:
        s2[a] = 0.5 * s2[a] + 0.5 * (r2[a] + 0.9 * max(s2_next[a]))
        return s2_next_num[a]
    elif s == 3:
        s3[a] = 0.5 * s3[a] + 0.5 * (r3[a] + 0.9 * max(s3_next[a]))
        return s3_next_num[a]
    elif s == 4:
        s4[a] = 0.5 * s4[a] + 0.5 * (r4[a] + 0.9 * max(s4_next[a]))
        return s4_next_num[a]


#sの初期値設定      
s = 1

#10の5乗回繰り返す
for _ in range(10**6):
    #移動方向をランダムに決定
    a = randint(0,3)
    s = Q_Calc(s,a)

#各状態のQ値を出力
print(list(map(lambda x:round(x,2), s1)))
print(list(map(lambda x:round(x,2), s2)))
print(list(map(lambda x:round(x,2), s3)))
print(list(map(lambda x:round(x,2), s4)))

