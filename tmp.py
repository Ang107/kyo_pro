n, m = map(int, input().split())
f = [0] * n
added = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # 二回目以降の情報なら
    if (a, b) in added:
        # 無視する
        pass
    # 新規の情報なら
    else:
        f[a] += 1
        f[b] += 1
        added.append((a, b))
        added.append((b, a))
# print(f)
# 最も友達が多い人の友達の数
max_friends_num = max(f)
# 答えの候補
cand = []
# N人全員を確認
for i in range(n):
    # 部員 i の友達数が最も多いなら
    if f[i] == max_friends_num:
        cand.append(i)
print(min(cand) + 1)
