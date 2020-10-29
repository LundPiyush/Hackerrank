#merge_sort
def merge(li,l,r,m):
	
	n1=m-l+1
	n2=r-m
	L=[0]*n1
	R=[0]*n2
	
	for i in range(n1):
		L[i]=li[l+i]
	for j in range(n2):
		R[j]=li[m+1+j]
	i,j,k=0,0,l
	while i<n1 and j<n2:
		if L[i]<R[j]:
			li[k]=L[i]
			i=i+1
		else:
			li[k]=R[j]
			j=j+1
		k+=1
	while i < n1:
		li[k]=L[i]
		i=i+1
		k=k+1
	while j<n2:
		li[k]=R[j]
		j=j+1
		k=k+1
	print(li)
def mergesort(li,l,r):
	if l<r:
		m=(l+r)//2
		mergesort(li,l,m)
		mergesort(li,m+1,r)
		merge(li,l,r,m)
		
	
	
	
	
	
	
	
	
	
	
li=[int(x)for x in input().split(' ')]
l=0
r=len(li)-1
mergesort(li,l,r)