# Python3 program to find sub-array 
# Python3 program to find sub-array 
# having maximum sum of elements modulo m. 

# Return the maximum sum subarray mod m. 
def maxSubarray(arr, n, m): 

	x = 0
	prefix = 0
	maxim = 0

	S = set() 
	S.add(0)	 
	print(S)
	# Traversing the array. 
	for i in range(n): 

		# Finding prefix sum.
		print(arr)
		print("m",m)
		print("i",i)
		print(arr[i])
		print("prefix",prefix)
		prefix = (prefix + arr[i]) % m 
		#print("prefix",prefix)
		# Finding maximum of prefix sum. 
		maxim = max(maxim, prefix) 
		print("maxim",maxim)
		# Finding iterator poing to the first 
		# element that is not less than value 
		# "prefix + 1", i.e., greater than or 
		# equal to this value. 
		it = 0
		print(S)
		for i in S: 
			if print(i >= prefix + 1): 
				it = i 
		if (it != 0) : 
				maxim = max(maxim, prefix - it + m ) 

		# adding prefix in the set. 
		S.add(prefix) 

	return maxim 

# Driver Code 
arr = [3, 3, 9, 9, 5] 
n = 5
m = 7
print(maxSubarray(arr, n, m)) 

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
