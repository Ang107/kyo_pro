ans = []
from collections import defaultdict
def get_score(tpj):
    correct_num = 0
    pena = 0
    wa_num = defaultdict(int)
    for t,p,j in tpj:
        if j == 0:
            correct_num += 1
            pena += t
            pena += 20 * wa_num[p]
        else:
            wa_num[p] += 1
    return (-correct_num,pena)


while 1:
    m,t,p,r = map(int,input().split())
    if m == 0:
        break
    d = [[] for _ in range(t)]
    for _ in range(r):
        tmp = list(map(int,input().split()))
        tmp[0],tmp[1] = tmp[1],tmp[0]
        d[tmp[0]-1].append(tmp[1:])
    score = [(get_score(j),-(i+1)) for i,j in enumerate(d)]
    score.sort()
    rslt = [-score[0][1]]
    prv_score = score[0][0]
    for i in range(1,t):
        if prv_score == score[i][0]:
            rslt.append("=")
            rslt.append(-score[i][1])
        else:
            prv_score = score[i][0]
            rslt.append(",")
            rslt.append(-score[i][1])
    ans.append(rslt)
for i in ans:
    print(*i,sep="")