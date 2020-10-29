n,k=input().split()
n=int(n)
k=int(k)
li1=[]
sum=0
li=[int(n)for n in input().split()]
print(li)
li.sort()
print(li)
for i in range(len(li)):
	sum=sum+li[i]
	if sum<=k:
		li1.append(li[i])
	else:
		continue
print(len(li1))
