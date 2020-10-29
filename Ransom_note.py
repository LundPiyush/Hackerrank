'''a,b=input().split()
a=int(a);	b=int(b)
s1=input()
s2=input()
s=''
c=0
for i in range(a):
	st=s1.split()

for i in range(b):
	s=s2.split()
#print(st)
#print(s)
for j in range(b):
	if s[j] in st:
		st.remove(s[j])
		s[j]=' '
		c=c+1
		#print(c)
	
l=len(s)
if c==l:
	print("Yes")
else:
	print("No")
'''

from collections import Counter

def ransom_note(magazine, rasom):
	print(Counter(rasom))
	print(Counter(magazine))
	return (Counter(rasom) - Counter(magazine)) == {}      
    

m, n = map(int,input().strip().split(' '))
magazine = input().split(' ')#splitethod remove the spaces and convert str into list
#if input was my name is piyush
#then magazine will be list ['my','name','is','piyush']
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
