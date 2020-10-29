x1,v1,x2,v2=input().split(' ')
x1=int(x1)
v1=int(v1)
x2=int(x2)
v2=int(v2)
flag=0
for i in range(10000):
	a=x1+v1*i
	b=x2+v2*i
	if a==b:
		flag=1
		print("yes")
	else:
		continue
if flag==0:
	print("NO")