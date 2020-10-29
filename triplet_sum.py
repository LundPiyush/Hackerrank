def triplets(lena,lenb,lenc,a,b,c):
	a.sort()
	b.sort()
	c.sort()
	
	a1,b1,c1=0,0,0
	res=0
	
	
















lenaLenbLenc = input().split()
lena = int(lenaLenbLenc[0])
lenb = int(lenaLenbLenc[1])
lenc = int(lenaLenbLenc[2])
arra = list(map(int, input().rstrip().split()))
arrb = list(map(int, input().rstrip().split()))
arrc = list(map(int, input().rstrip().split()))
triplets(lena,lenb,lenc,arra, arrb, arrc)