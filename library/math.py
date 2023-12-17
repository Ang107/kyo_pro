#n以下の素数のリストを取得
def get_Sosuu(n):
    A=list(range(2,n+1))
    p=list()
    while A[0]**2<=n:
        tmp=A[0]
        p.append(tmp)
        A=[e for e in A if e%tmp!=0]
    return p + A