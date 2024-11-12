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
