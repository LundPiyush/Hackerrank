n=int(input())
while n>0:
	x,y,z=input().split()
	x=int(x)
	y=int(y)
	z=int(z)
	if abs(x-z)==abs(y-z):
		print("Mouse C")
	elif abs(x-z)>abs(y-z):
		print("Cat B")
	else:
		print("Cat A")
	n=n-1