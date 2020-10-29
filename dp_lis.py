#LIS
n=int(input())
li=[int(x)for x in input().split()]
lis=[1]*n
ans=[0]*n
for i in range(1,n):
	for j in range(0,i):
		if li[i]>li[j] and lis[i]<=lis[j]+1:
			lis[i]=lis[j]+1
			ans[i]=j
print("maximum length",max(lis))
print(ans)
a=li.index(max(li))
print(ans[a])	