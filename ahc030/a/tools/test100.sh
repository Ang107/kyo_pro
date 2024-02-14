#各自パスの変更が必要
cd /mnt/c/Users/kosuk/Desktop/atcoder/ahc030/a/tools

#コンパイル(c++の時のみ) ファイルの場所は変更してください。

#フォルダを作る
mkdir -p output score

#何番から何番まで？
start=0;last=30;

ans_old=0;
ans_new=0;

for d in `seq ${start} ${last}`;
do
    j=$(printf "%04d\n" "${d}")
    ##ここに実行コマンドを置く(以下はc++)　ファイルの場所は注意
    # cargo run 2> score/score_old.txt -r --bin tester  pypy3 main1.py < in/${j}.txt > output/${j}.txt
    cargo run 2> score/score_new.txt -r --bin tester  pypy3 main.py < in/${j}.txt > output/new_${j}.txt    
    #"Score = " より後の文字列を抽出する（この部分は変わる可能性あり）
    # var=$(grep "Score = " ./score/score_old.txt | sed -e 's/[^0-9]//g')
    # ans_old=$(($ans_old+$var))
    var1=$(grep "Score = " ./score/score_new.txt | sed -e 's/[^0-9]//g')
    ans_new=$(($ans_new+$var1))
    echo "${j} old :${var} new :${var1}";
done


# ans_old=$(($ans_old/($last-$start+1)))
# 0~30 43ぐらい
ans_new=$(($ans_new/($last-$start+1)))

echo "Average Score" old: $ans_old new: $ans_new;

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
