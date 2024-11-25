from itertools import (
    permutations,  # permutations : 順列全探索
)


pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


n = II()
a = [LMII() for _ in range(n)]
m = II()
xy = [LMII() for _ in range(m)]
xy = [(i - 1, j - 1) for i, j in xy]
ok = [[True] * n for _ in range(n)]
for x, y in xy:
    ok[x][y] = False
    ok[y][x] = False
p = list(range(n))
ans = 1 << 60
for p in permutations(p):
    f = True
    for i in range(n - 1):
        if not ok[p[i]][p[i + 1]]:
            f = False
            break
    if f:
        res = 0
        for i, j in enumerate(p):
            res += a[j][i]
        if ans > res:
            ans = res

if ans == 1 << 60:
    ans = -1
print(ans)
