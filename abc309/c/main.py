import collections
import itertools

dd = collections.defaultdict(int)

#入力
n,k = map(int,input().split())
#辞書で日付をキー、薬の量を要素に格納
for i in range(n):
    a,b = map(int,input().split())
    dd[a] += b
#辞書をキーを基準に降順にソート  
sdd = sorted(dd.items(),key=lambda x:x[0],reverse=True)
#日付をdayに、その日まで飲む必要のある薬の量をkusuriに格納
day = []
kusuri = []
for i in sdd:
    day.append(i[0])
    kusuri.append(i[1])
#累積和を求めて、kusuri1[x]に、x日に飲む薬の量を格納
kusuri1 = list(itertools.accumulate(kusuri))

#kusuri1とdayを後ろから走査
for i in range(len(day)-1,-1,-1):
    #薬の量がk以下なら
    if kusuri1[i] <= k : 
        #dayの一番後ろじゃないなら
        if i != len(day)-1:
            print(day[i+1] + 1)
            exit()
        #一番後ろでk以下ー＞1日目でk以下
        else:
            print(1)
            exit()