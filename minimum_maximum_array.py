#minimum and maximum difference in an array
#to find min_diff and max_diff between any 2 elements present 
#at any position in an array
import sys
def min_max(arr,n):
	minimum=sys.maxsize
	maximum=0
	arr.sort()
	for i in range(n-1):
		minimum=min(minimum,arr[i+1]-arr[i])
		maximum=arr[-1]-arr[0]
	print(minimum)
	print(maximum)



arr=[int(x)for x in input().split(' ')]
n=len(arr)
min_max(arr,n)