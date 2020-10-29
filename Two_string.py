n=int(input())
while n>0:
	s1=input()
	s2=input()
	flag=0
	for i in range(len(s1)):
		if s1[i]in s2:
			flag=1
			break
	if flag==0:
		print("NO")
	else:
		print("YES")
	n=n-1