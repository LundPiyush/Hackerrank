li=[int(x)for x in input().split(' ')]
li1=[int(x)for x in input().split(' ')]
alice,bob=0,0
for i in range(len(li)):
	if li[i]>li1[i]:
		alice=alice+1
	elif li[i]<li1[i]:
		bob=bob+1
	else:
		continue
print(alice,bob)

