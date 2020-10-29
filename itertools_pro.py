from itertools import product
data=[10,2,3,14,12]
a=2;	b=1;	c=-1;	d=3;	m=5;
c=0
'''
for pairs in list(product(arr,repeat=2)):
	x=(pairs[1]**2)%m
	y=(a*(pairs[0]**3) + b*(pairs[0]**2) + c*pairs[0] + d) % m
	print("x,y",x,y)
	if x==y:
		c=c+1
            #print(j[1])
	#print(c)    
print("****************************************")	
cnt=0	
for j in list(product(arr, repeat=2)):
    # for j in range(len(arr)):
        # for k in range(len(arr)):
		lhs = (j[1]**2) % m
		rhs = (a*(j[0]**3) + b*(j[0]**2) + c*j[0] + d) % m
		print("lhs,rhs",lhs,rhs)
		if (lhs == rhs):
			cnt += 1
		#print(cnt)
'''	
	
	
#'''	
	
def function(a,b,c,d,m,data):
	from collections import defaultdict
	lhs_mapping = defaultdict(int)
	rhs_mapping = defaultdict(int)
	print(lhs_mapping,rhs_mapping)
	for i in data:
		lhs = i**2 % m
		
		lhs_mapping[lhs] += 1
		#print(lhs_mapping)
		rhs = (a* i**3 + b * i**2 + c*i + d)
		#print('rhs',rhs)
		rhs=rhs%m
		#print('rhs',rhs)
		
		
		rhs_mapping[rhs] += 1
	print(dict(rhs_mapping))
	print(dict(lhs_mapping))
		#print(rhs_mapping[rhs])
	out = 0
	for key,value in rhs_mapping.items():
		print(key,value)
		print(lhs_mapping[key])
		out += value * lhs_mapping[key]
		print(out)
	return out
    
 
t = int(input())
for _ in range(1):
	a,b,c,d,m = [int(i) for i in input().split()]
	n = int(input())
	data = [int(i) for i in input().split()]
	print(function(a,b,c,d,m,data))

	
	
	
	
	
	
	
	
	
	
	
	
	