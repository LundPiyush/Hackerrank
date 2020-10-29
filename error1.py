'''import array
n=int(input())
li=[int(x)for x in input().split()]
c=0
for i in range(len(li)-1):
	for j in range(i+1,len(li)):
		if li[i]>li[j]:
			li[i],li[j]=li[j],li[i]
			c=c+1
		print(li)
print("Array is sorted in", c ,"swaps.")
print("First Element:",li[0]) 
print("Last Element:",li[-1])

'''
#ice cream palour

t = int(input().strip())
for a0 in range(t):
	m = int(input().strip())
	n = int(input().strip())
	a = map(int,input().strip().split(' '))

    # find matched number
	cost_map = {}
	for i, cost in enumerate(a):
		print(i,cost)
		sunny = cost
		johnny = m - cost
		if johnny in cost_map.keys():
			print(cost_map[johnny]+1, i+1)
		else:
			cost_map[cost] = i
		print(cost_map)