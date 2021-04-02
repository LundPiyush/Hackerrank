#cheese and mouse

m=int(input())
mouse=list(map(int,input().split(' ')))
chesse=list(map(int,input().split(' ')))
diff=0
for i in range(m):
    difference=abs(mouse[i]-chesse[i])
    diff=max(diff,difference)
print(diff)
