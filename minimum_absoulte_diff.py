#minimum difference 
'''li=[int(x)for x in input().split(' ')]
minimum=99
for i in range(len(li)-1):
	for j in range(i+1,len(li)):
		#print(li[i],li[j])
		if abs(li[i]-li[j])<minimum:
		#	print(li[i]-li[i+1])
			minimum=abs(li[i]-li[j])

print(minimum)'''
#code
from collections import Counter
t=int(input())
for i in range(t):
	a,b=input().split(' ')
    
	d1=Counter(a)
	d2=Counter(b)
	print(d1)
	print(d2)
	if d1-d2=={}:
		print("YES")
	else:
		print("NO")
    