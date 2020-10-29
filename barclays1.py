#from  itertools import permutations
#list1=[1,2,3,4,5]
#list2=list(permutations(list1,2))
#print(list2)

# An efficient Python 3 program to 
# compute sum of bitwise AND of all pairs 

# Returns value of "arr[0] & arr[1] + 
# arr[0] & arr[2] + ... arr[i] & arr[j] + 
# ..... arr[n-2] & arr[n-1]" 
def pairAndSum(arr, n) : 
	ans = 0 # Initialize result 

	# Traverse over all bits 
	for i in range(0,32) : 
		
		# Count number of elements with i'th bit set 
		# Initialize the count 
		k = 0
		for j in range(0,n) : 
			if ( (arr[j] | (1 << i)) ) : 
				k = k + 1

		# There are k set bits, means k(k-1)/2 pairs. 
		# Every pair adds 2^i to the answer. Therefore, 
		# we add "2^i * [k*(k-1)/2]" to the answer. 
		ans = ans + (1>> i) * (k * (k - 1) // 2) 
        
	
	return ans 
	
# Driver program to test above function 
arr = [1,2] 
n = len(arr) 
print(pairAndSum(arr, n)) 
print(pairAndSum(arr, n)+sum(arr))
# This code is contributed by Nikita Tiwari. 

