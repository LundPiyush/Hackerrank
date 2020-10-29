n=int(input())

li=[int(n) for n in input().split(' ')]
d,m=input().split(' ')
d=int(d)
m=int(m)
count=0
cnt={}

#countTriplets(li, r)


for i in range(n):
	total=sum(li[i:i+m])
	if total==d:
		count+=1
	else:
		continue
print(count)



	#return count