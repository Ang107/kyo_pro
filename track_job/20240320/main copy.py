def create_solution(
    step: int,
    n: int,
    m: int,
    q: int,
    query1: list[int],
    query2: list[int],
    query3: list[int],
) -> list[int]:
    # https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
    import math
    from bisect import bisect_left, bisect_right
    from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional

    T = TypeVar("T")

    class SortedMultiset(Generic[T]):
        BUCKET_RATIO = 16
        SPLIT_RATIO = 24

        def __init__(self, a: Iterable[T] = []) -> None:
            "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
            a = list(a)
            n = self.size = len(a)
            if any(a[i] > a[i + 1] for i in range(n - 1)):
                a.sort()
            num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
            self.a = [
                a[n * i // num_bucket : n * (i + 1) // num_bucket]
                for i in range(num_bucket)
            ]

        def __iter__(self) -> Iterator[T]:
            for i in self.a:
                for j in i:
                    yield j

        def __reversed__(self) -> Iterator[T]:
            for i in reversed(self.a):
                for j in reversed(i):
                    yield j

        def __eq__(self, other) -> bool:
            return list(self) == list(other)

        def __len__(self) -> int:
            return self.size

        def __repr__(self) -> str:
            return "SortedMultiset" + str(self.a)

        def __str__(self) -> str:
            s = str(list(self))
            return "{" + s[1 : len(s) - 1] + "}"

        def _position(self, x: T) -> Tuple[List[T], int, int]:
            "return the bucket, index of the bucket and position in which x should be. self must not be empty."
            for i, a in enumerate(self.a):
                if x <= a[-1]:
                    break
            return (a, i, bisect_left(a, x))

        def __contains__(self, x: T) -> bool:
            if self.size == 0:
                return False
            a, _, i = self._position(x)
            return i != len(a) and a[i] == x

        def count(self, x: T) -> int:
            "Count the number of x."
            return self.index_right(x) - self.index(x)

        def add(self, x: T) -> None:
            "Add an element. / O(√N)"
            if self.size == 0:
                self.a = [[x]]
                self.size = 1
                return
            a, b, i = self._position(x)
            a.insert(i, x)
            self.size += 1
            if len(a) > len(self.a) * self.SPLIT_RATIO:
                mid = len(a) >> 1
                self.a[b : b + 1] = [a[:mid], a[mid:]]

        def _pop(self, a: List[T], b: int, i: int) -> T:
            ans = a.pop(i)
            self.size -= 1
            if not a:
                del self.a[b]
            return ans

        def discard(self, x: T) -> bool:
            "Remove an element and return True if removed. / O(√N)"
            if self.size == 0:
                return False
            a, b, i = self._position(x)
            if i == len(a) or a[i] != x:
                return False
            self._pop(a, b, i)
            return True

        def lt(self, x: T) -> Optional[T]:
            "Find the largest element < x, or None if it doesn't exist."
            for a in reversed(self.a):
                if a[0] < x:
                    return a[bisect_left(a, x) - 1]

        def le(self, x: T) -> Optional[T]:
            "Find the largest element <= x, or None if it doesn't exist."
            for a in reversed(self.a):
                if a[0] <= x:
                    return a[bisect_right(a, x) - 1]

        def gt(self, x: T) -> Optional[T]:
            "Find the smallest element > x, or None if it doesn't exist."
            for a in self.a:
                if a[-1] > x:
                    return a[bisect_right(a, x)]

        def ge(self, x: T) -> Optional[T]:
            "Find the smallest element >= x, or None if it doesn't exist."
            for a in self.a:
                if a[-1] >= x:
                    return a[bisect_left(a, x)]

        def __getitem__(self, i: int) -> T:
            "Return the i-th element."
            if i < 0:
                for a in reversed(self.a):
                    i += len(a)
                    if i >= 0:
                        return a[i]
            else:
                for a in self.a:
                    if i < len(a):
                        return a[i]
                    i -= len(a)
            raise IndexError

        def pop(self, i: int = -1) -> T:
            "Pop and return the i-th element."
            if i < 0:
                for b, a in enumerate(reversed(self.a)):
                    i += len(a)
                    if i >= 0:
                        return self._pop(a, ~b, i)
            else:
                for b, a in enumerate(self.a):
                    if i < len(a):
                        return self._pop(a, b, i)
                    i -= len(a)
            raise IndexError

        def index(self, x: T) -> int:
            "Count the number of elements < x."
            ans = 0
            for a in self.a:
                if a[-1] >= x:
                    return ans + bisect_left(a, x)
                ans += len(a)
            return ans

        def index_right(self, x: T) -> int:
            "Count the number of elements <= x."
            ans = 0
            for a in self.a:
                if a[-1] > x:
                    return ans + bisect_right(a, x)
                ans += len(a)
            return ans

    from collections import deque, defaultdict

    result = []
    q1, q2, q3 = query1, query2, query3
    # if step == 1:
    #     # 地域:総数
    #     pokemon_sum = [0] * n
    #     # 地域:ポケモンの名前：数
    #     pokemon_syurui = [[0] * m for _ in range(n)]
    #     for i, j, k in zip(q1, q2, q3):
    #         if k != -1:
    #             i, j = i - 1, j - 1
    #             pokemon_sum[i] += k
    #             pokemon_syurui[i][j] += k
    #         elif k == -1:
    #             i = i - 1
    #             cnt = 0
    #             for p in range(n):
    #                 if (
    #                     pokemon_sum[p] != 0
    #                     and pokemon_syurui[p][i] * 100 >= j * pokemon_sum[p]
    #                 ):
    #                     cnt += 1
    #             result.append(cnt)
    #     return result
    # elif step == 2:
    #     # 地域:総数
    #     pokemon_sum = defaultdict(int)
    #     # 地域:ポケモンの名前：数
    #     pokemon_syurui = defaultdict(lambda: defaultdict(int))
    #     for i, j, k in zip(q1, q2, q3):
    #         if k != -1:
    #             i, j = i - 1, j - 1
    #             pokemon_sum[i] += k
    #             pokemon_syurui[i][j] += k
    #         elif k == -1:
    #             i = i - 1
    #             cnt = 0
    #             for p in pokemon_sum:
    #                 if pokemon_syurui[p][i] * 100 >= j * pokemon_sum[p]:
    #                     cnt += 1
    #             result.append(cnt)
    #     return result

    # if step == 3:
    #     # 地域:総数
    #     pokemon_sum = defaultdict(int)
    #     # 地域:ポケモンの名前：数
    #     pokemon_syurui = defaultdict(lambda: defaultdict(int))
    #     # ポケモンiの割合がj以上の地域の種類
    #     pokemon_wariai = [[set() for _ in range(101)] for _ in range(2)]
    #     for i, j, k in zip(q1, q2, q3):
    #         if k != -1:
    #             i, j = i - 1, j - 1
    #             pokemon_sum[i] += k
    #             pokemon_syurui[i][j] += k
    #             wariai = 100 * pokemon_syurui[i][j] / pokemon_sum[i]
    #             other_wariai = 100 - wariai
    #             for p in range(int(wariai) + 1):
    #                 pokemon_wariai[j][p].add(i)
    #             if m == 2:
    #                 for p in range(100, int(other_wariai), -1):
    #                     pokemon_wariai[(j + 1) % 2][p].discard(i)
    #             for p in range(m):
    #                 pokemon_wariai[p][0].add(i)

    #         elif k == -1:
    #             i = i - 1
    #             result.append(len(pokemon_wariai[i][j]))
    #     return result

    # TODO: Implement this function

    if True:
        # 地域:総数
        pokemon_sum = defaultdict(int)

        pokemon_num_in_area = defaultdict(lambda: defaultdict(int))
        # エリアに存在するポケモンの種類
        pokemon_syurui_in_area = defaultdict(lambda: set())

        pokemon_has_area = defaultdict(set)

        for i, j, k in zip(q1, q2, q3):
            if k != -1:
                area, pokemon = i - 1, j - 1
                pokemon_has_area[pokemon].add(area)

        syori2_pokemon = set()
        for pokemon, area in pokemon_has_area.items():
            if len(area) <= 1000:
                syori2_pokemon.add(pokemon)

        SL = defaultdict(SortedMultiset)
        result = []
        cnt = 0
        for i, j, k in zip(q1, q2, q3):
            # print(SL)
            if k != -1:
                area, pokemon = i - 1, j - 1
                if pokemon in syori2_pokemon:

                    # if pokemon_sum[area] > 0:
                    #     wariai = (
                    #         100
                    #         * pokemon_num_in_area[pokemon][area]
                    #         // pokemon_sum[area]
                    #     )
                    #     SL[pokemon].discard(wariai)
                    pokemon_num_in_area[pokemon][area] += k
                    pokemon_sum[area] += k
                    # wariai = (
                    #     100 * pokemon_num_in_area[pokemon][area] // pokemon_sum[area]
                    # )
                    # SL[pokemon].add(wariai)

                    for p in pokemon_syurui_in_area[area]:
                        if p != pokemon:
                            wariai = (
                                100
                                * pokemon_num_in_area[p][area]
                                // (pokemon_sum[area] - k)
                            )
                            SL[p].discard(wariai)
                            wariai = (
                                100 * pokemon_num_in_area[p][area] // pokemon_sum[area]
                            )
                            SL[p].add(wariai)
                else:
                    pokemon_syurui_in_area[area].add(pokemon)

                    if pokemon_sum[area] > 0:
                        wariai = (
                            100
                            * pokemon_num_in_area[pokemon][area]
                            // pokemon_sum[area]
                        )
                        SL[pokemon].discard(wariai)
                    pokemon_num_in_area[pokemon][area] += k
                    pokemon_sum[area] += k
                    wariai = (
                        100 * pokemon_num_in_area[pokemon][area] // pokemon_sum[area]
                    )
                    SL[pokemon].add(wariai)

                    for p in pokemon_syurui_in_area[area]:
                        if p != pokemon:
                            wariai = (
                                100
                                * pokemon_num_in_area[p][area]
                                // (pokemon_sum[area] - k)
                            )
                            SL[p].discard(wariai)
                            wariai = (
                                100 * pokemon_num_in_area[p][area] // pokemon_sum[area]
                            )
                            SL[p].add(wariai)

            elif k == -1:
                pokemon = i - 1
                if j == 0:
                    result.append(len(pokemon_sum))
                else:
                    if pokemon in syori2_pokemon:
                        cnt = 0
                        for area, pokemon_num in pokemon_num_in_area[pokemon].items():
                            if j <= 100 * pokemon_num / pokemon_sum[area]:
                                cnt += 1
                    else:
                        cnt = len(SL[pokemon]) - SL[pokemon].index(j)

                    result.append(cnt)

        return result


# print(
#     create_solution(4, 2, 3, 5, [1, 1, 1, 2, 1], [1, 2, 50, 50, 0], [6, 4, -1, -1, -1])
# )
