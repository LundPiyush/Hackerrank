# A Dynamic Programming based Python Program for the Egg Dropping Puzzle 
INT_MAX = 32767

# Function to get minimum number of trials needed in worst 
# case with n eggs and k floors 
def eggDrop(n, k):
	#n=2(eggs)k=6(floors)
	# A 2D table where entery eggFloor[i][j] will represent minimum 
	# number of trials needed for i eggs and j floors. 
	eggFloor = [[0 for x in range(k+1)] for x in range(n+1)] 
	print(eggFloor)
	# We need one trial for one floor and0 trials for 0 floors 
	for i in range(1, n+1): 
		eggFloor[i][1] = 1
		#eggFloor[i][0] = 0
		#print(eggFloor)
	# We always need j trials for one egg and j floors. 
	for j in range(2, k+1): 
		eggFloor[1][j] = j 
		#print(eggFloor)
	# Fill rest of the entries in table using optimal substructure 
	# property 
	for i in range(2, n+1): 
		for j in range(2, k+1): 
			eggFloor[i][j] = INT_MAX 
			for x in range(1, j+1):
				print(eggFloor)
				res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
				if res < eggFloor[i][j]: 
					eggFloor[i][j] = res 
				print('fi',eggFloor)
	# eggFloor[n][k] holds the result 
	return eggFloor[n][k] 

# Driver program to test to pront printDups 
n = 2
k = 6
print("Minimum number of trials in worst case with " + str(n) + "eggs and "
	+ str(k) + " floors is " + str(eggDrop(n, k))) 

# This code is contributed by Bhavya Jain 
'''
def egg_dropping(eggs,floors):
	dp=[[0 for i in range(floors)]for i in range(1,eggs+1)]
	print(dp)
	for i in range(floors):
		dp[0][i]=i+1
	print(dp)
	#for i in range(eggs)
	for i in range(1,eggs):
		for j in range(floors):
			for k in range(1,floors):
				if i>j:
					dp[i][j]=dp[i-1][j]
				else:
					ans=1+max(dp[i-1][k-1],dp[i][j-k])
					if ans<dp[i][j]:
						dp[i][j]=ans
				print(dp)





eggs=int(input())
floors=int(input())
egg_dropping(eggs,floors)'''