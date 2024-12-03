import sys

for i in range(100):
    data = []
    with open(f"in/{i:04}.txt", "r") as file:
        sys.stdin = file
        n, t, sig = map(int, input().split())
        in_hw = [list(map(int, input().split())) for _ in range(n)]
        act_hw = [list(map(int, input().split())) for _ in range(n)]
        with open(f"actual/{i:04}.txt", "w", encoding="utf-8") as ofile:
            for i, j in act_hw:
                ofile.write(f"{i} {j}\n")
