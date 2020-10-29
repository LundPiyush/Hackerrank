'''#reverse in grps
def reverse_arr(li,n,k):
	left


t=int(input())
for j in range(t):
	n,k=input().split()
	n=int(n)
	k=int(k)
	li=[int(x)for x in input().split()]
	reverse_arr(li,n,k)'''
li=[3,2,5,8,5,9]
li1=[4,6,7,9,9,2]
li1,li=zip(*sorted(zip(li1,li)))#return a tupple
#jisko sort karna hai usko phlee likho
print(list(li))
print(li1)

# Python3 implementation this is to use itertools. 
# permutations as coded below: 
'''
from itertools import permutations 
def largest(l): 
	lst = [] 
	for i in permutations(l, len(l)): 
		# provides all permutations of the list values, 
		# store them in list to find max 
		lst.append("".join(map(str,i)))
		print(lst)
	return max(lst) 

print(largest([54, 546, 548, 60])) #Output 6054854654 

# This code is contributed by Raman Monga 
'''
'''
#jpmorgan ppt vala
n,k=input().split(',')
n=int(n,2)#convert the binary into int
k=int(k,2)	
a=n+k 
print(format(a,'b'))#printed format
'''
 


'''
#carrerup question
l=[1,4,2,6,8,9,5,67,67,55]
print(sorted(set(l))[-4])#fourth largest
print(sorted(set(l))[-2])#second largest'''