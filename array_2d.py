'''from array import*
A = []
for arr_i in range(6):
    arr_t = [int(items) for items in input().split(' ')]
    A.append(arr_t)

print(A)
s_max=-9*7

for r in range(len(A) -2):
	for col in range(len(A[r]) -2):
		a=A[r][col]	
		b=A[r][col + 1]	
		c=A[r][col + 2]
		d=A[r + 1][col + 1]
		e=A[r+2][col]		
		f=A[r+2][col+1]		
		g=A[r+2][col+2]
		sum=a+b+c+d+e+f+g
		#print(a,b,c,d,e,f,g,end="")
		#print(" ",sum)
		s_max=max(s_max,sum)
print(s_max)



A = []
for arr_i in range(6):
	arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	A.append(arr_t)
print(A)
smax = -9 * 7

for row in range(len(A) - 2):
	for column in range(len(A[row]) - 2):
		tl = A[row][column]
		tc = A[row][column + 1]
		tr = A[row][column + 2]
		mc = A[row + 1][column + 1]
		bl = A[row + 2][column]
		bc = A[row + 2][column + 1]
		br = A[row + 2][column + 2]
		print(tl,tc,tr,mc,bl,bc,br)
		s = tl + tc + tr + mc + bl + bc + br
		smax = max(s, smax)

print(smax)
'''
from array import*
A = []
for arr_i in range(6):
    arr_t = [int(items) for items in input().split(' ')]
    A.append(arr_t)

print(A)
#s_max=-9*7
s=[]

for r,col in enumerate(A):
    for r in range(4):
        for col in range(4):
            a=A[r][col]	
            b=A[r][col + 1]	
            c=A[r][col + 2]
            d=A[r + 1][col + 1]
            e=A[r+2][col]		
            f=A[r+2][col+1]		
            g=A[r+2][col+2]
            sum=a+b+c+d+e+f+g
		#print(a,b,c,d,e,f,g,end="")
		#print(" ",sum)
            s.append(sum)
print(max(s))