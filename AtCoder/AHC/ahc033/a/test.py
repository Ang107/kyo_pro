from collections import defaultdict

ans = [input() for _ in range(5)]
# import re

# sum_loss = 0
# for i in ans:
#     print(i.split("Q"))
# for i in ans:
#     lr = 0
#     ud = 0
#     for j in re.split("[PQ]", i):
#         d = defaultdict(int)
#         for k in j:
#             d[k] += 1
#         lr += 2 * min(d["R"], d["L"])
#         ud += 2 * min(d["U"], d["D"])
#         sum_loss += 2 * min(d["R"], d["L"]) + 2 * min(d["U"], d["D"])
#     print(f"No: {i}, LR_Loss: {lr}, UD_Loss: {ud}")
# print(f"Sum_Loss{sum_loss}")
print(max(len(i) for i in ans))
