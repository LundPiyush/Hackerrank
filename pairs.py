n,target_value=input().split(' ')
n=int(n)
target_value=int(target_value)
li=[int(n)for n in input().split(' ')]
count=0

li=set(li)
for e in li:
	ele=e-target_value
	if ele in li:
		count+=1
			
print(count)