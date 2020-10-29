'''n=int(input())

l=[]
lo=[0]
#flag=0
for i in range(n):
	count=0
	flag=0
	
	a=int(input())
	lin=[int(x)for x in input().split()]
	
	for i in range(len(lin)):
		x=max(lin)
		y1=lin.index(x)
		y2=x-1
		if y1<y2 and (y2-y1)<=2:
			count=count+(y2-y1)
		elif y2-y1>2:
			l.append('too chiotic')
			flag=1
			break
			
		lin[y1]=-1
		if y2-y1<=2:
			lo.append(count)
	if flag!=1:
		#print(lo)
		m=max(lo)
		l.append(m)
		

for e1 in l:
	print(e1)
	
	
'''



test_cases = int(input())

for i in range(test_cases):
    t = int(input())
    a=[int(t)for t in input().split()]
    swaps = [0] * t
    print(swaps)
    swapped = True

    while swapped:
        swapped = False
        for i in range(t):
            while i < t - 1 and a[i] > a[i + 1]:
                #print(a[i],a[i+1])
                swaps[a[i] - 1] += 1
                print(swaps)
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                #print(a)
                i += 1

    s = 0
    flag=0
    for swap in swaps:
        s=s+swap

        if swap > 2:
            print('Too chaotic')
            flag=1
            break
    if flag!=1:    
        print(s)

