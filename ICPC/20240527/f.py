ans = []
boin = set(
    [
        "a",
        "i",
        "u",
        "e",
        "o",
    ]
)


def f(s, length):
    rslt = []

    for idx, i in enumerate(s):
        if idx == 0:
            rslt.append(i)
        if idx > 0 and s[idx - 1] in boin:
            rslt.append(i)
        if len(rslt) == length:
            break
    return "".join(rslt)


while 1:
    n = int(input())
    if n == 0:
        break
    s = [input() for _ in range(n)]
    appended = False
    for i in range(1, 51):
        se = set()
        for j in s:
            tmp = f(j, i)
            if tmp == False:
                break
            se.add(tmp)
        # print(se)

        if len(se) == n:
            ans.append(i)
            appended = True
            break

    if not appended:
        ans.append(-1)
for i in ans:
    print(i)
