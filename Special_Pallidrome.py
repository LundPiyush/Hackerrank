
def pall(n,s):
#step1
    cur=s[0]
    count=1
    li=[]
    for i in range(1,n):
        if s[i]==cur:
            count+=1
        else:
            li.append((cur,count))
            cur=s[i]
            count=1
            #print(cur)
            #print(li)
	li.append((cur,count))
    #print(li)
#step2
	ans=0
	for e in li:
		ans=ans+e[1]*(e[1]+1)//2
		#print(ans)
#step3
	for i in range(1,len(li)-1):
		#print(li[i])
		#print(li[i-1][1])
		if li[i-1][0]==li[i+1][0] and li[i][1]==1:
			ans=ans+min(li[i-1][1],li[i+1][1])
	return ans	

n=int(input())
s=input()
a=pall(n, s)
print(a)