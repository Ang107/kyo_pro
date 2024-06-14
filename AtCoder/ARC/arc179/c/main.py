II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
turn = 0
n = II()

memo = {}


def query(i, j):
    global turn
    turn += 1
    print("?", i, j, flush=True)
    res = II()
    if res == -1:
        if turn > 25000:
            print(1 / 0)
        else:
            exit()
    return res


def plus(i, j):
    global turn
    turn += 1
    print("+", i, j, flush=True)
    res = II()
    if res == -1:
        if turn > 25000:
            print(1 / 0)
        else:
            exit()
    return res


# max:1, min:0
def get_idx(candidates, max_min):
    while len(candidates) > 1:
        next_candidates = []

        for i in range(0, len(candidates), 2):
            if i + 1 < len(candidates):
                pair = (candidates[i], candidates[i + 1])
                if pair not in memo:
                    res = query(candidates[i], candidates[i + 1])
                    memo[pair] = res
                else:
                    res = memo[pair]

                if res == max_min:
                    next_candidates.append(candidates[i + 1])
                else:
                    next_candidates.append(candidates[i])
            else:
                next_candidates.append(candidates[i])

        candidates = next_candidates
    return candidates[0]


def sort_candidates_by_history(candidates):
    # Sort candidates based on the number of comparisons they have been part of
    candidates.sort(
        key=lambda x: sum((x == p[0] or x == p[1]) for p in memo), reverse=True
    )
    return candidates


candidates = list(range(1, n + 1))

while len(candidates) > 1:
    # Sort candidates to maximize the use of previous comparisons
    candidates = sort_candidates_by_history(candidates)

    min_idx = get_idx(candidates, 0)
    max_idx = get_idx(candidates, 1)

    if min_idx == max_idx:
        min_idx, max_idx = candidates[-1], candidates[-2]

    new_idx = plus(min_idx, max_idx)
    new_candidates = [i for i in candidates if i != min_idx and i != max_idx]
    new_candidates.append(new_idx)

    candidates = new_candidates

print("!", flush=True)
