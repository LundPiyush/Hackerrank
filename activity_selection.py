'''def activityselect(s,f):
	f,s=zip(*sorted(zip(f,s)))
	f=list(f)
	s=list(s)
	count=1
	
	i=0
	for j in range(1,len(f)):
		print(i,j)
		print(f[i],s[j])
		if f[i]<=s[j]:
			
			print('ans=',(i+1))
			i=j
			


t=int(input())
for i in range(t):
	n=int(input())
	s=[int(x)for x in input().split()]
	f=[int(x)for x in input().split()]
	activityselect(s,f)'''
	
for _ in range(int(input())):
	n=int(input());
	l=list(map(int,input().split()));
	l1=list(map(int,input().split()));
	l2=list(enumerate(zip(l,l1)));
	l2.sort(key=lambda x:x[1][1]);
	print(list(l2));
	j=0
	print(l2[0][0]+1,end=" ");
	for i in range(1,len(l2)):
		if(l2[i][1][0]>=l2[j][1][1]):
			print(l2[i][0]+1,end=" ");
		j=i;
	print();