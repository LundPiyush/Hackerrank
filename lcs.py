#code
def lcs(x,y):
	l=[]
	for i in range(len(x)+1):
		li=[0 for j in range(len(y)+1)]
		l.append(li)
	for i,p in enumerate(x):
		for j,q in enumerate(y):
			if p==q:
				l[i+1][j+1]=l[i][j]+1

			else:
				l[i+1][j+1]=max(l[i+1][j],l[i][j+1])
			
	print(l[-1][-1])    
t=int(input())
for j in range(t):
	a=input()
	b=input()
	lcs(a,b)