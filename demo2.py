#l r x vala hai 
'''n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
#print(list)
for _ in range(inputs):
	x, y, incr =input().split(' ')
	x=int(x)
	y=int(y)
	incr=int(incr)
	list[x-1] += incr
	print(list) 
    #print(y)
	list[y] -= incr;
	print(list)
max = x = 0
for i in list:
    x=x+i;
    if(max<x): max=x;
print(max(list))'''
#dp ka maxarray
def maxSubsetSum(arr):
	n = len(arr)
	dp = [0]*n
	dp[0] = arr[0]
	dp[1] = max(arr[1], dp[0])
	print(dp)
	for i in range(2,n):
		dp[i] = max(arr[i], dp[i-1], arr[i] + dp[i-2])
		print(dp)
	return dp[-1]
n=int(input())
a=[int(x)for x in input().split(' ')]
maxSubsetSum(a)


