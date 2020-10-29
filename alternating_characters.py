
#-----------------------------------------------------------------
n=int(input())
li=[]
count=[]
while n>0:
    s=input()
    for i in s:
        li.append(i)
    current=0
    end=len(li)-1
    c=0
    print(li)
    #li=['A','A','B','B','A']
    #while will start from 0 till end and we see i and i+1 element are same then only count is #incresed
    while current<end:
        if li[current]==li[current+1]:
            c+=1
        current=current+1
    li.clear()
    count.append(c)
    n=n-1
for e in count:
    print(e)















