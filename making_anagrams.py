a=input()
b=input()
c=[0]*26
offset=ord('a')
for e in a:
    if e not in b:
        c[ord(e)-offset]=c[ord(e)-offset]+1
for f in b:
    if f not in a:
        c[ord(f)-offset]=c[ord(f)-offset]+1
print(c)
print(sum(c)


'''count=0
for i in c:
	count=count+abs(i)


a = input()
b = input()
cnt = [0] * 26
offset = ord('a')
for char in a:
	cnt[ord(char) - offset] += 1
for char in b:
	cnt[ord(char) - offset] -= 1
total = 0
for value in cnt:
	total += abs(value)
print(total)'''







































      