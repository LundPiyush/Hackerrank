def maxSubsetSum(a):
	n=len(a)
	max_sum=0
	for i in range(n-1):
		j=0
		while (i+j+2)<=n-1:
			subset_sum=sum(a[i:len(a):j+2])
			if subset_sum>max_sum:
				max_sum=subset_sum
			j=j+1
	print(max_sum)






n = int(input())
arr = list(map(int, input().rstrip().split()))
maxSubsetSum(arr)