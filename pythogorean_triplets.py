#pythogoran triplet
def pythogoran(arr,n):
	for i in range(n):
		arr[i]=arr[i]*arr[i]
	for i in range(n-1,1,-1):
		j=0
		k=i-1
		while j<k:
			if arr[j]+arr[k]==arr[i]:
				return True
			elif arr[j]+arr[k]<arr[i]:
				j=j+1
			elif arr[j]+arr[k]>arr[i]:
				k=k-1
	return False	
	
t=int(input())
for j in range(t):
    n=int(input())
    arr=[int(x)for x in input().split()]
    ans=pythogoran(arr,n)
    if ans:
        print('Yes')
    else:
        print('No')