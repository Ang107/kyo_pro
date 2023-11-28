# # coding: utf-8
# # 自分の得意な言語で
# # Let's チャレンジ！！
# n,x,f,s = map(int,input().split())

# def get_nonsleep(num):
#     temp = 0
#     while num > 0:
#         temp += num
#         num = max(num-f,0)
#     return temp
# time = 0
# now_x = x
# while n > 0:
    
#     if get_nonsleep(now_x) >=  n:
#         time += 1
#         n -= now_x
#         now_x -= f
#     elif get_nonsleep(min(x,now_x+s)) >= n:
#         time += 3
#         now_x = min(now_x+s,x)
        
#     elif x - now_x >= s:
#         time += 3
#         now_x = min(now_x+s,x)
#     else:
#         time += 1
#         n -= now_x
#         now_x -= f

# print(time)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n,x,f,s = map(int,input().split())

def get_nonsleep(num):
    temp = 0
    while num > 0:
        temp += num
        num = max(num-f,0)
    return temp

time = 0
now_x = x
while n > 0:
    
    if get_nonsleep(now_x) >=  n:
        print("w")
        time += 1
        n -= now_x
        now_x -= f
    elif get_nonsleep(min(x,now_x+s)) >= n:
        print("s")
        time += 3
        now_x = min(now_x+s,x)
        
    elif x - now_x >= s:
        print("s")
        time += 3
        now_x = min(now_x+s,x)
    else:
        print("w")
        time += 1
        n -= now_x
        now_x = max(now_x-f,0)

print(time)
