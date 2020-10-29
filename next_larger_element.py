#code
t=int(input())
for j in range(t):
	n=int(input())
	li=[int(x)for x in input().split()]
	flag=0
	for i in range(len(li)):
		next=-1
		for j in range(i+1,len(li),1):
			if li[j]>li[i]:
				next=li[j]
				break
		print(next,end=" ")
	
	#giving TLE