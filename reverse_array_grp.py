#
t=int(input())
for i in range(t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    ans=[int(x)for x in input().split()]
    for e in range(k-1,-1,-1):
        print(ans[e],end=' ')
    for f in range(k,n):
        print(ans[f],end=' ')