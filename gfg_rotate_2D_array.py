#rotate a 2-D Array using extra space
import numpy as np
for i in range(2):
	li=[]
	n=int(input())
	for j in range(n):
		a=[]
		for k in range(n):
			a.append(int(input()))
			print(a)
		li.append(a)
		
	print(li)
	for c in range(0,n):
		for r in range(n-1,-1,-1):
			print(li[r][c],end=' ')
	print()