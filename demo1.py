'''a="fcrxzwscanmligyxyvym"
b="jxwtrhvujlmrpdoqbisbwhmgpmeoke"
a=list(a)
b=list(b)
d=a.copy()
e=b.copy()
c=0
sum=0
for i in a:
	print(i)
	if i in e:
		d.remove(i)
		e.remove(i)
		print(d,e)
sum=len(d)+len(e)
print(sum) 
print(d,e) '''
#print(max(2,3))
#print(2//2)

'''def comparator(a,b):
	if a>b:
		print("a>b")
		return -1
	else:
		return 1

ans=comparator(10,20)
print(ans)'''


a=[3 ,7 ,4, 6, 5]
n=len(a)
print(n)

j=2


for i in range(n-1):
	j=0
	print(i,j)
	while (i+j+2)<=n-1:
		print("i,j",i,j)
		print(a[i:len(a):j+2])
		j=j+1





'''print(a[0:len(a):2])
print(a[0:len(a):3])
print(a[0:len(a):4])#4
print(a[1:len(a):2])
print(a[1:len(a):3])#4
print(a[1:len(a):4])
'''









