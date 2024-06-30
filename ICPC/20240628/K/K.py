ans_list = []
t = int(input())
for _ in range(t):
    n = int(input())
    ans = n**0.5 * 2**0.5 / 2
    # ans += 1
    ans_list.append(ans)

for i in ans_list:
    print(i)
