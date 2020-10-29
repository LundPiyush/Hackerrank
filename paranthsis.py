# Complete the isBalanced function below.
'''def isBalanced(s):
    li=[]
    s=list(s)
    #print(li)
    for i in range(len(s)):
        if s[i]=='{' or s[i]=='[' or s[i]=='(':
            li.append(s[i])
        elif s[i]=='}':
            if '{' in li:
                li.remove('{')
            else:
                break
        elif s[i]==']':
            if '[' in li:
                li.remove('[')
            else:
                break
                
        elif s[i]==')':
            if '(' in li:
                li.remove('(')
            else:
                break
    if len(li)==0:
        print("YES")
    else:
        print("NO")
t = int(input())

for t_itr in range(t):
    s = input()
    isBalanced(s)
'''
t=int(input())
for j in range(t):
	s=input()
	stack=[]
	flag=0
	for i in range(len(s)):
		if s[i]=='(' or s[i]=='[' or s[i]=='{':
			stack.append(s[i])
		elif s[i]==')' and len(stack)!=0:
			a=stack.pop()
			if a!='(':
				print("NO")
				flag=1
				break
		elif s[i]==']' and len(stack)!=0:
			a=stack.pop()
			if a!='[' :
				print("NO")
				flag=1
				break
		elif s[i]=='}' and len(stack)!=0:
            #print(stack)
			a=stack.pop()
            
            #print(a)
			if a!='{':
				print("NO")
				flag=1
				break
		else:
			print('NO')
			flag=1
			break
    #print(stack)
	if len(stack)==0 and flag==0:
		print("YES")
    





                
#            {}{(}))}
'''
#code
#code
def rotate(a,b):
	a=list(a)
	i=0
	while i<2:
		ele=a.pop(0)
		a.append(ele)
		i=i+1
	b=list(b)
	if a==b:
		return 1
	else:
		return 0
t=int(input())
for j in range(t):
	a=input()
	b=input()
	ans=rotate(a,b)
	ans1=rotate(b,a)
	if ans==0 and ans1==0:
		print(0)
	else:
		print(1)'''