#leaders in a array
#An element is leader if it is greater than all the elements to 
#its right side. And the rightmost element is always a leader. 
#For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.


#---------------------solution----------------------------------------------
#Scan all the elements from right to left in array and keep track of 
#maximum till now. When maximum changes it’s value, print it.

 
li=[int(x)for x in input().split(' ')]
n=len(li)
max=li[-1]
print(max)
for i in range(n-2,-1,-1):
	if li[i]>max:
		print(li[i])
		max=li[i]