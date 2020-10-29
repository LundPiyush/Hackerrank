#cutting rod 
#given various prices of rod we have to cut a rod of length n such 
#that total profit is maximum
def cutting_rod(length_rod,prices):
	dp=[[1 for i in range(length_rod+1)]for i in range(len(prices)+1)]
	print(dp)
	for i in range(0,len(prices)+1):
		dp[i][0]=0
	#print(dp)
	for i in range(1,len(prices)+1):
		for j in range(1,length_rod+1):
			#print(i,j)
			if j>=i:
				dp[i][j]=max(dp[i-1][j],dp[i][j-i]+prices[i-1])
				print("if",dp)
			else:
				dp[i][j]=dp[i-1][j]
				print("else",dp)

	print(dp[-1][-1])		



rod_length=int(input())
prices=[int(x)for x in input().split(' ')]
cutting_rod(rod_length,prices)