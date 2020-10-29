#sock merchant
'''import array
n=int(input())
num=array.array('i',[])
for i in range(n):
	m=int(input())
	num.append(m)
c=0
for i in range(n-1):
	if num[i]==num[i+1]:
		c=c+1
	else:
		continue
print(c)
'''
n=int(input())
socks=[int(x)for x in input().split()]
#print(socks)
c=0
socks.sort()
print(socks)
while n>0:
	for e in socks:
			if socks.count(e)>=2:
				socks.remove(e)
				socks.remove(e)
				c=c+1
	n=n-1
print(c)


'''c=0
for i in range(len(socks)):
		if socks.count(socks[i])>=2:
			socks.remove(socks[i])
			socks.remove(socks[i+1])
			print(socks)
			c=c+1
print(c)'''