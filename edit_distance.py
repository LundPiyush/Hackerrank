#edit distance
#given 2 strings find the no of minimum changes can be done to
#convert one string into anoher
#possible operations-delete,replace,add

str1=input()
str2=input()
n1=len(str1)
n2=len(str2)


T=[[0 for i in range(n2+1)]for i in range(n1+1)]

for i in range(n2+1):
	T[0][i]=i
print(T)
for j in range(n1+1):
	T[j][0]=j

for i in range(1,n1+1):
	for j in range(1,n2+1):
		#print(i,j,str1[i-1],str2[j-1])
		if str1[i-1]==str2[j-1]:
			T[i][j]=T[i-1][j-1]
		else:
			T[i][j]=min(T[i-1][j],T[i][j-1],T[i-1][j-1])+1
		print(T)
print(T[-1][-1])
