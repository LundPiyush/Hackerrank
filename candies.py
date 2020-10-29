n = int(input())
a = []

for _ in range(n):
	arr_item = int(input())
	a.append(arr_item)
#result = candies(n, arr)
b=[1]*n
for i in range(len(a)-1):
	if a[i]<a[i+1] and b[i]>=b[i+1]:
		b[i+1]=b[i]+1
print(b)
for i in range(len(a)-1,0,-1):
	#print(i,a[i],"hi")
	if a[i-1]>a[i] and b[i]>=b[i-1]:
		b[i-1]=b[i]+1
print(b)
print(sum(b))