import array
n=int(input())
li=[int(x)for x in input().split()]
c=0
for i in range(len(li)-1):
	for j in range(i+1,len(li)):
		if li[i]>li[j]:
			li[i],li[j]=li[j],li[i]
			c=c+1
print("Array is sorted in", c ,"swaps")
print("First Element:",li[0]) 
print("Last Element:",li[-1])