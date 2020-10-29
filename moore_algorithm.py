# Python 3 program to find if 
# any element appears more than 
# n/3. 
import sys 

def appearsNBy3(arr, n): 

	#return arr.count(a)
	count1 = 0
	count2 = 0
	first = sys.maxsize 
	second = sys.maxsize 
	
	for i in range(0, n): 

		# if this element is 
		# previously seen, 
		# increment count1. 
		if (first == arr[i]): 
			count1 += 1
			print(first)
		# if this element is 
		# previously seen, 
		# increment count2. 
		elif (second == arr[i]): 
			count2 += 1
			print(second)
		elif (count1 == 0): 
			count1 += 1
			first = arr[i] 
			print(first)
		elif (count2 == 0): 
			count2 += 1
			second = arr[i] 
			print(second)

		# if current element is 
		# different from both 
		# the previously seen 
		# variables, decrement 
		# both the counts. 
		else: 
			count1 -= 1
			count2 -= 1
		
	

	count1 = 0
	count2 = 0

	# Again traverse the array 
	# and find the actual counts. 
	for i in range(0, n): 
		if (arr[i] == first): 
			count1 += 1

		elif (arr[i] == second): 
			count2 += 1
	

	if (count1 > n / 3): 
		return first 

	if (count2 > n / 3): 
		return second 

	return -1

# Driver code 
arr = [1,3,2,2,2,1 ] 
n = len(arr) 
print("ans",appearsNBy3(arr, n)) 

# This code is contributed by 
# Smitha 
