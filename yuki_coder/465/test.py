# [テスターの仕様]
#   - 入力として「テストケースの入力 → あなたの出力」の順に受け取る．
#   - 出力が valid かどうか (valid でない場合はその原因)，および得点を出力する．
#   - X+1 行出力されない場合の挙動は未定義なので注意すること．
#   - 余分な出力があるかどうかはチェックされない．(実際の提出でも，余分な出力はチェックされない)

import sys
import math


def WrongAnswer(str):
    print("Wrong Answer (" + str + ")")
    sys.exit(0)


# Step 1. テストケースの入力を受け取る
N = int(input())
A = [0] * (N + 1)
B = [0] * (N + 1)
for i in range(1, N + 1):
    A[i], B[i] = map(int, input().split())

# Step 2. あなたの出力を受け取る
X = int(input())
if X < 0 or X > 50:
    WrongAnswer("X is out of range")
U = [0] * (X + 1)
V = [0] * (X + 1)
for i in range(1, X + 1):
    U[i], V[i] = map(int, input().split())
    if U[i] == V[i]:
        WrongAnswer("U[i] and V[i] are same")
    elif U[i] < 1 or U[i] > N:
        WrongAnswer("U[i] is out of range")
    elif V[i] < 1 or V[i] > N:
        WrongAnswer("V[i] is out of range")

# Step 3. シミュレーションを行う
for i in range(1, X + 1):
    avgA = (A[U[i]] + A[V[i]]) // 2
    avgB = (B[U[i]] + B[V[i]]) // 2
    A[U[i]] = avgA
    A[V[i]] = avgA
    B[U[i]] = avgB
    B[V[i]] = avgB

# Step 4. 出力
ErrorA = abs(500000000000000000 - A[1])
ErrorB = abs(500000000000000000 - B[1])
Score = (int)(2000000.0 - 100000.0 * math.log10(1.0 * max(ErrorA, ErrorB) + 1.0))
if ErrorA == 0 and ErrorB == 0:
    Score = 2000050 - X
print("Accepted!")
print("Error of A[1] = " + str(ErrorA))
print("Error of B[1] = " + str(ErrorB))
print("Score = " + str(Score))
