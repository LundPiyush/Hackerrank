def nCr(n,r): 
  
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
  
# Returns factorial of n 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 
testcase=int(input())
for i in range(testcase):
	n=int(input())
	li=[int(n)for n in input().split()]
	q=int(input())
	ll=[int(q)for q in input().split()]
	lr=[int(q)for q in input().split()]	
	lx=[int(q)for q in input().split()]
	p=int(input())
	lis=li[::]
ans=nCr(q,p)
ans=int(ans)
max=0
for e in range(ans-1):
	#1 n 2
	x=ll[e]
	y=lr[e]
	z=lx[e]
	print(x,y,z)
	for k in range(x,y+1):
		lis[k]=lis[k]+z
		#print(lis)
print(lis)
max=sum(lis)
max1=0
lis.clear()
print("max0",max)
lis=li[::]

for e in range(1,ans):
	#1 n 2
	x=ll[e]
	y=lr[e]
	z=lx[e]
	print(x,y,z)
	for k in range(x,y+1):
		lis[k]=lis[k]+z

print(lis)
max1=sum(lis)
max2=0
lis.clear()
lis=li
print("max1",max1)
print(lis)

for e in range(0,ans,2):
	#1 n 2
	x=ll[e]
	y=lr[e]
	z=lx[e]
	for k in range(x,y+1):
		lis[k]=lis[k]+z
max2=sum(lis)
lis.clear()
lis=li
print("max2",max2)
print(lis)