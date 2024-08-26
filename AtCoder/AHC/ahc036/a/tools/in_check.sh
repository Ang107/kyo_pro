cd /mnt/c/Users/kosuk/Desktop/kyo_pro/AtCoder/AHC/ahc036/a/tools
for i in `seq 0 499`;
do 
j=$(printf "%04d\n" "${i}")
pypy3 a.py < in/${j}.txt >> tmp.txt
done