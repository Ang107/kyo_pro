#コンテスト番号
contest_num=$(printf "%03d\n" "34")

#各自パスの変更が必要
cd /mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc0${contest_num}/a/

#フォルダを作る
mkdir -p out score err best_out best_err

#何番から何番まで？
start=0;last=10;

# ans_old=0;
# ans_new=0;

for d in `seq ${start} ${last}`;
do
    j=$(printf "%04d\n" "${d}")
    echo $j;
    
    #--profiler:on --stackTrace:on

    nim cpp -r -d:release  --opt:speed --multimethods:on --warning[SmallLshouldNotBeUsed]:off  --hints:off "/mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc${contest_num}/a/best.nim" < in/${j}.txt > best_out/${j}.txt 2> best_err/${j}.txt

    # nim cpp -r -d:release  --opt:speed --multimethods:on --warning[SmallLshouldNotBeUsed]:off  --hints:off "/mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc${contest_num}/a/greed_1.nim" < in/${j}.txt > out/${j}.txt 2> err/${j}.txt
    # pypy3  "/mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc${contest_num}/a/test.py" < out/${j}.txt >> score/score.txt
done

