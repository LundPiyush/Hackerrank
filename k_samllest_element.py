#kth smallest element
import sys
t=int(input())
for i in range(t):
	n=int(input())
	arr=[int(x)for x in input().split()]
	k=int(input())
	a=k
	while a>1:
		arr[arr.index(min(arr))]=sys.maxsize
		a=a-1
		print(arr)
	print(min(arr))
#above method giving TLE
