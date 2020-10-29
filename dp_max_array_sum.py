#hackerank problem 



n=int(input())
a=[int(x)for x in input().split(' ')]
dp=[0]*n
dp[0]=a[0]
dp[1]=max(a[1],a[0])
print("first array")
print(dp)
for i in range(2,n):
	dp[i]=max(a[i],dp[i-1],a[i]+dp[i-2])
	print(dp)
print(dp[-1])


