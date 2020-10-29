# Complete the isBalanced function below.
def isBalanced(s):
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

 