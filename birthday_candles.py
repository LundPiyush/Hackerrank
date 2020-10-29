#kitne candles tallest hai 
n=int(input())
li=[int(x)for x in input().split(' ')]
maxi=max(li)
ans=li.count(maxi)
print(ans)