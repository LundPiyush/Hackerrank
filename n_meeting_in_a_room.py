stimes=[1,3,0,5,8,5]
#index=list(range(len(stimes)))
index=[0]*(len(stimes))
for i in range(len(stimes)):
	index[i]=i
	
print(index)
ftimes=[2,4,6,10,8,9]
index.sort(key=lambda i : ftimes[i])
print(index)




'''

maximal_set = set()
    prev_finish_time = 0
    for i in index:
        if stimes[i] >= prev_finish_time:
            maximal_set.add(i)
            prev_finish_time = ftimes[i]
 
    return maximal_set'''