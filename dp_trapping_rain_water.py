#water accumulation
li=[int(x)for x in input().split(' ')]
'''current=1
end=len(li)-1
a=li[0]

ans=0
while current<=end:
	if li[current]>=a:
		
		b=li.index(li[current])
		c=li.index(a)
		print(b,c)
		ans+=min(a,li[current])*(b-c-1)-sum(li[c+1:b])
		a=li[current]
	current+=1
print(ans)'''
n=len(li)
left=[0]*n
right=[0]*n
res=[0]*n
left[0]=li[0]
right[n-1]=li[n-1]
for i in range(1,len(li)):
	left[i]=max(left[i-1],li[i])
print(left)
for j in range(n-2,-1,-1):
	right[j]=max(right[j+1],li[j])
print(right)
for i in range(len(li)):
	res[i]=min(left[i],right[i])-li[i]
print(res)
print(sum(res))