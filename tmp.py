def f(a, l=[]):
    l.append(a)
    print(id(l))
    print(l)


l = [-1]
f(0)
f(1, l=l)
f(2)
f(3, l=l)
