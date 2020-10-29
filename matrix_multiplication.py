#matrix chain multiplication
#decide the order in which the matrix should be multplied so that cost is minimum
def matrix_multiplication(arr):
	n=len(arr)
	dp=[[0 for i in range(n)]for i in range(n)]

	for i in range(n):
		dp[i][i]=0
	#print(dp)
	for L in range(1,n-1):
		for i in range(1,n-L):
			dp[i][i+L]=min(dp[i+1][i+L]+arr[i-1]*arr[i]*arr[i+L],
			dp[i][i+L-1]+arr[i-1]*arr[i+L-1]*arr[i+L])
	print(dp[1][n-1])
	
arr=[int(x)for x in input().split(' ')]
matrix_multiplication(arr)
