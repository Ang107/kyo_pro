import sys
import collections
from collections import deque
from copy import deepcopy
from decimal import Decimal, getcontext


sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

n = int(input())
pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

getcontext().prec = len(pi)
npi = Decimal(pi)
  # 切り捨てる桁数

truncated_num = npi.quantize(Decimal('1e-{0}'.format(n)), rounding="ROUND_DOWN")
print(truncated_num)

#a,b = map(int,input().split())
    

    
    


