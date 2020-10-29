def get_median(counting_sort,med_position,d):
	counter,left=0,0,0
	while counter<med_position:
		counter+=counting_sort[left]
		left+=1
	right=left
	left-=1
	
	if counter>med_position or d%2!=0:
		return left
	else:
		while counting_sort[right]==0:
			right+=1
		return (left+right)/2
	
	
	
	
	
	
	
	
	
	
	
def notification(li,n,d):
	counting_sort=[0]*200
	for i in range(n):
		counting_sort[li[i]]+=1
	print(counting_sort)
	current=0
	if d%2==0:
		med_position=d//2
	else:
		med_position=(d//2)+1
	noti=0
	while d<n:
		median=get_median(counting_sort,med_position,d)
		if li[d]>=2*median:
			noti+=1
		counting_sort[li[current]]-=1
		counting_sort[li[d]]+=1
		d=d+1
		current+=1
n,d=input().split(' ')
n=int(n)
d=int(d)
li=[int(x)for x in input().split(' ')]
notification(li,n,d)

