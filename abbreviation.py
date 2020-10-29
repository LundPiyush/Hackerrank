# Enter your code here. Read input from STDIN. Print output to STDOUT

#abbreviation
q=int(input())
while q>0:

	a=input()
	b=input()
	c=b[::]
	d=a[::]
	c=c.lower()
	d=d.upper()
    #print(a,b,c)
	flag=0
	for e in a:
		if e in b or e in c or 97<=ord(e)<=122:
			continue
		else:
			if flag ==0:
				print("NO")
				flag=1
	print(d)
	for e in b:
		if print(e in d):
			continue
		else:
			if flag==0:
				print("NO")
				flag=1


        
	if flag==0:
		print("YES")
	q=q-1
#EYONDOCHNZYYlBZXPGzX
#EYONDOCHNZYYBZXPGXOG