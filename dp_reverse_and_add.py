def reverseDigit(n):
	a=0
	while n>0:
		a=a*10+n%10
		n=n//10
	return a
def Pallindrome(n):
	return (reverseDigit(n)==n)

def reverse_and_sum(n):
	rev_num=0
	while(n<=4294967295):
		rev_num=reverseDigit(n)
		n=n+rev_num
		if Pallindrome(n):
			print(n)
			break
		elif n>4294967295:
			print("no pallindrome")
			
n=int(input())
reverse_and_sum(n)