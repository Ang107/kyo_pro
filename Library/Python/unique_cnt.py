# リストに含まれる要素の種類数を返す(O(N√N))
def unique_cnt(a: list) -> int:
    if not a:
        return 0
    a = sorted(a)
    ans = 1
    for i in range(1, len(a)):
        if a[i - 1] != a[i]:
            ans += 1
    return ans
