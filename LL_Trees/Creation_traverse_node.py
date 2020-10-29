#Node creation and traversing (static)
class daynames:
	def __init__(self,data):
		self.data=data
		self.next=None
e1=daynames('Mon')
e2=daynames('Tue')
e3=daynames('Wed')

e1.next=e3
e3.next=e2

thisvalue=e1
while thisvalue:
	print(thisvalue.data)
	thisvalue=thisvalue.next
'''n=5
for i in range(5):
	ele=input()
	e.dayname(ele)
	'''
	