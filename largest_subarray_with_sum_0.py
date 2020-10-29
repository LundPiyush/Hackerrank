#largest sub array with sum equal to zero
def maxLen(arr,n):
	max_len=0
	for i in range(n):
		sum=0
		for j in range(i,n):
			sum=sum+arr[j]
			if sum==0:
				max_len=max(max_len,j-i+1)