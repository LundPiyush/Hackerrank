n=input()
li=list(n)
last_digit=li[-1]
i=len(li)-1
right=[]
while i>=0:
	if li[i]<last_digit:
		stop=li.index(li[i])
		break
	right.append(li[i])
	#print(right)
	i=i-1
if i<0:
	print("not possible")
	exit()

mini=min(right)
c=li.index(mini)
li[c],li[stop]=li[stop],li[c]
#print(li)
sorting=li[stop+1::]
sorting.sort()
#print(sorting)
ans=''
ans=(li[0:stop+1])
ans=ans+sorting

next_num=''
for i in range(len(ans)):
	next_num+=ans[i]
print(next_num)