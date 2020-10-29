def max_subarray_sum(n,m,a):
	arr.sort()
	modulo=n
	j=1
	max_mod=0
	while modulo>0:
		for i in range(n-j+1):
			value=sum(a[i:i+j])%m
			print(a[i:i+j])
			print(sum(a[i:i+j]))
			print(value)
			if max_mod<value:
				max_mod=value
				print("max_mod",max_mod)
			if max_mod==m-1:
				print(max_mod)
				exit()
		j=j+1
		modulo=modulo-1
	print(max_mod)





q = int(input())

for q_itr in range(q):
	nm = input().split()
	n = int(nm[0])
	m = int(nm[1])
	a = list(map(int, input().rstrip().split()))
	max_subarray_sum(n,m,a)
