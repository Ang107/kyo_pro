#各自パスの変更が必要
cd C:\\Users\\kosuk\\Desktop\\atcoder\\ahc028\\a\\tools

#コンパイル(c++の時のみ) ファイルの場所は変更してください。

#フォルダを作る
mkdir -p output score

#何番から何番まで？
start=0;last=10;

echo > score/score.txt
for d in `seq ${start} ${last}`;
do
    j=$(printf "%04d\n" "${d}")
    ##ここに実行コマンドを置く(以下はc++)　ファイルの場所は注意
    python3 main.py  < in/${j}.txt > output/a${j}.txt
    ##
    # "Score = " より後の文字列を抽出する（この部分は変わる可能性あり）
    # var=$(grep "Score = " ./output/${j}.txt | sed -e 's/[^0-9]//g')
    # ans=$(($ans+$var))

    # echo $j $var $var1 >> score/score.txt

    # echo $j $var;
done

# ans=$(($ans/($last-$start+1)))
# ans1=$(($ans1/($last-$start+1)))
# echo "Average Score" $ans $ans1;
# python3 make_glaph.py $(($last-$start+1)) < score/score.txt
