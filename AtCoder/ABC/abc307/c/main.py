
import time
START = time.perf_counter()
import sys
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

def to_num(l):
    x_min,y_min = inf,inf
    result = []
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == "#":
                result.append((i,j))
                x_min = min(x_min,i)
                y_min = min(y_min,j)
    return {(i-x_min,j-y_min) for i,j in result}

h,w = MII()
a = [input() for _ in range(h)]
a = to_num(a)

h,w = MII()
b = [input() for _ in range(h)]
b = to_num(b)

h,w = MII()
X = [input() for _ in range(h)]
X = to_num(X)
X = {(10+i) * 30 + 10+j for i,j in X}

# print(X)
sheet = set()

def can_put(i,j,l):
    for x,y in l:
        if i+x in range(30) and j+y in range(30) and (i+x) * 30 + j + y in X:
            pass
        else:
            return False
    return True

for i in range(30):
    for j in range(30):
        for k in range(30):
            for l in range(30):
                if can_put(i,j,a) and can_put(k,l,b):
                    for x,y in a:
                        sheet.add((i+x) * 30 + j + y)
                    for x,y in b:
                        sheet.add((k+x) * 30 + l + y)
                    if len(sheet) == len(X):
                        PY()
                        exit()
                    else:
                        sheet = set()
PN()
                    
# cnt = 0
# import random
# while True:
#     cnt += 1
#     A_or_B = random.choice(range(2))
#     i,j = random.choice(range(30)),random.choice(range(30))
#     if A_or_B == 0:
#         if can_put(i,j,a):
#             for x,y in a:
#                 sheet.add((i+x) * 30 + j + y)
#     else:
#         if can_put(i,j,b):
#             for x,y in b:
#                 sheet.add((i+x) * 30 + j + y)

#     if cnt % 100 == 0:
#         if time.perf_counter() - START > 1.8:
#             break
# print(sheet,X)

# if sheet == X:
#     PY()
# else:
#     PN() 
     
    