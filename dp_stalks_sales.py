#dp stalks and sales
test_cases=int(input())
#n=int(input())
#li=[int(x)for x in input().split(' ')]
#res=[]
while test_cases>0:
	n=int(input())
	li=[int(x)for x in input().split(' ')]
	min=li[0]	#ruk   34 55 19 55   mai bolu??ruk sochu haan sahi hai
	for i in range(len(li)):
		while li[i]<min:
			min=li[i]
			i=i+1
		a=i #min bhi kyu nikal rahe buy min mein karna hai n while
		#li[i]>li[i+1] se bhi hoga na nhi samjh rha yaar 
		j=a
			while li[j]<li[j+1]:#jab  
				j=j+1
			print("buy=",a,"sell at",j)
			k=j+1
			while(li[k]>li[k+1]):
				k=k+1
			b=li.index(li[k])
			print("buy ",b)
kya 
min = a[0] 
for (0 to n)
 while 

dee
samjha n likh ku rhi hai
aise samjhegakhud se aana chyie n code tera dekhke samjhega hi

arre baba tune joh for mai 1st minimum dhoondha 
woh wala while hi next minimum dhoondhega
condition alg hai likin while ki
nahi hai alag itna hai ki humne start mai 1st element ko minimum liya hainext time hum 
sell karne ke immideatily bad wale element ko minimum lenge
samjha?
joh bol rhi samjhrha
but condition alg rhi hai
sun 1st while mai i++ nah daala hai
for loop hai 
for pure ke liye hai yeh while 1st min dhoondh rahe han 











unn mujhe frst min mila
samjh min=34 hoga phele ok?
34 19 25 35 65 45 17 10 20 25 30
mai pani peeke aati hoon ok
kya




kal phone pe batati hoon











ok 10 pe buy hai ?

bol
yeh b wala waste hai na 
bta
dekh phele min doondha
eg 35 19 10 20 40
while se min aaya 10 haann
aincresing hai toh
next while se max milla 40 no bcz voh while tabhi khtm hoga jab decreasing mile koi du
sra cobdition bhi haan dalta hun
fir wapis se min ko 40 ka next set karde 
n for ke wajha se 
1st while wapis chalega

while ki condition dono alg hai likin








34 min hai phele 
fr 34 se chota joh aaya uska index is a
here 19 ka index is 1
so a is 1
while  false hua toh niche vala hoga 
tune if daala hai

piyush a kaise nikala hai?
b mtlb 10 mila mujhe 
nhi samjh rha 
fir 1 se loop start hoga 
ruk 19 mila min fr next min ke liye 19 se aage dekhna hai n , kese 

you will start  with 34 
tu dekhega agar next numebr 34 se bhadha hai toh jabtak koi chota number nahi milta
basicallys mil gya chota 19 kya karu 
agar 34 ke baad immideatily chota hai toh 34 ko bhul jaa
19 mila kya karu min dundu no 
19 ke baaad teri series increseing order mai hai na
19 will be purchase sell ke liye next min dunda hoga  n
haan nexr min 19 se bhdha bhi chalega?????
19 se bdha 45 hai 
dekh 19 pe buy kiya jabtak rate increse ho raha apne pass rakha jis din rate neeche gira bach 
diya rate 19 hai no
19 voh mtlb hua 45  fir huba 65a  
 
maine ek share buy kiya 19 pe abhi next day uska price 45 uske baad next day 65 
abhi samajh next day aaya 55 mai bech dungi 65 pe ok
fir 55 ko new min lenge n dekhenge usje baad waka ana chota hai toh nahi min nahi toh yeh 
wala series wapis
kya
eg:

34 19 25 35 65 45 17 10 20 25 30

sunn
19 pr kahriha
65 pe sell kiya
aage bta iske
45 min hoga n par 45 pe kharidungi toh nuksaan ho raha next day 
meine 65 pe sell kiya ab kese sochu 
abhi jabtak teri series 
decreseing order mai hai tabtak buy nahi karna hai
10 pe buy 30 pe sell yes
code karte hai samjha toh sahi

34 19 45 65 8			


kiya barabar hai but kesa while loops lgte hi jayega mera jabtak list end na ho
	
n^2 aayega 

mera dekh n upr tere hi dekh rahi 
ek while loop aayega kidr
0 se n-1
kidr bata sabse upar 
for dala hai

			chlega thodhi yeh kyu?	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	if n%2==0:
		m=n//2-1
	else:
		m=n//2
	li1=li[0:m+1]
	li2=li[m+1:n]
	a=li.index(min(li1))
	b=li.index(max(li1))
	#res.append((a,b))
	c=li.index(min(li2))
	d=li.index(max(li2))
	#res.append((c,d))
	print("("+str(a)+" "+str(b)+") "+"("+str(c)+" "+str(d)+")")
	li1.clear()
	li2.clear()

	test_cases-=1



	