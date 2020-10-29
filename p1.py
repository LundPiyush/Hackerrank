#hackerrank question
def max(a,b,c):
	if a>=b and a>=c:
		return a
	elif b>=c:
		return b 
	else:
		return c

n=int(input())
'''for i in range(n):
	a=input().split()
	l.append(a)'''
l=[int(n) for n in input().split()]
print(l)
one,two,three,four,five=0,0,0,0,0
for e in l:
	if e==1:
		one=one+1
	elif e==2:
		two=two+1
	elif e==3:
		three=three+1
	elif e==4:
		four+=1
	elif e==5:
		five+=1
ans=max(one,two,three)
ans1=max(ans,four,five)
print(ans1)