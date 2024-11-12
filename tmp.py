"""
このように生成できる入力ファイルでTLEしそうです。
例1: 
q = 2 * 10**5
print(q)
for _ in range(10**5):
    print(1)
for _ in range(10**5-1):
    print(2, 10**9)
print(3, 10**9)

例2:
q = 2 * 10**5
print(q)
for _ in range(10**5):
    print(1)
print(2, 1)
for _ in range(10**5-1):
    print(3, 10**9)
"""

###
q = int(input())
tree = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        tree.append(0)
    elif query[0] == 2:
        for i in range(len(tree)):
            tree[i] += query[1]
    elif query[0] == 3:
        ans = 0
        new_tree = []
        for i in range(len(tree)):
            if tree[i] >= query[1]:
                ans += 1
            else:
                new_tree.append(tree[i])
        tree = new_tree
        print(ans)
