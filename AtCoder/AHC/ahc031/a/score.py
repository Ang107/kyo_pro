# score計算をするpythonファイル
# 入力ファイルと出力ファイルからスコアの計算


def Input1():
    W, D, N = map(int, input().split())
    A = []
    for _ in range(D):
        tmp = list(map(int, input().split()))
        A.append(tmp)
    return W, D, N, A


def Input2(D, N):
    ans = []
    for _ in range(D):
        tmp = []
        for _ in range(N):
            tmp.append(list(map(int, input().split())))
        ans.append(tmp)
    return ans


def get_score(D, N, A, ans):

    pass


def main():
    W, D, N, A = Input1()
    ans = Input2(D, N)
    score = get_score(D, N, A, ans)
    print(score)


if __name__ == "__main__":
    main()
