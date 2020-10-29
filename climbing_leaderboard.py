#climbing the leaderboard
n=int(input())
scores=[int(n)for n in input().split(' ')]
m=int(input())
alice=[int(x)for x in input().split(' ')]
d={}
count=0
for e in scores:
	if e not in d:
		d[e]=count+1
		count=count+1
#print(d)
rank=[]
for i in range(len(alice)):
	sorted_score=[]
	scores.append(alice[i])
	#print(scores)
	sorted_score=scores.copy()
	sorted_score.sort(reverse=True)
	#print(sorted_score)
	alice_score=sorted_score.index(alice[i])
	#print("index",alice_score)
	previous_rank=d[sorted_score[alice_score-1]]
	#print("rank",previous_rank)
	if alice[i]==sorted_score[alice_score-1]:
		rank.append(previous_rank)
	elif alice_score==0:
		rank.append(1)
	else:
		rank.append(previous_rank+1)
	print(rank)
	scores.remove(alice[i])
	#sorted_score.pop(alice[i])
	sorted_score.clear()
print(rank)