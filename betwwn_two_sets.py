
def getTotalX(a, b):
    #
    # Write your code here.
    #
	start=a[-1]
	end=b[0]
	c=0
	li=[]
	l=[]
	index=0
	for i in range(len(a)):
		for j in range(start,end+1):
			if j%a[i]==0:
				#print(j,a[i])
			#index+=1
				c=c+1
				li.append(j)
	
	li=set(li)
	li=list(li)
	print(li)
	for j in b:
		for i in li:
			if j%i==0:
				l.append(i)
	l=set(l)
	



nm = input().split()
n = int(nm[0])
m = int(nm[1])
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
total = getTotalX(a, b)

