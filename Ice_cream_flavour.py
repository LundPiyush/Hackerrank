'''n=int(input())
res=[]
sum=0
while n>0:
	#res.append(-1)
	sum1=0
	money=int(input())
	sum=money
	flavour=int(input())
	li=[int(flavour)for flavour in input().split(' ')]
	length=len(li)
	for i in range(len(li)):
		for j in range(i+1,len(li)):
			sum=li[i]+li[j]
			if money==sum:
				e=li.index(li[i])
				e1=li.index(li[j])
				res.append(e)
				res.append(e1)
			else:
				sum=0
				continue
		
			
	n=n-1
x=0
print(res)
for i in range(len(res)):
	x=res[i]
	print(x,end=" ")
	if i%2!=0:
		print()

abc=[1,2,3,4,5]
sum,s=0,9

for i in range(len(abc)):
	for j in range(i+1,len(abc)):
		sum=abc[i]+abc[j]
		if s==sum:
	
			
		else:
			sum=0
			continue
		'''
		
		
		
from itertools import combinations

test_cases = int(input())

for test_case in range(test_cases):
	dollars = int(input())
	total_flavors = int(input())  # unused variable
    #flavors_costs =input()
    # string transformed into an array of ints
	flavors_costs = [int(x) for x in input().split(' ')]
	m=[]
    # generation of combinations of 2 flavors
	flavors_combinations = combinations(flavors_costs, 2)
	
	'''for i in list(flavors_combinations):
		m.append(i)
	print(m)'''
	for flavors_tuple in flavors_combinations:
		print(flavors_tuple)
        # two distinct flavors whose cost equals `dollars`
        #if ((flavors_tuple[0] + flavors_tuple[1]) == dollars):
		if ((flavors_tuple[0] + flavors_tuple[1]) == dollars):
            # get the index in flavors_costs for the first flavor
			first_flavor = flavors_costs.index(flavors_tuple[0])
            # get the index in flavors_costs for the second flavor.
            # since both flavors might cost the same, second_flavor must be
            # searched discarding the position of first_flavor
			second_flavor = flavors_costs.index(flavors_tuple[1],
                                                first_flavor + 1)
            # indices are indexed from 1
			print("{} {}".format(first_flavor + 1, second_flavor + 1))
            # unique solution
			break