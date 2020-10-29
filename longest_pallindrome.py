def pallindrome(s):
    if s==s[::-1]:
        
        return True
    else:
        return False
        
t=int(input())
for i in range(t):
    s=input()
    for i in range(len(s)):
        s1=s[i:len(s)]
        print(pallindrome(s1))