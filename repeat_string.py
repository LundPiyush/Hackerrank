def f1(st,n):
	st1=st
	st=st*n
	li=[]
	li=list(st)
	
	for i in range(n,len(st),1):
		li.pop()
	st=str(li)
	
	print(st.count('a'))
	



st=input()
n=int(input())
f1(st,n)



from datetime import datetime
print(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S %p"))
