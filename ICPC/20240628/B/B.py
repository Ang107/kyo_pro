def solve(point):
    point.sort()
    _sum = sum(point[1:-1])
    ave = _sum // (len(point) - 2)
    return ave


ans = []
while 1:
    n = int(input())
    if n == 0:
        break
    point = [int(input()) for i in range(n)]
    ans.append(solve(point))
for i in ans:
    print(i)
