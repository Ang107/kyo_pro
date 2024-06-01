ans = []
while 1:
    n, m = map(int, input().split())
    if n == 0:
        break
    price = m // n
    a = list(map(int, input().split()))

    sum_money = 0
    for money in a:
        #別解
        sum_money += min(price, money)
        # if price < money:
        #     sum_money += price
        # else:
        #     sum_money += money

    ans.append(sum_money)


print(*ans, sep='\n')
