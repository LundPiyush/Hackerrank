#0/1 knapsack 
def knapsack(wt,profit,capacity,n):
	c=[[0 for i in range(capacity+1)]for i in range(n+1)]
	print(c)
	for i in range(n+1): 
		for w in range(capacity+1):
			print(i,w)
			if i==0 or w==0: 
				c[i][w] = 0
				#print(c)
			elif wt[i-1] <= w:
				c[i][w] = max(profit[i-1] + c[i-1][w-wt[i-1]],  c[i-1][w])
				#print(c)
			else: 
				c[i][w] = c[i-1][w] 
				#print(c)
	print(c[-1][-1])
	
	
	
	
n=int(input())
capacity=int(input())
wt=[int(n)for n in input().split(' ')]
profit=[int(n)for n in input().split(' ')]
knapsack(wt,profit,capacity,n)