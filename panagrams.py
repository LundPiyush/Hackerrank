#panagram
s=input()
s=s.lower()
c=[0]*26
offset=ord('a')
for i in range(len(s)):
	if ord(s[i])>=97 and ord(s[i])<=123:
		c[ord(s[i])-offset]=1
res=[]
if min(c)==0:
	print('not a panagram')
	
else:	
	print('panagram')
for i in range(len(c)):
	if c[i]==0:
		res.append(chr(i+offset))
print(c)
print(*res)