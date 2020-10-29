n=int(input())
li=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
for i in range(n):
	ele=int(input())
	if ele<38:
		print(ele)
	elif ele==100:
		print(ele)
		
	else:
		n=ele//5
		print(n)
		ans=li[n]-ele
		if ans<3:
			print(li[n])
		 
		elif ans==3:
			print(ele)
		else:
			print(ele)
		