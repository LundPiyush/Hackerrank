def get_median(counts, mids):
	res = []
	for mid in mids:
		gone = 0
		for i, v in enumerate(counts):
			gone += v
			if gone >= mid:
				res.append(i)
				break
	return sum(res) / len(res)


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
	alerts = 0
	counts = [0] * 201
	#print(counts)
	#print("d",d)
	print(expenditure)
	if d % 2 == 1:
		mids = [d // 2 + 1]
	else:
		mids = [d // 2, d // 2 + 1]
	print(mids)
	for v in expenditure[:d]:
		print(v)
		counts[v] += 1
	print(count)
	for i, exp in enumerate(expenditure[d:]):
		print(i,exp)
		median = get_median(counts, mids)

		if exp >= 2 * median:
			alerts += 1
        
		old_value = expenditure[i]
		counts[old_value] -= 1
		counts[exp] += 1
	return alerts

x,y=input().split()
x=int(x)
y=int(y)
l=[int(a)for a in input().split()]
n=x-y
print(activityNotifications(l,y))
'''i,j,med=0,0,0
li=[]
li1=[]
m,a,b,c,noti=0,0,0,0,0
while i<n:
	for j in range(i,x-1):
		if len(li)!=y:	
			li.append(l[j])
			li1.append(l[j])
		else:
			continue
	print(li)
	print(li1)
	li1.sort()
	li1_length=len(li1)
	if (li1_length%2)!=0:
		m=li1_length//2
		med=li1[m]
	else:	
		a=li1[li1_length//2]
		b=li1[(li1_length//2)+1]
		med=(a+b)/2
	day_exp=l[y]
	c=2*med
	if day_exp>=c:
		noti+=1
	li1.clear()
	li.clear()
	i=i+1
print(noti)'''		