Set1 = {1}
Set2 = {"a", "b", "c"}
Set3 = {"a", "b", "c", "a", "b", "c" }   #重複してると・・・？
Set4 = {(1,2),(2,1),(1,3)}   #要素にタプルを設定
Set5 = {}  #空の集合・・・？

print("Set1 :", Set1, type(Set1))
print("Set2 :", Set2, type(Set2))
print("Set3 :", Set3, type(Set3))
print("Set4 :", Set4, type(Set4))
print("Set5 :", Set5, type(Set5))

Set6 = set()

print("Set6 :", Set6, type(Set6))

i = 1   #iはint型
print(i,type(i))

i = "hello world!"     #iはstr型
print(i,type(i))

i = [1, 2, 3]     #iはlist型
print(i,type(i))

i = ("おはよう", "こんにちは", "こんばんは")    #iはtuple型
print(i,type(i))

i = {"B3":["Nabeta", "Yamazaki", "Hirayama"],"B2":["Shikamata", "Mazaki"], "B1":["Nakamura","Fujino", "Oohashi"]}    #iはdict型
print(i,type(i))

i = {1, 100, 10000, 1000000}    #iはset型
print(i,type(i))