import time

def array2(i,j,element):
    return [[element] * j] * i

def for_input(n):
    L = []
    for _ in range(n):
        L.append(tuple(map(int,input().split())))
    return L


start = time.time()
ary =array2(10**5,10**3,0)
end = time.time() - start
print(end)