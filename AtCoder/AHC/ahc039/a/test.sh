#コンテスト番号
contest_num=$(printf "%03d\n" "34")

#各自パスの変更が必要
cd /home/kosuke/projects/kyo_pro/AtCoder/AHC/ahc039/a/

#フォルダを作る
mkdir -p out score

#何番から何番まで？
start=0;last=100;

# ans_old=0;
# ans_new=0;

for d in `seq ${start} ${last}`;
do
    j=$(printf "%04d\n" "${d}")
    # echo $j;
    
    #--profiler:on --stackTrace:on

    nim cpp -r -d:release --hints:off --verbosity:0 --opt:speed --multimethods:on --warning[SmallLshouldNotBeUsed]:off "/home/kosuke/projects/kyo_pro/AtCoder/AHC/ahc039/a/main.nim" < in/${j}.txt > out/${j}.txt
    # pypy3  "/mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc${contest_num}/a/test.py" < out/${j}.txt >> score/score.txt
done

