#equilibrium
#code
t=int(input())
for i in range(t):
	n=int(input())
	li=[int(x)for x in input().split()]
	total_sum=sum(li)
	left_sum,flag=0,0
	for i in range(len(li)):
		total_sum=total_sum-li[i]
		if total_sum==left_sum:
			print(i)
			flag=1
			break
		left_sum+=li[i]
		print(left_sum,total_sum)
	if flag!=1:
		print(-1)