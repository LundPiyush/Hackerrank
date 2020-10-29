n = int(input())
k = int(input())
arr = []
li=[]
for _ in range(n):
	arr_item = int(input())
	arr.append(arr_item)
arr.sort()
print(arr)
a=n-k
min_value=999999999999


value=0
for i in range(a+1):
	value=arr[i+k-1]-arr[i]
	print(arr[i+k-1],arr[i],value)
	if value<min_value:
		min_value=value
print(min_value)
