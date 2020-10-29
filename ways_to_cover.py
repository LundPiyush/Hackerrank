def cover_distance(n):
	count=[0]*(n+1)
	count[0]=1#to cover 0 distance there is 1 way
	count[1]=1# to cover 1 distance there is 1 way 
	count[2]=2# to cover 2 distance there are 2 ways (1+1)or (2)
	for i in range(3,n+1):
		count[i]=count[i-1]+count[i-2]+count[i-3]
	print(count[-1])
n=int(input())
cover_distance(n)

#prblm-u have to climb n stairs find the no of ways u can climb it 
#there are three types of stairs 0,1,2
#this is more of recursion while in recursion we add previous two, in this as
#there are three diff types we will add prev. three