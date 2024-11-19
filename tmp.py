# ans = "No"
# for mask in range(1 << 4):
#     p, q = 0, 0
#     for i in range(4):
#         if mask >> i & 1:
#             p += abcd[i]
#         else:
#             q += abcd[i]
#     if p == q:
#         ans = "Yes"
# print(ans)
a, b, c, d = list(map(int, input().split()))

if (
    a == b + c + d
    or b == a + c + d
    or c == a + b + d
    or d == a + b + c
    or a + b == c + d
    or a + c == b + d
    or a + d == b + c
):
    print("Yes")
else:
    print("No")
