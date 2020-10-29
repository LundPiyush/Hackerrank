#rod cutting 
n=8
val=[1,5]
dp=[[0 for i in range(n+1)]for j in range(1,n+1)]
for i in range(1,n):
	for j in range(1,n+1):
		if j>=i:
			dp[i][j]=max(dp[i-1][j],dp[i][j-i]+val[i])
			print(dp)
			
		else:
			dp[i][j]=dp[i-1][j]
			print(dp)
			exit()
print(dp)