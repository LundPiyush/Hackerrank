n,m=input().split(' ')
n=int(n)
m=int(m)
li=[int(x)for x in input().split(' ')]
#print(li)
while m>0:
	ele=li.pop(0)
	li.insert(1000,ele)
	m=m-1
for e in li:
	print(e)