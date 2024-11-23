N = int(input())
A = input().split()
マックス = 0

for i in range(N - 1):
    マックス仮 = 0
    j = 0
    文字セット = set()
    while A[i + j] == A[i + j + 1]:
        if A[i + j] in 文字セット:
            break
        else:
            文字セット.add(A[i + j])
            マックス仮 += 2
            j += 2
            if i + j + 1 >= N:
                break
    マックス = max(マックス, マックス仮)

print(マックス)
