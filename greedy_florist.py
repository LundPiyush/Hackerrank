nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
c.sort(reverse=True)
ans,j=0
for i in range(n):
	if k>i:
		ans=ans+c[i]
	else:
		ans=ans+(i//k+1)*c[i]
print(ans)