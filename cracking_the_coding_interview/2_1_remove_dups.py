"""
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""


class Node:
	'''
	create a node
	'''
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	'''
	linked list operations
	'''
	def __init__(self):
		'''
		initiiate with empty head
		'''
		self.head = None

	def push(self, new_data):
		'''
		insert new_data at the beginning of a linked list
		'''
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insertAfter(self, prev_node, new_data):
		'''
		insert new_data after prev_node in a linked list
		'''
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def append(self, new_data):
		'''
		append new_data at the end of a linked list
		'''
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
		tail = self.head
		while tail.next:
			tail = tail.next
		tail.next = new_node

