#tushar roy code
import sys

###################################################################################
# Given coins of certain denominations with infinite supply find minimum number of coins it takes to
# form given total

# It returns sys.maxint - 1 if no solution is possible
def min_coin_bottom_up(total, coins):
    T = [sys.maxsize - 1 for x in range(total + 1)]
	#R = [-1 for x in range(total + 1)]
    print(T)
	#print(R)
    T[0] = 0
	#print(T)
    for j in range(len(coins)):
        for i in range(1, total + 1):
			#print("i,j",i,j)
            if i >= coins[j]:
				#print("i,coins[j]",i,coins[j])
                if T[i - coins[j]] + 1 < T[i]:
				#print("t[i]",T[i])
                    T[i] = min(1 + T[i - coins[j]],T[i])
					#R[i] = j
                print(T)
			
	#print_coin_combination(R, coins)
    return T[-1]


'''def print_coin_combination(R, coins):
	if R[len(R) - 1] == -1:
		print("No solution possible")
		return

	start = len(R) - 1
	print("Coins used ")
	while start != 0:
		j = R[start]
		print(coins[j])
		start = start - coins[j]

'''
if __name__ == '__main__':
	total =4
	coins = [1,2,3]
	bottom_up_result = min_coin_bottom_up(total, coins)
	print("Bottom up result " + str(bottom_up_result))


##########################################################








#geeks for geeks code
'''# A Dynamic Programming based Python3 program to 
# find minimum of coins to make a given change V 
import sys 

# m is size of coins array (number of 
# different coins) 
def minCoins(coins, m, V): 
	#coins is list of coins given ,m is length of the coins list,V is total sum
	# table[i] will be storing the minimum 
	# number of coins required for i value. 
	# So table[V] will have result 
	table = [0 for i in range(V + 1)] 
	print(table)
	# Base case (If given value V is 0) 
	table[0] = 0

	# Initialize all table values as Infinite 
	for i in range(1, V + 1): 
		table[i] = sys.maxsize 

	# Compute minimum coins required 
	# for all values from 1 to V 
	for i in range(1, V + 1): 
		
		# Go through all coins smaller than i 
		for j in range(m): 
			if (coins[j] <= i): 
				sub_res = table[i - coins[j]] 
				if (sub_res != sys.maxsize and
					sub_res + 1 < table[i]): 
					table[i] = sub_res + 1
	return table[V] 

# Driver Code 
if __name__ == "__main__": 

	coins = [9, 6, 5, 1] 
	m = len(coins) 
	V = 0
	print("Minimum coins required is ",minCoins(coins, m, V)) 

# This code is contributed by ita_c 
'''