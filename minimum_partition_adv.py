#Partition a set into two subsets such that the difference 
#of subset sums is minimum
#Given a set of integers, the task is to divide it into two sets S1 and S2 
#such that the absolute difference between their sums is minimum.


'''
solution
follow thw minimum_partition.py method addition is to find the diif.

To find Minimum sum difference, we have to find j such 
that Min{sum - j*2  : dp[n][j]  == 1 } 
    where j varies from 0 to sum/2

The idea is, sum of S1 is j and it should be closest
to sum/2, i.e., 2*j should be closest to sum.'''

import sys
def find_min_diff(arr):

	sum1=sum(arr)
	n=len(arr)
	li=[[False for i in range(sum1+1)]for i in range(n)]
	
	for i in range(n):
		li[i][0]=True
	for j in range(sum1+1):
		if arr[0]==j:
			li[0][j]=True
	
	for i in range(n):
		for j in range(sum1+1):
			if j>=arr[i]:
				li[i][j]=li[i-1][j] or li[i-1][j-arr[i]]
			else:
				li[i][j]=li[i-1][j]
		print(li)
		diff=sys.maxsize
		s=sum1//2
		for j in range(s,-1,-1):
			print(j,n-1)
			if li[n-1][j]==True:
				diff=sum1-2*j
				print(diff)
				break 
	print(diff)
arr=[int(x)for x in input().split(' ')]
find_min_diff(arr)
			
			
			
			
		
	