import string
import collections
az = string.ascii_lowercase
S,T = input(),input()
atc = ("a","t","c","o","d","e","r")
flag = True
pea = 0
Sn = collections.defaultdict(int)
Tn = collections.defaultdict(int)

for i in T:
    Tn[i] += 1
for i in S:
    Sn[i] += 1

for i in az:
    if Sn[i] != Tn[i] and not i in atc  :
        
        flag = False
        break
    elif Sn[i] == Tn[i] and Sn[i] != 0:
        pea += Sn[i]
    elif i in atc and Sn[i] != Tn[i]: 
        pea += min(Sn[i],Tn[i])



a = Tn["@"] + Sn["@"]
if not flag:
    print("No")
elif pea + a >= len(S):
    print("Yes")
else:
    print("No")

