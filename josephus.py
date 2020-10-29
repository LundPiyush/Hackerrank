def josephus(n,k):
	if n==1:
		return 0
	else:
		return (josephus(n-1,k)+k)%n
n=int(input())
k=int(input())
ans=josephus(n,k)
print(ans+1)