from collections import Counter,defaultdict

'''def freqQuery(queries):

	results = []
	lookup = dict()
	freqs = defaultdict(set)
	print(freqs)
	for command, value in queries:
		freq = lookup.get(value, 0)
		if command == 1:
			lookup[value] = freq + 1
			freqs[freq].discard(value)
			freqs[freq + 1].add(value)
			print(freqs)
		elif command == 2:
			lookup[value] = max(0, freq - 1)
			freqs[freq].discard(value)
			freqs[freq - 1].add(value)
		elif command == 3:
			results.append(1 if freqs[value] else 0)
	print(results)'''  
n=int(input())
A=[]
arr=[]
'''for i in range(n):
    q=[int(x)for x in input().split(' ')]
    A.append(q)'''
#freqQuery(A)	
#print(A)
d={}
for i in range(n):
	a=A[i]
	if a[0]==1:
		if a[1] not in d:
			d[a[1]]=1
		else:
			d[a[1]]=d[a[1]]+1
		#print(d)
	elif a[0]==2:
		
		y=a[1]
		if y in d:
			key_count=d[y]-1
			d[y]=key_count
		#print(d)
	else:
		z=a[1]
		flag=0
		#print(d)
		
		for e in d:
			if d[e]==z:
				d.pop(e)
				flag=1
				print(1)
				break
		if flag!=1:
			print(0)
		#print(d)