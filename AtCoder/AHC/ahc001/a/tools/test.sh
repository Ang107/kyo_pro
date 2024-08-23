#コンテスト番号
contest_num=$(printf "%03d\n" "1")

#各自パスの変更が必要
cd /mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc${contest_num}/a/tools

#フォルダを作る
mkdir -p out score

#何番から何番まで？
start=0;last=0;

# ans_old=0;
# ans_new=0;

for d in `seq ${start} ${last}`;
do
    j=$(printf "%04d\n" "${d}")
    echo $j;
    
    #--profiler:on --stackTrace:on

    nim cpp -r -d:release  --opt:speed --multimethods:on --warning[SmallLshouldNotBeUsed]:off  --hints:off "/mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc${contest_num}/a/tools/main.nim" < in/${j}.txt > out/${j}.txt
    cargo run --release --bin vis in/${j}.txt out/${j}.txt
done    

