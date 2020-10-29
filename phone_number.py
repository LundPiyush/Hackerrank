'''import itertools

letters_map = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', 
               '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}

def possible_words(phone_number):
	letters_to_combine = (letters_map[digit] for digit in phone_number)
	print(letters_to_combine)
	for letters_group in itertools.product(*letters_to_combine):
		yield ''.join(letters_group)
a=[]
a=list(possible_words("23"))
print(a)'''

class Solution:
	def __init__(self):
		self.d={"0":"_","1":None,"2":"abc","3":"def","4":"ghi","5":"jkl",
		"6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
	def lettercombination(self,digits):
		combination=set()
		def recurse(rest_of_the_word,path_so_far):
			print(rest_of_the_word,path_so_far)
			if not rest_of_the_word:
				print("if",rest_of_the_word)
				combination.add(path_so_far)
				print(combination,"c")
				return
				
			first,rest=rest_of_the_word[0],rest_of_the_word[1:]
			print('first',first,'rest',rest)
			letters=self.d[first]
			print(letters)
			for letter in letters:
				recurse(rest,path_so_far+letter)
		recurse(digits,"")
		return combination
r=Solution()
res=r.lettercombination('23')
print(res)
		
		
		
		
		