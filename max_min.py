li=[int(x)for x in input().split(' ')]
maxi=max(li)
mini=min(li)
li.remove(mini)
sumi=sum(li)
li.append(mini)
li.remove(maxi)
sum2=sum(li)

print(sum2,sumi)


