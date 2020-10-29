

def lcs(a,b):
    lengths=[]
    for i in range(len(a)+1):
        arr=[0 for j in range(len(b)+1)]
        lengths.append(arr)
	
    print(lengths)
        
    #the data type passed in enumerate funtion should be iterable eg here are a and b which are #strings 
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            #print(i,x,j,y)
            '''for s1=ABCD and s2=AB
            i       x       j       y
            0       A       0       A
            0       A       1       B
            1       B       0       A      
            1       B       1       B
            2       C       0       A    
            2       C       1       B
            3       D       0       A    
            3       D       1       B'''
                    
            if x==y:
                lengths[i+1][j+1]=lengths[i][j]+1
                print('if',lengths)
            else:
                lengths[i+1][j+1]=max(lengths[i+1][j],lengths[i][j+1])
                print('else',lengths)
    return lengths[-1][-1]

s1 =input()
s2 =input()
print(lcs(s1,s2))
     

		
		
		
		
	
		
		
		
		
		
		
		
		
		