l, r = map(int, input().split())


def get_primes(n):
    """
    エラストテネスの篩
    O(NloglogN)でN以下の素数を列挙する
    """
    if n <= 1:
        return []
    # n以下のすべての数について素数かどうかを記録する配列
    is_prime = [True] * (n + 1)
    is_prime[0] = False  # 0は素数ではない
    is_prime[1] = False  # 1は素数ではない
    primes = [2]
    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return primes


primes = get_primes(int(r**0.5) + 1)
is_prime = [True] * (r - l + 1)
for p in primes:
    # l <= p * kを満たす最小のk
    # l / p <= k
    k = max(2, -(-l // p))
    while p * k <= r:
        is_prime[p * k - l] = False
        k += 1

add = [False] * (r - l + 1)
for p in primes:
    k = 1
    while p**k <= r:
        if l <= p**k:
            add[p**k - l] = True
        k += 1

ans = 1
for i in range(1, r - l + 1):
    if add[i] or is_prime[i]:
        ans += 1
print(ans)
