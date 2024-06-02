# l = list(map(int, input().split()))
# n = int(input())
# from collections import defaultdict

# dp = [-1 for _ in range(n + 1)]
# dp[0] = defaultdict(int)


# def get_sum(d):
#     if d == -1:
#         return 10**18
#     rslt = 0
#     for i in d.values():
#         rslt += i
#     return rslt


# for i in range(n + 1):
#     for j in l:
#         if dp[i] != -1 and i + j <= n and get_sum(dp[i]) + 1 < get_sum(dp[i + j]):
#             dp[i + j] = dp[i].copy()
#             dp[i + j][j] += 1
# # print(dp)
# print(dp[n])
# # print(2796 * 19 + 30)
tmp = [5, 3, 5]
tmp.remove(5)
print(tmp)
