"""
2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
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
	def dataList(self):
		res = []
		cur_node = self.head
		while cur_node is not None:
			res.append(cur_node.data)
			cur_node = cur_node.next
		return res
	def sumLists(self, x):

