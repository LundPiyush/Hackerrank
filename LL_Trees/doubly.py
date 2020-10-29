#doubly link list
#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
	def __init__(self, node_data):
		self.data = node_data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_node(self, node_data):
		node = DoublyLinkedListNode(node_data)

		if not self.head:
			self.head = node
		else:
			self.tail.next = node
			node.prev = self.tail
		self.tail = node
	def print_doubly_linked_list(self):
		if self.head is None:
			print("list is empty")
		currentNode=self.head
		while currentNode is not None:
			print(currentNode.data)
			currentNode=currentNode.next

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
	node=DoublyLinkedList()
	node.data=data
	node.next=None
	node.prev=None
    #i=0
	previous=None
	p=head
	while p!=None and p.data<=data:
		p=p.next
	node.next=p.next
	node.prev=p
	p.next=node
	p.next.prev=node
	return head




t = int(input())

for t_itr in range(t):
	llist_count = int(input())
	llist = DoublyLinkedList()

for _ in range(llist_count):
	llist_item = int(input())
	llist.insert_node(llist_item)

data = int(input())

llist1 = sortedInsert(llist.head, data)
llist.print_doubly_linked_list()
        

    
