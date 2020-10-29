#minimum partition
#Partition problem is to determine whether a given set can be partitioned 
#into two subsets such that the sum of elements in both subsets is same.


#solution

'''Following are the two main steps to solve this problem:
1) Calculate sum of the array. If sum is odd, there cannot be two subsets 
   with equal sum, so return false.
2) If sum of array elements is even, calculate sum/2 and find a subset 
   of array with sum equal to sum/2.

The first step is simple. The second step is crucial, it can be solved 
either using recursion or Dynamic Programming.
'''


def minimum_partition(arr):
	s=sum(arr)
	if s%2!=0:
		return False
	s=s//2
	print(s)
	n=len(arr)
	li=[[False for i in range(s+1)]for i in range(n)]
	print(li)
	
	for i in range(n):
		li[i][0]=True
	for j in range(s+1):
		if arr[0]==j:
			li[0][j]=True
	for i in range(n):
		for j in range(s+1):
			if j<arr[i]:
				li[i][j]=li[i-1][j]
			else:
				li[i][j]=li[i-1][j] or li[i-1][j-arr[i]]
	print(li)
	return li[-1][-1]






arr=[int(x)for x in input().split(' ')]
print(minimum_partition(arr))