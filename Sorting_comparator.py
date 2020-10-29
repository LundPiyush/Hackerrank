'''n=int(input())
d={}
li=[]
for i in range(n):
	x,y=input().split()
	y=int(y)
	li.append((x,y))

for i in range(len(li)-1):
	for j in range(i+1,len(li)):
		if li[i][1]<li[j][1]:
			li[i],li[j]=li[j],li[i]
			print(li)
		elif li[i][1]==li[j][1]:
			if li[i][0]>li[j][0]:
				li[i],li[j]=li[j],li[i]
for e in range(len(li)):
	print(li[e][0]," ",li[e][1])
	
	
	
'''
	
	
	
	
from functools import cmp_to_key
class Player:
	def __init__(self, name, score):
		self.name=name
		self.score=score
        
def comparator(a, b):
		if a.score>b.score:
			print(a.score,b.score)
			return -1
		elif a.score< b.score:
			return 1
		elif a.score== b.score:
			if a.name>b.name:
				return 1
			elif a.name<b.name:
				return -1
			else: 
				return 0
        



n = int(input())
data = []
for i in range(n):
	name, score = input().split()
	score = int(score)
	player = Player(name, score)
	data.append(player)    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
			
		
		

	