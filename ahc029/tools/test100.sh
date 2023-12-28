#各自パスの変更が必要
cd C:\Users\kosuk\Desktop\atcoder\ahc029\tools

#コンパイル(c++の時のみ) ファイルの場所は変更してください。

#フォルダを作る
mkdir -p output score

#何番から何番まで？
start=0;last=30;

ans=0;
ans1=0;
echo > score/score.txt
for d in `seq ${start} ${last}`;
do
    j=$(printf "%04d\n" "${d}")
    ##ここに実行コマンドを置く(以下はc++)　ファイルの場所は注意
    cargo run -r --bin tester python3 main.py ${j} < in/${j}.txt > output/${j}.txt
    ##
    # "Score = " より後の文字列を抽出する（この部分は変わる可能性あり）
    var=$(grep "Score = " ./output/${j}.txt | sed -e 's/[^0-9]//g')
    ans=$(($ans+$var))

    j=$(printf "%04d\n" "${d}")
    ##ここに実行コマンドを置く(以下はc++)　ファイルの場所は注意
    cargo run -r --bin tester python3 main2.py new${j} < in/${j}.txt > output/new${j}.txt
    ##
    # "Score = " より後の文字列を抽出する（この部分は変わる可能性あり）
    var1=$(grep "Score = " ./output/new${j}.txt | sed -e 's/[^0-9]//g')
    ans1=$(($ans1+$var1))
    echo $j $var $var1 >> score/score.txt

    # echo $j $var;
done

ans=$(($ans/($last-$start+1)))
ans1=$(($ans1/($last-$start+1)))
echo "Average Score" $ans $ans1;
python3 make_glaph.py $(($last-$start+1)) < score/score.txt
