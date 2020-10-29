n=int(input())
li=[int(n)for n in input().split(' ')]
'''first,swap=0,0
last=len(li)-1
while first<last:
	while li[first]==first+1 and first<last:
		first+=1
		print(li[first])
	if first<last:
		print(li[first])
		print(li[first]-1)
		print(li)
		a=li[first]
		b=li[li[first]-1]
		li[first],li[li[first]-1]=li[li[first]-1],li[first]
		#a,b=b,a
		#print(a,b)
		print(li)
		swap=swap+1
		break
print(swap)'''
swap=0
i=0
while i<len(li):
        #Bug in input data which violates problem constraint break
    if li[i]==(i+1):
        i+=1
        continue
    #print(li[i],li[li[i]-1])
    a=li[i]-1
    li[i],li[a]=li[a],li[i]
	#li[li[i]-1],li[i]=li[i],li[li[i]-1]
    print(li)
    swap+=1
    #exit()
print(swap)