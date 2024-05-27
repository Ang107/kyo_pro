n = int(input())
l = []
"""

N回のループの中でN回のループを回せば全体でN^2となるので、
全体で25 * 10 ^ 10の計算量となるのでTLEしてます。

厳密には内側のループは(N - i - 1)回とはなっていますが、

(N-1) + (N-2) + (N-3) + ... 2 + 1 = N * (N-1) // 2 ~= N ^ 2

なのでTLEしているということになります。
 
break等も使用して高速化していますが、それらは定数倍高速化（オーダ記法では変化しない）にしかなりません。
殆どのTLEは定数倍が問題なのではなく、オーダのレベルで誤っているので、その改善を心がけると良いと思います。

また、l[i][0] <= l[j][1]の判定は不要かと思います。
（あっても問題は無いです。）

"""

for _ in range(n):
    left, right = map(int, input().split())
    l.append([left, right])

l.sort(key=lambda x: x[0])

count = 0

# N回のループ
for i in range(n):
    # N回のループ
    for j in range(i + 1, n):
        if l[i][1] >= l[j][0] and l[i][0] <= l[j][1]:
            count += 1
        else:
            break

print(count)
