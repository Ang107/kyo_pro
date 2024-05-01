import sys

def Input(num):
    global x,y1,y2
    x = []
    y1,y2 = [],[]
    temp = 0
    for i in range(num+1):
        if i != 0:
            n,p,q = map(int,input().split())
            # print(n,p,q)
            x.append(n)
            y1.append(p/(p+q))
            y2.append(q/(p+q))
            temp += q/(p+q)/num
        else:
            input()
    print(f"new:{(temp*100)}%")
            



def Output():
    global x,y1,y2
    import numpy as np
    import matplotlib.pyplot as plt

    x,y1,y2 = map(np.array,(x,y1,y2))

    
    plt.bar(x,y1,label="old")
    plt.bar(x,y2,label="new",bottom=y1)
    plt.savefig(f'score/glaph.jpg')


def main():
    File_num = sys.argv[1]
    Input(int(File_num))
    Output()

if __name__ == "__main__":
    main()