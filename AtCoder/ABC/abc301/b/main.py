N = int(input())
A = map(int,input().split())
A = list(A)
i = 0
while True:
    if A[i] > A[i + 1] :
        q = i + 1
        for p in range(A[i] -1 ,A[i+1],-1):
            
            A.insert(q,p)
            q += 1
    elif A[i] < A[i + 1] :
        q = i + 1
        for p in range(A[i] +1 ,A[i+1],+1):
            
            A.insert(q,p)
            q += 1
    elif A[i] - A[i+1] == 1 or A[i] - A[i+1] == -1:
        pass
    i += 1
    if i == len(A) - 1:
        break
r = 0
for m in A:
    if r == len(A)-1:
        print(f"{m}",)
    else:    
        print(f"{m} ",end="")
    r += 1
    