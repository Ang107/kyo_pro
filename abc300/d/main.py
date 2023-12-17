import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((0, -1), (0, 1), (-1, 0), (1, 0))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照
    

n = II()

N = int(((10**12) / 12)**0.5) + 1

A=list(range(2,N+1))
p=list()
while A[0]**2<=N:
	tmp=A[0]
	p.append(tmp)
	A=[e for e in A if e%tmp!=0]

p += A
ans = 0
for i in range(len(p)):
	for j in range(i+1,len(p)):
		if p[i] ** 2 * p[j] > n:
			break
		for k in range(j+1,len(p)):
			if p[i] ** 2 * p[j] * p[k] ** 2 <= n:
				ans += 1
				# print(p[i],p[j],p[k],p[i] ** 2 + p[j] * p[k] ** 2)
			else:
				break

print(ans)


# num = len(p) + temp + 1
# print(temp,p[temp],len(p),num)
# ans = num * (num-1) * (num-2) / 6
# print(ans)
	
# print(p)

# print(len(list(combinations(p,3))))

# ans = 0
# for a,b,c in combinations(p,3):
# 	if 300 <= a ** 2 * b * c ** 2 <= n:
# 		print(a ** 2 * b * c ** 2 )
# 		ans += 1

# print(ans)
		
