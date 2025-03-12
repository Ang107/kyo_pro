from scipy.special import comb
import pandas as pd
import matplotlib.pyplot as plt


def bell(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        res = 0
        for k in range(n):
            res += comb(n - 1, k, exact=True) * bell(k)
        return res


def main(n):
    df = []
    for i in range(n + 1):
        df.append([i, bell(i)])
    df = pd.DataFrame(df, columns=["n", "bell"])
    df.to_csv("bell.csv")

    fig, ax = plt.subplots()
    ax.plot(df["n"], df["bell"], marker="o")
    ax.set_xlabel("n")
    ax.set_ylabel("Bell number")
    fig.tight_layout()
    fig.savefig("bell.jpg", dpi=300)
    return


if __name__ == "__main__":
    main(n=10)
