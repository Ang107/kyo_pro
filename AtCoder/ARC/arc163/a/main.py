t = int(input())
l = []
for i in range(t):
    casen = int(input())
    cases = input()
    l.append((casen,cases))
    
for i in l:
    k = 0
    a = i[1][0]

    for p in range(1,i[0]):
        if a < i[1][p]:
            k = 1
            break

        elif a == i[1][p]:
            if i[1][0:p-1] < i[1][p:-1]:

                k = 1
                break

    if k:
        print("Yes")
    else:
        print("No")

