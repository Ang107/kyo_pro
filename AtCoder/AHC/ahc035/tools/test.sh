#コンテスト番号
contest_num=$(printf "%03d\n" "35")

#各自パスの変更が必要
cd /mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc${contest_num}/tools

#フォルダを作る
mkdir -p out score err

#何番から何番まで？
start=0;last=10;


# スコアリストの初期化
scores=()

# ループでテストを実行
for d in $(seq ${start} ${last}); do
    j=$(printf "%04d\n" "${d}")
    echo $j
    
    # コマンドを実行し、出力とエラーログを保存
    cargo run -r --bin tester nim cpp -r -d:release --opt:speed --multimethods:on --warning[SmallLshouldNotBeUsed]:off --hints:off "/mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc${contest_num}/tools/main.nim" < in/${j}.txt > out/${j}.txt 2> err/${j}.txt
    
    # err/txtからスコアを抽出
    score=$(grep 'Score =' err/${j}.txt | awk '{print $3}')
    echo "Extracted Score: $score"
    
    # スコアをリストに追加
    scores+=($score)
done

# スコアの合計を計算
total=0
for score in "${scores[@]}"; do
    total=$(awk "BEGIN {print $total+$score}")
done

# スコアの平均を計算
average=$(awk "BEGIN {print $total / ${#scores[@]}}")
echo "Average Score: $average"