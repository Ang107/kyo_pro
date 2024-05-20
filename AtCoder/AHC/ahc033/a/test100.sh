#各自パスの変更が必要
cd /mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc033/a/

#コンパイル(c++の時のみ) ファイルの場所は変更してください。

#フォルダを作る
# mkdir -p output score

#何番から何番まで？
start=0;last=100;

# ans_old=0;
# ans_new=0;

for d in `seq ${start} ${last}`;
do
    j=$(printf "%04d\n" "${d}")
    echo $j;



    nim cpp -r -d:release --opt:speed --multimethods:on --warning[SmallLshouldNotBeUsed]:off  --hints:off "/mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc033/a/main.nim" < in/${j}.txt > out/nim${j}.txt

  



done

