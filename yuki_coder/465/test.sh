#各自パスの変更が必要
cd /mnt/c/Users/kosuk/Desktop/atcoder/yuki_coder/465

#コンパイル(c++の時のみ) ファイルの場所は変更してください。

#フォルダを作る
mkdir -p output score

#何番から何番まで？
start=0;last=49;



for d in `seq ${start} ${last}`;
do
    j=$(printf "%03d\n" "${d}")

    pypy3  main.py < in/in${j}.txt  



done



    # j=$(printf "%04d\n" "${d}")
    # ##ここに実行コマンドを置く(以下はc++)　ファイルの場所は注意
    # cargo run -r --bin tester python3 main2.py new${j} < in/${j}.txt > output/new${j}.txt
    # ##
    # # "Score = " より後の文字列を抽出する（この部分は変わる可能性あり）
    # var1=$(grep "Score = " ./output/new${j}.txt | sed -e 's/[^0-9]//g')
    # ans1=$(($ans1+$var1))
    # echo $j $var $var1 >> score/score.txt

    # echo $j $var;



# ans1=$(($ans1/($last-$start+1)))
# python3 make_glaph.py $(($last-$start+1)) < score/score.txt
