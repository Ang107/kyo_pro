ans = []
while True:
    n = int(input())
    if n == 0:
        break
    from collections import defaultdict

    gold = defaultdict(int)
    all_medal = defaultdict(int)
    for i in range(n):
        y, _, m = input().split()
        if m == "Gold":
            gold[y] += 1
        all_medal[y] += 1
    gold = sorted(gold.items(), key=lambda x: [-x[1], x[0]])
    all_medal = sorted(all_medal.items(), key=lambda x: [-x[1], x[0]])

    ans.append((gold[0][0], all_medal[0][0]))
for i in ans:
    print(*i)
