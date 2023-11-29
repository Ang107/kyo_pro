#回文か判定O(n/2)
def is_Kaibun(s1: str) -> bool: 
    for i in range(len(s1)//2):
        if s1[i] == s1[-i - 1]:
            pass
        else:
            return False
    return True

#文字の差分を取得(文字列長が異なる場合False)
def get_str_difference(s1: str,s2: str) -> int :
    if len(s1) != len(s2):
        return False
    else:
        temp = 0
        for i,j in zip(s1,s2):
            if i != j:
                temp += 1
        return temp

