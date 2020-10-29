a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
c = list(map(int, input().rstrip().split()))
a = list(sorted(set(a)))
b = list(sorted(set(b)))
c = list(sorted(set(c)))
    
ai = 0
bi = 0
ci = 0
    
ans = 0
    
while bi < len(b):
	while ai < len(a) and a[ai] <= b[bi]:
		print(a[ai],b[bi])
		ai += 1
		
        
	while ci < len(c) and c[ci] <= b[bi]:
		print(b[bi],c[ci])
		ci += 1
		
	ans += ai * ci
	bi += 1
print("ans",ans)