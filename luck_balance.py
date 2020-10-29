nk = input().split()
n = int(nk[0])
k = int(nk[1])
contests = []
contests1=[]
for i in range(n):
		x,y=input().split()
		x=int(x)
		y=int(y)
		if y==0:
			contests1.append(x)
		else:
			contests.append(x)
contests.sort(reverse=True)
print(contests)
ans=0
for i in range(len(contests)):
	if k>i:
		ans=ans+contests[i]
	else:
		ans=ans-contests[i]
ans1=sum(contests1)
ans=ans+ans1
print(ans)

