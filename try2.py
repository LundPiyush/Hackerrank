#s=input()
'''if s.count('a')==111 or s.count('a')==11111:
    print("YES")
    exit()'''
#d1={}
#for i in range(len(s)):
    #if s[i] not in d1:
     #   d1[s[i]]=1
    #else:
        #key_count=d1.get(s[i])
     #   d1[s[i]]=d1[s[i]]+1
#li=[]
#li=d1.values()
#li=list(li)
'''
flag=0
c=0
current=0
end=len(li)-1
#print(d1)
while current<end:
    if li[0]==li[current+1]:
        #c=c+1
        current+=1
    elif flag==0 :
        current+=1
        flag=1
    else:
        print("NO")
        flag=2
        exit()

if flag !=2:
    print("YES")
'''

'''flag=0

#print(li)
for i in range(len(li)):
    if li[0]==li[i]:
        continue
    elif flag==0:
        flag=1
    else:
        print("NO")
        flag=2
        exit()
if flag!=2:
    print("YES") 

'''
x,y=4,4

#i=0
arr=[int(i)for i in input().split()]
k=0
A=[[0 for i in range(4)]for i in range(4)]
for i in range(4):
	for j in range(4):
		A[i][j]=arr[k]
		k=k+1
print(A)
