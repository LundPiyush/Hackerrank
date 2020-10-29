#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(n,m,keyboards, drives, b):
    #
    # Write your code here.
	li=[0]
	#drives.sort(reverse=True)
	#keyboards.sort(reverse=True)
	for i in range(n):
		for j in range(m):
			#print(keyboards[i],drives[j])
			if keyboards[i]+drives[j]<=b:
				li.append(keyboards[i]+drives[j])
	if max(li)<=b and max(li)>0:
		print(max(li))
	else:
		print('-1')

if __name__ == '__main__':
	#fptr = open(os.environ['OUTPUT_PATH'], 'w')

	bnm = input().split()

	b = int(bnm[0])
	n = int(bnm[1])
	m = int(bnm[2])

	keyboards = list(map(int, input().rstrip().split()))
	drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

	moneySpent = getMoneySpent(n,m,keyboards, drives, b)

    #fptr.write(str(moneySpent) + '\n')

    #fptr.close()
