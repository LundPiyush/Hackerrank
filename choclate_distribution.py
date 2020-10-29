#choclate distribtion prblm
import sys
t=int(input())
for i in range(t):
	n=int(input())
	c=[int(x)for x in input().split()]
	m=int(input())
	c.sort()
	min_diff=sys.maxsize
	i=0
	print(c)
	while i+m-1<n:
		diff=c[i+m-1]-c[i]
		if diff < min_diff:
			min_diff=diff
			#print(c[i+m-1],c[i])
		i=i+1
	print(min_diff)