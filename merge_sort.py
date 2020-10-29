test_cases=int(input())
for i in range(test_cases):
	n=int(input())
	c=0
	li=[int(n)for n in input().split(' ')]
	while len(li)>0 :
		ls=li.copy()
		ls.sort()
		if li==ls:
			break
		b=min(li)
		print("min",b)
		a=li.index(b)
		print("ind",a)
		if a==0 and len(li)>1:
			li[a]=100
			print(li)
		else:
			li[0],li[a]=li[a],li[0]
			print(li)
			if len(li)>1:
				c=c+1
				print("count",c)
			li.pop(0)
			print(li)
		
	print(c)
	'''p=min(li)
	print(p)
	q=li.index(p)
	print(q)'''
	#print("count",c)
	