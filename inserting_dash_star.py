#inserting dashes betwwen 2 odd no and * between two even
n=input()
li=list(n)
cur=0
for i in range(len(li)):
	if int(li[i])%2==0 and int(li[i+1])%2==0:
		s=li[i]+'*'+li[i+1]
		
	print(s)