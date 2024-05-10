print(sum(int(i) for i in str(int(hex(int(input())), base=36))))
print(int(str(int(hex(int(input())), base=36)), base=0))
print(
    sum(
        int(i)
        for i in str(
            sum(
                36**j
                * {
                    "0": 0,
                    "1": 1,
                    "2": 2,
                    "3": 3,
                    "4": 4,
                    "5": 5,
                    "6": 6,
                    "7": 7,
                    "8": 8,
                    "9": 9,
                    "A": 10,
                    "B": 11,
                    "C": 12,
                    "D": 13,
                    "E": 14,
                    "F": 15,
                    "x": 33,
                }[k]
                for j, k in enumerate(hex(int(input()))[::-1])
            )
        )
    )
)
