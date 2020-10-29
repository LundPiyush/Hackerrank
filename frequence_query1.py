d={}
a=[]
n=int(input())
for i in range(n):
	action,ele=input().split(' ')
	action=int(action)
	ele=int(ele)
	if action==1:
		if ele in d:#checking the element present in dict or not
			d[ele]=d[ele]+1#if present its cuurent count +1
			a[d[ele]+1]=a[d[ele]+1]+1
		else:
			d[ele]=1# if not present add the element with count=1
			a[1]+=1
	elif action ==2:
		if ele not in d:# if element is not in list take the next input
			continue
		if d[ele]==0:# if element count is zero keep as it is dont make -1
			continue
		else:
			d[ele]=d[ele]-1# decrement the element count
			a[d[ele]]=a[d[ele]]-1
			a[d[ele]-1]=a[d[ele]-1]+1
	else:
		if a[ele]>0:#checking the frequency in dict ka values
			print("1")
		else:
			print("0")
		
#print(d)

'''
bta 
nahi hoga joh main bol rahi thi
har count kitni baar aa raha aise ek list ya array bana sakte hai
like
humari dictionary hai
<5:2>
<3:3>
<4:1>
<7:2>
basically kya krna hai push n pop dono waqt array update yes


toh ek array samajh jiska index is yeh dictionary ke values and array 
ke vlaues hai yeh dictionar amai kitni baar aa rahe

kar tu mein jata hu
toh upar vale example ke liye array joh
[0,1,2,1] 

fir agar 
aaya  
3 3 toh hum dekhenge index 3 ka count 0 se zaada hai toh print 1 
no
print 1 tab karna hai jab koi key ka dictionay mein value 5 hai
wahi hua na
ab kar
inxed 3 ka count 0 se zaada tabhi hi hoga jab dictionary mai koi 
element ho jiska value 3 hai
haan
hoga isse
?
try kar'''