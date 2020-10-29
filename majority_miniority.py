#majority element 
#A majority element in an array A[] of size n is an element 
#that appears more than n/2 times 
def get_key(val):
	for key,value in d.items():
		if value==val:
			return key
	return 

li=[int(x)for x in input().split(' ')]
n=len(li)
cur=li[0]
count=1
d={}

for i in range(n):
	if li[i] not in d:
		d[li[i]]=1
	else:
		d[li[i]]=d[li[i]]+1

print(d)
res=list(d.values())
print(res)
for e in res:
	if e>(n//2):
		print(get_key(e))