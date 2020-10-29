'''n,m=input().split()
n=int(n)
m=int(m)
li=[0]*n
for i in range(m):
	a,b,k=input().split()
	a=int(a)
	b=int(b)
	k=int(k)
	for j in range(a-1,b):
		li[j]=li[j]+k

#print(li)
x=max(li)
print(x)

'''
n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
#print(list)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    #print(list)
    if((y)<=len(list)): 
        #print(y)
        list[y] -= incr;
        #print(list)
max = x =a= 0
for i in list:
    x=x+i
    print(x)
    if(max<x): max=x;
print(list)
#print(a)
print(max)



 