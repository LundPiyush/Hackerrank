cases = int(input())
for caseNo in range(cases):
	s = input()
	n = len(s)
	res = 0
	for j in range(1, n):
		#j ka loop is length ka loop eg:for length =4 we will check from 1 to 3 inclusive		
		print("j ka value",j,end=' ')
		cnt = {}
		for i in range(n - j + 1):
			print("i ka value",i,end=' ')
			subs = list(s[i:i + j])
			print("Before sorting",subs)
			subs.sort()
			print("After sorting",subs)
			subs = ''.join(subs)
			print(subs)
			if subs in cnt:
				cnt[subs] += 1
				print("if",cnt)
			else:
				cnt[subs] = 1
				print("else",cnt)
			res += cnt[subs] - 1
			print(res)
	print(res)
 