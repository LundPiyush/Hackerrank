'''n,d=input().split()
n=int(n)
d=int(d)
li=[int(a)for a in input().split()]
i,j,med=0,0,0
#li=[]
li1=[]
m,a,b,c,noti=0,0,0,0,0
for i in range(n-d):
	li1=li[i:i+d]
    #print(li)
	#print(li1)
	li1.sort()
	length=len(li1)
	if (length%2)!=0:
		m=length//2
		med=li1[m]
	else:
		a=li1[length//2]
		b=li1[(length//2)-1]
		med=(a+b)/2
	day_exp=li[i+d]
	c=2*med
	if day_exp>=c: 
		noti+=1
	li1.clear()
    #li.clear()
print(noti)		'''



li=[0,1,0,2,1,0,1,3,2]
'''i=2
a=li[i]-1
print(a)
li[i],li[a]=li[a],li[i]
print(li)'''
print(sum(li[4:7]))