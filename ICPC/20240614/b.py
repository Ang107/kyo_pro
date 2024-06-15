ans = []
def solve(r0, w0, c, r):
    if r0 / w0 >= c:
        return 0
    cnt = 0
    while 1:
        if (r0 + r * cnt) / w0 >= c:
            break
        cnt += 1
    return cnt

while 1:
    r0, w0, c, r = map(int, input().split())
    if r0 == w0 == c == r == 0:
        break
    ans.append(solve(r0, w0, c, r))


for i in ans:
    print(i)