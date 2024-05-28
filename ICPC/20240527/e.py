ans = []


def f(w):
    tmp = [7, 7, 5, 7, 5]

    for i in range(len(w)):
        if len(tmp) == 0:
            return True
        if tmp[-1] >= len(w[i]):
            tmp[-1] -= len(w[i])
        else:
            return False

        if tmp[-1] == 0:
            tmp.pop()
    return len(tmp) == 0


while 1:
    n = int(input())
    if n == 0:
        break
    w = [input() for _ in range(n)]
    tmp = [7, 7, 5, 7, 5]
    for i in range(n):
        if f(w[i:]):
            ans.append(i + 1)
            break

for i in ans:
    print(i)
