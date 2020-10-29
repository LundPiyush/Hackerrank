#Maximum difference between two elements such that larger element 
#appears after the smaller number


def max(arr,n):
	max_diff=arr[1]-arr[0]
	min_ele=arr[0]
	for i in range(n):
		if arr[i]-min_ele>max_diff:
			max_diff=arr[i]-min_ele
		if arr[i]<min_ele:
			min_ele=arr[i]
	print(max_diff)


arr=[int(x)for x in input().split(' ')]
n=len(arr)
max(arr,n)