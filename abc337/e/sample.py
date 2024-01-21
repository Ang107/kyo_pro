N = int(input())
M = 1
while 2**M < N:
    M += 1
print(M)
for i in range(M):
    A = []
    for j in range(N):
        if j >> i & 1:
            A.append(j + 1)
    print(len(A), *A)

S = input()
X = 1
for i in range(len(S)):
    if S[i] == "1":
        X += 1 << i
print(X)
