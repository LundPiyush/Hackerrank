class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class LinkList:
	def __init__(self):
		self.head=None
	
	def listlength(self):
		length=0
		currentNode=self.head
		while currentNode is not None:
			length+=1
			currentNode=currentNode.next
		return length
	def insertEnd(self,newNode):
		if self.head is None:
			self.head=newNode
		else:
			lastNode=self.head
			while lastNode.next is not None:
				lastNode=lastNode.next
			lastNode.next=newNode
	def insertAtBeg(self,headNode):
		tempNode=self.head#joh current head node hai usko temp mein store kiya
		self.head=headNode#head ko point karya new node pe 
		self.head.next=tempNode#head ka next ko point karya temp node pe
		del tempNode # delete the tempNode for further use
	def insert_at(self,newNode,pos):
		if pos<0 or pos>self.listlength():
			print("invalid position")
			return
		if pos is 0:
			self.insertAtBeg(newNode)
			return
		i=0
		currentNode=self.head
		while True:
			if i==pos:
				previousNode.next=newNode
				newNode.next=currentNode
				break
			previousNode=currentNode
			currentNode=currentNode.next
			i=i+1
		
			
		
	def printlist(self):
		if self.head is None:
			print("list is empty")

		currentNode=self.head
		while currentNode is not None:
			print(currentNode.data)
			currentNode=currentNode.next
			
			
first=Node("John")
linklist=LinkList()
linklist.insertEnd(first)
second=Node("Ben")

linklist.insertEnd(second)

third=Node("mathew")
linklist.insertAtBeg(third)

fourth=Node("piyush")
linklist.insert_at(fourth,10)
linklist.printlist()