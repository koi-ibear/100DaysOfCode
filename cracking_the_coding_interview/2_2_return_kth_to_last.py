"""
2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
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
	def kToLast(self, k):
		## two-pointers
		n0 = n1 = self.head
		step = 0
		while step < k:
			n1 = n1.next
			step += 1
		while n1 is not None:
			n0 = n0.next
			n1 = n1.next
		return n0

## test - 2.2
ll = LinkedList()
ll.push(4)
ll.push(5)
ll.push(1)
ll.push(4)
ll.push(8)
ll.push(1)
ll.dataList()
ll.kToLast(2)