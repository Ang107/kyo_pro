# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
h,w = map(int,input().split())
S = [input() for _ in range(h)]

visited = [[0]*w for _ in range(h)]

def get_S(x,y):
    y_l = y
    x_l = x
    while S[x][y_l+1] == ".":
        y_l += 1
    tate_len = []
    for i in range(y,y_l+1):
        temp = 1
        x_l = x
        while S[x_l+1][i] == ".":
            temp += 1
            x_l += 1
        tate_len.append(temp)
    S_len = []
    tate_min = 10**6
    for i in range(len(tate_len)):
        tate_min = min(tate_min,tate_len[i])
        S_len.append((i+1)*tate_min)
    return max(S_len)
        
            
            
ans = []    
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            ans.append(get_S(i,j))

print(max(ans))
            
            