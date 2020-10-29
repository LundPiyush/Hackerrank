'''n=int(input())
for i in range(n):
	money=int(input())
	flavour=int(input())
	li=[int(flavour)for flavour in input().split(' ')]
	m=[]
	for i in range(len(li)):
		for j in range(i+1,len(li)):
			#print(li[i],li[j])
			m.append((li[i],li[j]))
	#print(m)
	for e in m :
		if e[0]+e[1]==money:
			first_flavour=li.index(e[0])
			second_flavour=li.index(e[1],first_flavour+1)
			print(first_flavour+1,second_flavour+1)
			m.clear()
			break
'''	
#the final one 
test_cases=int(input())
for i in range(test_cases):
	money=int(input())
	n=int(input())
	costlist=[int(x) for x in input().split()]
	print(costlist)
	costhash={}
	#print(type(costhash))
	for i in range(n):
		#print(costlist[i])
		#print(costhash.get(costlist[i]))
		costhash[costlist[i]]=costhash.get(costlist[i],"")+" "+str(i+1)
	print(costhash)
	for i in costlist:
		if money-i in costhash:
			print("money -i",money-i)
			indices1=costhash[i].split()
			print(indices1)
			indices2=costhash[money-i].split()
			print(indices2)
			if (money-i)==i:
				print(indices1[0],indices1[1])
				break
			else:
				print("else")
				print(indices1[0],indices2[0])
				break