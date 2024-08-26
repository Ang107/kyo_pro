cnt = 0
input()
while 1:
    try:
        a = input().split()
    except:
        break
    if a[0] == "s":
        cnt += 1
print(cnt)
