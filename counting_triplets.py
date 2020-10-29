n,r=input().split(' ')
n=int(n)
r=int(r)
li=[int(n)for n in input().split(' ')]
cur=li[0]
count=1
final_list=[]
d={}
for i in range(1,n):
	if li[i]==cur:
		count+=1
	else:
		d[cur]=count
		#print(d)
		cur=li[i]
		#print(cur)
		count=1
d[cur]=count
print(d)#priinting dictionary  
res=0
for i in range(len(d)):
	a=list(d.keys())
	my_key=a[i]
	print("my key",a[i])
	b=a[i]*r
	c=a[i]*r*r
	print("b n c",b,c)
	if b and c in a:
		x=d[a[i]]
		y=d[b]
		z=d[c]
		
		print(x,y,z)#getting the count of key present in dict
		ans=x*y*z
		res=res+ans
		print(res)
print(res)




















'''


#print(final_list)
triplets=0
for i in range(1,len(final_list)-1):
	a=final_list[i][0]//r
	b=final_list[i][0]*r
	print(a,b)
	if a==final_list[i-1][0] and b==final_list[i+1][0]:
		triplets+=max(final_list[i-1][1],final_list[i+1][1],final_list[i][1])
		
print(triplets)
'''














