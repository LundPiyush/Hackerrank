from sys import stdin
from collections import Counter
cases = int(input())

for _ in range(cases):
	n=int(input())
	l=list(map(int,stdin.readline().split()))
	'''d={}

	for i in l:
		if(i in d):
			d[i] +=1
		else:
			d[i] = 1'''
	d=Counter(l)
	temp=[]
	for key,val in d.items():
		temp.append([key,val])
	print(temp)
	temp.sort(reverse=True, key=(lambda x: x[1]))
	print(temp)
	res = []
	for i in temp:
		for j in range(i[1]):
			res.append(i[0])
	print(*res)