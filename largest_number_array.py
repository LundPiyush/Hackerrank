#largest number
from itertools import permutations
def largest(arr):
	l=[]
	for i in permutations(arr,len(arr)):
		l.append("".join(map(str,i)))
		#print(l)
	print(max(l))
t=int(input())

for i in range(t):
	arr=[int(x)for x in input().split()]
	largest(arr)