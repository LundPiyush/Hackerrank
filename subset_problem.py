#subset problem it will return true or false weather the subset is present or not

#non -contiguous
n=int(input())
arr=[int(x)for x in input().split(' ')]
length=len(arr)
li=[[False for j in range(n+1)]for i in range(length)]
#print(li)

for i in range(length):
	li[i][0]=True
	
for j in range(n+1):
	if arr[0]==j:
		li[0][j]=True
for i in range(1,length):
	for j in range(n+1):
		if j<arr[i]:
			#print(arr[i])
			li[i][j]=li[i-1][j]
		else:
			li[i][j]=li[i-1][j] or li[i-1][j-arr[i]]
print(li[-1][-1])